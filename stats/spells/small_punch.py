
from ..spell import Spell
from ..spell_type import SpellType
from ..element import Element

from typing import Optional
import  typing

if typing.TYPE_CHECKING:
    from ..character import Character

class SmallPunch(Spell):

    def __init__(self):
        super().__init__()

        self.name = "small-punch"
        self.spell_type = SpellType.ATK

    # ------>

    #def use(self, user: "Character", target: Optional["Character"]|list["Character"]) -> list[str]:
    #    log: list[str] = []
    #
    #    # default spell (overide it in child class of all spell).
    #    log.append(f"{user.name} use {self.name}.")
    #
    #    if not type(target).__name__ == "Character":  # default spell focus only one target.
    #        return log
    #
    #    # make damage.
    #    damage_maked = user.atk(5, self.element_spell, target)
    #    log.append(f"{target.name} lose {damage_maked} HP ({self.element_spell.getName()}).")
    #    if target.is_dead:
    #        log.append(f"{target.name} is dead.")
    #
    #    # buy mana/stamina cost (or other).
    #    self.applyCoseSpell(user)
    #
    #    return log
    