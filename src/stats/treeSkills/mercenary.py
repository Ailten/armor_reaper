
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

from ..spells.slash import Slash
from ..spells.estoc import Estoc

def mercenaryTree(character: "Character"):
    character.spells.append( Slash() )

    if character.lvl >= 3:
        character.spells.append( Estoc() )