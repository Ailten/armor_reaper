
from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

import random

class BulletWater(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'BulletWater'

        self.element_spell = Element.WATER
        self.type_damage = TypeDamage.MAGIC

        self.stamina_cost = 5

        self.priority_to_use = 100

        self.target_expected_count = 10

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):
        """
        -2~5 HP (Water)
        on every oponent.
        """

        for target in targets:
            launcher.atk(
                target=target,
                damage=random.randint(2, 5),
                element=self.element_spell,
                type_damage=self.type_damage
            )