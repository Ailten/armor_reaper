
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

from ..spells.slash import Slash

def mercenaryTree(character: "Character"):
    character.spells.append( Slash() )