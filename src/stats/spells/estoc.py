from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

import random

class Estoc(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'Estoc'

        self.element_spell = Element.AIR
        self.type_damage = TypeDamage.PHYSIC

        self.turn_cooldown = 2

        self.stamina_cost = 2

        self.priority_to_use = 200

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):
        """
        -4~6 HP (Air)
        -3~4 SP
        """

        if len(targets) == 0:
            return

        launcher.atk(
            target=targets[0],
            damage=random.randint(4, 6),
            element=self.element_spell,
            type_damage=self.type_damage
        )

        targets[0].subSP(random.randint(3, 4), False)