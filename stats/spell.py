
import typing

if typing.TYPE_CHECKING:
    from .character import Character

class Spell:

    def __init__(self):
        self.name = 'unknow-spell'

        self.turn_cooldown = 0
        self.turn_when_use = int(float('-inf'))

    # ------>

    def use(self, user: Character, target: Character|list[Character]|None) -> list[str]:
        log: list[str] = []

        # default spell, do nothing (overide it in child class of all spell).
        log.append(f"{user.name} use {self.name}.")

        return log


