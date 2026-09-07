
from enum import Enum

class SpellType(Enum):
    DEFAULT = 0,

    ATK = 1,
    HEAL = 2,
    BOOST = 3

    # ------>
    
    def getName(self) -> str:
        return self.name.lower()