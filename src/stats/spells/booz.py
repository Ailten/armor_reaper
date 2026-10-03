from ..spell import Spell
from ..element import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

from ..statusEffects.elemsBoost import ElemsBoost

import random

class Booz(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'Booz'

        self.element_spell = Element.WATER
        self.type_damage = TypeDamage.MAGIC

        self.turn_cooldown = 5

        self.priority_to_use = 500

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):
        """
        +4~7 all elems (launcher) by lvl (3t).
        """

        range_stats = (4, 7)

        launcher.addStatusEffect(ElemsBoost(
            launcher=launcher,
            target=launcher,
            turn_live=3,
            stats={
                Caracs.STRENGTH: random.randint(range_stats[0] * launcher.lvl, range_stats[1] * launcher.lvl),
                Caracs.SAGESSE: random.randint(range_stats[0] * launcher.lvl, range_stats[1] * launcher.lvl),
                Caracs.INTELIGENT: random.randint(range_stats[0] * launcher.lvl, range_stats[1] * launcher.lvl)
            }
        ))