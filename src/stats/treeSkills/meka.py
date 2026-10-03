
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..character import Character

from ..spells.shoot import Shoot
from ..spells.booz import Booz

def mekaTree(character: "Character"):
    character.spells.append( Shoot() )

    if character.lvl >= 3:
        character.spells.append( Booz() )