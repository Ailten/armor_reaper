
from enum import IntEnum

class Caracs(IntEnum):

    # base stats.

    HP: 201
    MP: 202
    SP: 203

    # ------>
    
    STRENGTH: 1  # mul damage phyisic.
    SAGESSE: 2  # mul damage magic.
    INTELIGENT: 3  # use to boost mecanic.

    AGILITY: 3  # use to chance of dodge.
    DEXTERITY: 4  # use to chance to crit.

    LUCK: 5  # use to chance of loot.

    # ------>
    
    def getName(self) -> str:
        return self.name.lower()


