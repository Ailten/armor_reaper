
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

from ..spells.shoot import Shoot

def mekaTree(character: "Character"):
    character.spells.append( Shoot() )