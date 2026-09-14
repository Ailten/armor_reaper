
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

        self.priority_to_use = 120

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):

        if random.randint(1, 6) == 6:
            launcher.atk(
                target=targets[0],
                damage=15,
                element=self.element_spell,
                type_damage=self.type_damage
            )
        else:
            launcher.atk(
                target=targets[0],
                damage=1,
                element=self.element_spell,
                type_damage=self.type_damage
            )

        # buy mana/stamina cost (or other).
        self.applyCoseSpell(launcher)