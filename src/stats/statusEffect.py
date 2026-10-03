
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from .character import Character

class StatusEffect:

    def __init__(self, launcher: "Character", target: "Character", turn_live: int|None):

        self.name = 'StatusEffect'

        self.launcher = launcher
        self.target = target

        self.turn_live = turn_live
        self.turn_when_apply = target.battle.turn

    # ------>

    def expire(self):
        self.destroy()
    def targetDie(self):
        self.destroy()
    def launcherDie(self):
        self.destroy()

    def destroy(self):  # when SE is destroy (all case).
        self.target.status_effects.remove(self)