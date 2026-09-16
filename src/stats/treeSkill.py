
from .treeSkills import *
from collections.abc import Callable

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from character import Character

def getTreeSkillInjector(tree_skill_id: int) -> Callable[["Character"], None]|None:
    match tree_skill_id:
        case 1:
            return mercenaryTree
        case 2:
            return mageTree
        case 3:
            return mekaTree
    
    return None