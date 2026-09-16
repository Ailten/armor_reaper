
from functools import cache

@cache
def xpNeedToLvlUp(lvl: int) -> int:
    
    xp_need = 10

    for i in range(1, lvl):
        xp_need = int(xp_need * 1.5)
    
    return xp_need