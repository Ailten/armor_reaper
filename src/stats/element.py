
from enum import IntEnum
from .caracs import Caracs

class Element(IntEnum):
    NEUTRAL = 0,

    HEARTH = 1,
    FIRE = 2,
    AIR = 3,
    WATER = 4

    # ------>
    
    def getName(self) -> str:
        return self.name.lower()
    

class TypeDamage(IntEnum):
    NEUTRAL = 0,

    PHYSIC = 1,
    MAGIC = 2,
    MECANIC = 3

    # ------>
    
    def getName(self) -> str:
        return self.name.lower()
    
    def getCarac(self) -> Caracs|None:
        match self:
            case TypeDamage.PHYSIC:
                return Caracs.STRENGTH
            case TypeDamage.MAGIC:
                return Caracs.SAGESSE
            case TypeDamage.MECANIC:
                return Caracs.INTELIGENT
        return None