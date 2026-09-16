
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from .character import Character

from .characters.slime import Slime


def mobsIdToCharacter(mob_id: int) -> Optional["Character"]:
    match mob_id:
        case 1:
            return Slime()
        
    return None
