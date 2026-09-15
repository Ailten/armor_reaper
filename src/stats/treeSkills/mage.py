
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

from ..spells.fireBall import FireBall

def mageTree(character: "Character"):
    character.spells.append( FireBall() )