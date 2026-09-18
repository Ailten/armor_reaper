
from pydantic import BaseModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.stats.character import Character

class CharacterDto(BaseModel):
    id: int
    name: str
    skin: str

    hp: int
    mp: int
    sp: int

    @staticmethod
    def castFromCharacter(character: 'Character') -> 'CharacterDto':
        return CharacterDto(
            id=character.index,
            name=character.name,
            skin=character.skin,

            hp=character.hp.max_val,
            mp=character.mp.max_val,
            sp=character.sp.max_val
        )
    