
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .character import Character

from .characters.slime import Slime


def mobsIdToCharacter(mob_id: int) -> "Character"|None:
    match mob_id:
        case 1:
            return Slime()
        
    return None
