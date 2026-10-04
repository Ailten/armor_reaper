
from enum import IntEnum

class Caracs(IntEnum):

    # base stats.

    HP = 201
    MP = 202
    SP = 203

    # ------>
    
    STRENGTH = 1  # mul damage physic.
    SAGESSE = 2  # mul damage magic.
    INTELIGENT = 3  # use to boost mecanic.

    AGILITY = 4  # use to chance of dodge.
    DEXTERITY = 5  # use to chance to crit.

    LUCK = 6  # use to chance of loot.

    GUTS = 7  # add fix (damage/heal) for physic.
    CONSENTRATION = 8  # same for magic.
    CREATIVITY = 9 # same for mecanic.

    # ------>
    
    def getName(self) -> str:
        return self.name.lower()


