from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

from ..statusEffects.caracsBoost import CaracsBoost

import random

class Booz(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'Booz'

        self.element_spell = Element.WATER
        self.type_damage = TypeDamage.MAGIC

        self.target_expected_count = 0
        self.turn_cooldown = 5

        self.priority_to_use = 500

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):
        """
        +2~3 ALL_FIX (3t) launcher.
        """

        range_stats = (2, 3)

        launcher.addStatusEffect(CaracsBoost(
            launcher=launcher,
            target=launcher,
            turn_live=3,
            stats={
                Caracs.ALL_FIX: random.randint(range_stats[0], range_stats[1])
            }
        ))