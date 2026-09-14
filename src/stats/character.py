
from .jauche import Jauche
from .element import Element, TypeDamage
from .caracs import Caracs

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .battle import Battle
    from .spell import Spell

from .spells.wait import Wait

class Character:

    def __init__(self, dict_params: dict[str,any]={}):

        self.name = (
            dict_params.get('name') or
            dict_params.get('pseudo') or
            'Anon'
        )

        self.lvl = dict_params.get('lvl', 1)
        self.xp = dict_params.get('xp', 0)
        
        self.hp = Jauche(dict_params.get('hp', 20))
        self.mp = Jauche(dict_params.get('mp', 20))
        self.sp = Jauche(dict_params.get('sp', 20))

        self.spells: list[Spell] = [ Wait ]

        self.is_death = False

        # set in battle.
        self.index: int|None = None
        self.is_left_team: bool|None = None
        self.battle: 'Battle'|None = None

    # ------>

    def addStats(self, stats: dict[Caracs,int], is_sub: bool=False):
        for k,v in stats.items():
            value = v if not is_sub else - v
            carac_name = k.getName()
            is_character_has = hasattr(self, carac_name)
            base_carac = 0 if not is_character_has else getattr(self, carac_name)
            if isinstance(base_carac, Jauche):
                base_carac.val += value
                base_carac.max_val += value
                continue
            if not is_character_has:
                self.__setattr__(carac_name, value)
                continue
            self.__setattr__(carac_name, base_carac + value)

    def getStats(self, carac: Caracs) -> int:
        carac_name = carac.getName()
        if hasattr(self, carac_name):
            carac_get = getattr(self, carac_name)
            if isinstance(carac_get, Jauche):
                return carac_get.val
            return carac_get
        return 0

    # ------>

    def atk(self, 
        target: 'Character',
        damage: int,
        element: Element=Element.NEUTRAL,
        type_damage: TypeDamage=TypeDamage.NEUTRAL
    ):
        damage_eval = float(damage)

        # eval mult.
        damage_eval *= self.getMultTypeDamage(type_damage)

        damage_eval = max(int(damage_eval), 0)

        target.takeDamage(
            laucher=self,
            damage=damage_eval,
            element=element,
            type_damage=type_damage
        )

    def takeDamage(self,
        laucher: 'Character'|None,
        damage: int,
        element: Element=Element.NEUTRAL,
        type_damage: TypeDamage=TypeDamage.NEUTRAL
    ):
        damage_eval = float(damage)
        
        # eval res mult.
        damage_eval /= self.getMultTypeRes(type_damage, laucher)

        damage_eval = max(int(damage_eval), 0)

        self.hp.sub(damage_eval)

        if self.hp.val <= 0:
            self.death()

    def death(self,
        killer: 'Character'|None
    ):
        self.is_death = True

    def heal(self, 
        target: 'Character',
        heal: int,
        element: Element=Element.NEUTRAL,
        type_damage: TypeDamage=TypeDamage.NEUTRAL
    ):
        heal_eval = float(heal)

        # eval mult.
        damage_eval *= self.getMultTypeDamage(type_damage)

        heal_eval = max(int(heal_eval), 0)

        target.takeHeal(
            laucher=self,
            heal=heal_eval,
            element=element,
            type_damage=type_damage
        )

    def takeHeal(self,
        laucher: 'Character'|None,
        heal: int,
        element: Element=Element.NEUTRAL,
        type_damage: TypeDamage=TypeDamage.NEUTRAL
    ):
        heal_eval = float(heal)
        
        heal_eval = max(int(heal_eval), 0)

        self.hp.add(heal_eval)

    # ------>

    def getMultTypeDamage(self, type_damage: TypeDamage) -> float:
        stats_mult = self.getStats(type_damage.getCarac())
        return (stats_mult / 100.0) + 1.0
    
    def getMultTypeRes(self, type_damage: TypeDamage, oponent: 'Character') -> float:
        carac = type_damage.getCarac()
        stats = self.getStats(carac)
        stats -= oponent.getStats(carac)
        stats = max(stats, 0)
        return (stats / 100.0) + 1.0