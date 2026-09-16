
from .element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .character import Character

class Spell:

    def __init__(self):
        self.name = 'unknow-spell'

        self.turn_cooldown = 0
        self.turn_when_use = 0  # stock last turn when use.

        self.element_spell = Element.NEUTRAL
        self.type_damage = TypeDamage.NEUTRAL

        self.mana_cost = 0
        self.stamina_cost = 0

        self.target_expected_count = 1  # 0, 1, N.
        self.is_target_expected_oponent = True  # True = target should be an oponent team.

        self.priority_to_use = 0

    # ------>

    # to overide.
    def use(self, launcher: "Character", targets: list["Character"]):
        
        # make damage.
        #launcher.atk(1, self.element_spell, targets[0])

        launcher.battle.logs.append(f'nothing happend.')

    def bodyUse(self, launcher: "Character", targets: list["Character"]):

        # log.
        launcher.battle.logs.append(f'{launcher.name} use {self.name} !')

        # use.
        self.use(launcher, targets)

        # buy mana/stamina cost (or other).
        self.applyCoseSpell(launcher)
    
    # ------>

    def isCanUse(self, owner: "Character") -> bool:
        if self.mana_cost > owner.mp.val:
            return False
        if self.stamina_cost > owner.sp.val:
            return False
        if (self.turn_when_use - owner.battle.turn) > self.turn_cooldown:  # verify cooldown turn.
            return False
        return True
    
    def applyCoseSpell(self, owner: "Character"):
        owner.mp.sub(self.mana_cost)
        owner.sp.sub(self.stamina_cost)
        self.turn_when_use = owner.battle.turn  # update cooldown turn.

    # ------>

    def orderTargetPriority(self, targets: list["Character"]):
        targets.sort(key=lambda t: t.hp.val)