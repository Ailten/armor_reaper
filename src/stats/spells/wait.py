from ..spell import Spell

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

class Wait(Spell):

    def __init__(self):
        super().__init__()

        self.name = 'Wait'

        self.priority_to_use = 0

    # ------>

    def use(self, launcher: "Character", targets: list["Character"]):

        launcher.sp.add(2)
        launcher.mp.add(2)

        # buy mana/stamina cost (or other).
        self.applyCoseSpell(launcher)