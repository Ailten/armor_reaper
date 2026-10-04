
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
    
    def getCaracStats(self) -> Caracs|None:
        match self:
            case TypeDamage.PHYSIC:
                return Caracs.PHYSIC_STATS
            case TypeDamage.MAGIC:
                return Caracs.MAGIC_STATS
            case TypeDamage.MECANIC:
                return Caracs.MECANIC_STATS
        return None
    
    def getCaracFix(self) -> Caracs|None:
        match self:
            case TypeDamage.PHYSIC:
                return Caracs.PHYSIC_FIX
            case TypeDamage.MAGIC:
                return Caracs.MAGIC_FIX
            case TypeDamage.MECANIC:
                return Caracs.MECANIC_FIX
        return None
    
    def getCaracResFix(self) -> Caracs|None:
        match self:
            case TypeDamage.PHYSIC:
                return Caracs.PHYSIC_RES_FIX
            case TypeDamage.MAGIC:
                return Caracs.MAGIC_RES_FIX
            case TypeDamage.MECANIC:
                return Caracs.MECANIC_RES_FIX
        return None
    
    def getCaracMultFinal(self) -> Caracs|None:
        match self:
            case TypeDamage.PHYSIC:
                return Caracs.PHYSIC_FINAL_MULT
            case TypeDamage.MAGIC:
                return Caracs.MAGIC_FINAL_MULT
            case TypeDamage.MECANIC:
                return Caracs.MECANIC_FINAL_MULT
        return None
