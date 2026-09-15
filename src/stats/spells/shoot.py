
from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

import random

class Shoot(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'Shoot'

        self.element_spell = Element.AIR
        self.type_damage = TypeDamage.MECANIC

        self.priority_to_use = 90

        self.target_expected_count = 2

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):
        """
        (1/6)
          └ -12 HP (Air)
        (5/6)
          └ -1 HP (Air)
        on 2 oponent.
        """

        for i in range(self.target_expected_count):
            current_target = targets[i%len(targets)]
            
            if random.randint(1, 6) == 6:
                launcher.atk(
                    target=current_target,
                    damage=12,
                    element=self.element_spell,
                    type_damage=self.type_damage
                )
            else:
                launcher.atk(
                    target=current_target,
                    damage=1,
                    element=self.element_spell,
                    type_damage=self.type_damage
                )