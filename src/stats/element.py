
from enum import Enum

class Element(Enum):
    NEUTRAL = 0,

    HEARTH = 1,
    FIRE = 2,
    AIR = 3,
    WATER = 4

    # ------>
    
    def getName(self) -> str:
        return self.name.lower()