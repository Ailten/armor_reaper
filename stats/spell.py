
import typing
from typing import Optional

from .element import Element

if typing.TYPE_CHECKING:
    from .character import Character

class Spell:

    def __init__(self):
        self.name = 'unknow-spell'

        self.turn_cooldown = 0
        self.turn_when_use = int(float('-inf'))

        self.element_spell: Element|None = None

        # TODO: crit ? alow, probability ...

    # ------>

    def use(self, user: "Character", target: Optional["Character"]|list["Character"]) -> list[str]:
        log: list[str] = []

        # default spell (overide it in child class of all spell).
        log.append(f"{user.name} use {self.name}.")

        if not target is Character:  # spell focus only one target.
            return log
        
        # make damage.
        damage_maked = user.atk(5, Element.HEARTH, target)
        log.append(f"{target.name} lose {damage_maked} HP ({Element.HEARTH.getName()}).")
        if target.is_dead:
            log.append(f"{target.name} is dead.")

        return log


