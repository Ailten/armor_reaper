
from enum import Enum, auto

class Caracs(Enum[tuple(int, int)]):

    REST = (0, 1)

    # base stats.

    HP = (auto(), 1)
    MP = (auto(), 2)
    SP = (auto(), 2)

    # ------>
    
    PHYSIC_STATS = (auto(), 1)  # mul damage physic.
    MAGIC_STATS = (auto(), 1)  # mul damage magic.
    MECANIC_STATS = (auto(), 1)  # use to boost mecanic.

    PHYSIC_FIX = (auto(), 4)  # add fix (damage/heal) for physic.
    MAGIC_FIX = (auto(), 4)  # same for magic.
    MECANIC_FIX = (auto(), 4)  # same for mecanic.
    ALL_FIX = (auto(), 8)  # same for all thre.

    PHYSIC_RES_FIX = (auto(), 3)  # add fix res (take damage) for physic.
    MAGIC_RES_FIX = (auto(), 3)  # same for magic.
    MECANIC_RES_FIX = (auto(), 3)  # same for mecanic.
    ALL_RES_FIX = (auto(), 6)  # same for all thre.

    PHYSIC_FINAL_MULT = (auto(), 12)  # mult (damage/heal) apply after fix add for physic.
    MAGIC_FINAL_MULT = (auto(), 12)  # same for magic.
    MECANIC_FINAL_MULT = (auto(), 12)  # same for mecanic.

    DODGE_RATE = (auto(), 10)  # use to chance of dodge.
    CRIT_RATE = (auto(), 10)  # use to chance to crit.

    LOOT_RATE = (auto(), 3)  # use to chance of loot.

    # ------>
    
    def getName(self) -> str:
        return self.name.lower()


