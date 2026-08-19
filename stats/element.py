
from enum import Enum

class Element(Enum):
    NEUTRAL = (0, 'neutral'),

    HEARTH = (1, 'hearth'),
    FIRE = (2, 'fire'),
    AIR = (3, 'air'),
    WATER = (4, 'water')

    # ------>
    
    def getIndex(self) -> int:
        return self.value[0]
    
    def getName(self) -> str:
        return self.value[1]