
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

from ..spells.fireBall import FireBall
from ..spells.magicalDrain import MagicalDrain

def mageTree(character: "Character"):
    character.spells.append( FireBall() )

    if character.lvl >= 3:
        character.spells.append( MagicalDrain() )