
from ..character import Character
from ..spell import Spell
from typing import Optional

from ..spells.small_punch import SmallPunch


class Rogue(Character):

    def __init__(self):
        super().__init__()

        self.name = 'rogue'

        self.spells.append(SmallPunch())

    # ------>

    #def chooseASpellToUse(self) -> tuple[Spell, Optional["Character"]|list["Character"]]|None:
    #    spell_can_use = self.getSpellUsable()
    #    if len(spell_can_use) == 0:
    #        return None
    #    
    #    spell_choose = spell_can_use[0]
    #    target = self.battle.getCharactersFiltered(is_left_team=not self.is_team_left)[0]
    #    return (
    #        spell_choose,
    #        target
    #    )
