
from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

import random

class MagicalDrain(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'MagicalDrain'

        self.element_spell = Element.WATER
        self.type_damage = TypeDamage.MAGIC

        self.mana_cost = 1

        self.priority_to_use = 10

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):
        """
        (steal) 4~6 MP
        """

        if len(targets) == 0:
            return
        
        amount_steal = random.randint(4,6)
        target = targets[0]
        mp_target = target.mp.val
        target.subMP(amount_steal, False)
        amount_steal = mp_target - target.mp.val  # get dif mp reduced.
        launcher.addMP(amount_steal, False)

    # ------>

    def isCanUse(self, owner: "Character") -> bool:
        if not super().isCanUse(owner):
            return False
        if owner.mp.val == owner.mp.max_val:  # already full mana.
            return False
        if sum([ c.mp.val for c in owner.battle.characters if c.is_left_team != owner.is_left_team ]) == 0:
            return False  # no any MP to steal in oponent.
        return True
    
    # ------>

    def orderTargetPriority(self, targets: list["Character"]):
        targets.sort(key=lambda t: t.mp.val, reverse=True)  # priority to the oponenent with the most mana.