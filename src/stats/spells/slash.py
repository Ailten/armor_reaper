from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

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

        launcher.atk(
            target=targets[0],
            damage=5,
            element=self.element_spell,
            type_damage=self.type_damage
        )

        # buy mana/stamina cost (or other).
        self.applyCoseSpell(launcher)