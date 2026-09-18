
from .treeSkills import *
from collections.abc import Callable

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from character import Character

from enum import IntEnum

class TreeSkill(IntEnum):
    MercaryTree = 1
    MageTree = 2
    MekaTree = 3

def injectTreeSkill(character: "Character", tree_skill_id: int):

    match tree_skill_id:
        case 1:
            character.skin = character.skin or 'Mercenary'
            return mercenaryTree(character)
        case 2:
            character.skin = character.skin or 'Mage'
            return mageTree(character)
        case 3:
            character.skin = character.skin or 'Meka'
            return mekaTree(character)