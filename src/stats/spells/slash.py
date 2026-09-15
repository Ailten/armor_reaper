from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

import random

class Slash(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'Slash'

        self.element_spell = Element.HEARTH
        self.type_damage = TypeDamage.PHYSIC

        self.stamina_cost = 1

        self.priority_to_use = 100

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):
        """
        -3~5 HP (Hearth)
        """

        launcher.atk(
            target=targets[0],
            damage=random.randint(3, 5),
            element=self.element_spell,
            type_damage=self.type_damage
        )