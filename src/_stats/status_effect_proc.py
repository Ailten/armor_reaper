
from enum import Enum

class StatusEffectProc(Enum):
    WhenAtk = 0,
    WhenHeal = 1,
    WhenTakeDamage = 2,
    WhenTakeHeal = 3,
    WhenDead = 4,

    WhenIsApply = 5,
    WhenIsRemove = 6
