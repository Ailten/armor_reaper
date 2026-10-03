
from ..statusEffect import StatusEffect
from ..caracs import Caracs

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class ElemsBoost(StatusEffect):

    def __init__(self, launcher: "Character", target: "Character", turn_live: int|None, stats: dict[Caracs, int]):

        super().__init__(launcher, target, turn_live)

        self.name = 'ElemsBoost'

        # stock stats for remove when destroy.
        self.stats = stats

        self.target.addStats(stats)

    # ------>

    def destroy(self):

        self.target.addStats(self.stats, is_sub=True)

        super().destroy()

