
from .jauche import Jauche
from .element import Element, TypeDamage
from .caracs import Caracs

from typing import TYPE_CHECKING, Optional
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

        self.spells: list[Spell] = [ Wait() ]

        self.is_death = False

        # set in battle.
        self.index: int|None = None
        self.is_left_team: bool|None = None
        self.battle: 'Battle'|None = None

        self.is_player: bool = dict_params.get('is_player', True)
        self.skin: str|None = None if self.is_player else self.name

    # ------>

    # use in futur, for equipement or statusEffect.
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

    def getStats(self, carac: Caracs|None) -> int:
        if carac == None:
            return 0
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
            launcher=self,
            damage=damage_eval,
            element=element,
            type_damage=type_damage
        )

    def takeDamage(self,
        launcher: Optional['Character'],
        damage: int,
        element: Element=Element.NEUTRAL,
        type_damage: TypeDamage=TypeDamage.NEUTRAL
    ):
        damage_eval = float(damage)
        
        # eval res mult.
        damage_eval /= self.getMultTypeRes(type_damage, launcher)

        damage_eval = max(int(damage_eval), 0)

        damage_make = self.hp.sub(damage_eval)

        self.battle.logs.append((f'{self.name} : -{damage_make} HP', self.index))

        if self.hp.val <= 0 and self.is_death == False:
            self.death(launcher)

    def death(self,
        killer: Optional['Character']|None=None
    ):
        self.is_death = True

        # log.
        self.battle.logs.append((f'{self.name} die.', self.index))

        # check who win.
        self.battle.isFightEnd()

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
            launcher=self,
            heal=heal_eval,
            element=element,
            type_damage=type_damage
        )

    def takeHeal(self,
        launcher: Optional['Character'],
        heal: int,
        element: Element=Element.NEUTRAL,
        type_damage: TypeDamage=TypeDamage.NEUTRAL
    ):
        heal_eval = float(heal)
        
        heal_eval = max(int(heal_eval), 0)

        heal_make = self.hp.add(heal_eval)

        self.battle.logs.append((f'{self.name} : +{heal_make} HP', self.index))

    # ------>

    def getMultTypeDamage(self, type_damage: TypeDamage) -> float:
        carac = type_damage.getCarac()
        stats = 0 if carac == None else self.getStats(carac)
        return (stats / 100.0) + 1.0
    
    def getMultTypeRes(self, type_damage: TypeDamage, oponent: 'Character') -> float:
        carac = type_damage.getCarac()
        stats = 0 if carac == None else self.getStats(carac)
        stats -= 0 if carac == None else oponent.getStats(carac)
        stats = max(stats, 0)
        return (stats / 100.0) + 1.0
    
    # ------>

    def addSP(self, sp_add: int):
        sp_add = self.sp.add(sp_add)

        # logs.
        self.battle.logs.append((f'{self.name} : +{sp_add} SP', self.index))

    def subSP(self, sp_sub: int):
        sp_sub = self.sp.add(sp_sub)

        # logs.
        self.battle.logs.append((f'{self.name} : -{sp_sub} SP', self.index))

    def addMP(self, mp_add: int):
        mp_add = self.mp.add(mp_add)

        # logs.
        self.battle.logs.append((f'{self.name} : +{mp_add} MP', self.index))

    def subMP(self, mp_sub: int):
        mp_sub = self.mp.add(mp_sub)

        # logs.
        self.battle.logs.append((f'{self.name} : -{mp_sub} MP', self.index))

    # ------>