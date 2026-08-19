
import typing
from typing import Optional

from .element import Element
from .spell_type import SpellType

if typing.TYPE_CHECKING:
    from .character import Character
    from .battle import Battle

class Spell:
    default_spell: "Spell" = None

    def __init__(self):
        self.name = 'unknow-spell'

        self.turn_cooldown = 0
        self.turn_when_use = int(float('-inf'))

        self.element_spell = Element.NEUTRAL
        self.spell_type = SpellType.DEFAULT

        self.mana_cost = 0
        self.stamina_cost = 0

        self.is_can_crit = False
        self.crit_purcent = 0

    # ------>

    def use(self, user: "Character", target: Optional["Character"]|list["Character"]) -> list[str]:
        log: list[str] = []

        # default spell (overide it in child class of all spell).
        log.append(f"{user.name} use {self.name}.")

        if not target is Character:  # default spell focus only one target.
            return log
        
        # make damage.
        damage_maked = user.atk(5, Element.HEARTH, target)
        log.append(f"{target.name} lose {damage_maked} HP ({Element.HEARTH.getName()}).")
        if target.is_dead:
            log.append(f"{target.name} is dead.")

        # buy mana/stamina cost (or other).
        self.applyCoseSpell(user)

        return log
    
    # ------>

    def isCanUse(self, user: "Character", battle: Battle) -> bool:
        if self.mana_cost > user.mana.val:
            return False
        if self.stamina_cost > user.stamina.val:
            return False
        if (battle.turn - self.turn_when_use) > self.turn_cooldown:  # verify cooldown turn.
            return False
        return True
    
    def applyCoseSpell(self, user: "Character", battle: Battle):
        user.mana.sub(self.mana_cost)
        user.stamina.sub(self.stamina_cost)
        self.turn_when_use = battle.turn  # update cooldown turn.

    # ------>

    @staticmethod
    def getDefaultSpell() -> "Spell":

        # singleton default spell.
        if Spell.default_spell == None:
            Spell.default_spell = Spell()
            Spell.default_spell.name = "wait"

        return Spell.default_spell



