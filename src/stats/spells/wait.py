from ..spell import Spell

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

import random

class Wait(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'Wait'

        self.priority_to_use = 0

        self.target_expected_count = 0
        self.is_target_expected_oponent = False

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):
        """
        +2~4 SP (self)
        +2~4 MP (self)
        """

        launcher.addSP(random.randint(2, 4))
        launcher.addMP(random.randint(2, 4))