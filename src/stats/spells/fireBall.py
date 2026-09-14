
from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class FireBall(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'FireBall'

        self.turn_cooldown = 1

        self.element_spell = Element.FIRE
        self.type_damage = TypeDamage.MAGIC

        self.mana_cost = 3

        self.priority_to_use = 120

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):

        launcher.atk(
            target=targets[0],
            damage=8,
            element=self.element_spell,
            type_damage=self.type_damage
        )

        # buy mana/stamina cost (or other).
        self.applyCoseSpell(launcher)