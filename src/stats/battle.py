
from .character import Character

class Battle:

    def __init__(self):
        self.turn = 0
        self.character_turn = 0

        self.characters: list[Character] = []

        # index count (to assigne).
        self.index_character = 0

        self.logs: list[str] = []

        self.is_left_win: bool|None = None

    # ------>

    def getCharacterTurn(self) -> Character:
        self.characters[self.character_turn]

    def increaseCharacterTurn(self):
        # prevent from infinit recurs.
        if any([c.is_death for c in self.characters]):
            return
        
        self.character_turn += 1
        if self.character_turn >= len(self.characters):
            self.turn += 1
        self.character_turn %= len(self.characters)

        # move to next character if next one is dead.
        if self.getCharacterTurn().is_death:
            self.increaseCharacterTurn()

    def isFightEnd(self) -> bool:
        teams = [0, 0]
        for c in self.characters:
            if c.is_death:
                continue
            teams[0 if c.is_left_team else 1] += 1
            if teams[0] > 0 and teams[1] > 0:
                return False
        
        # stock info who win (prevent double kill).
        if self.is_left_win == None:
            self.is_left_win = teams[0] > 0

        return True
    
    # ------>

    def spawn(self, character_to_spawn: "Character", is_left_team: bool):
        self.index_character += 1
        character_to_spawn.index = self.index_character
        self.characters.append(character_to_spawn)
        character_to_spawn.battle = self
        character_to_spawn.is_left_team = is_left_team

    # ------>

    def simulateFight(self):

        # prep fight.
        self.orderTurn()
        for c in self.characters:  # order spells.
            c.spells.sort(key=lambda s: s.priority_to_use, reverse=True)

        # log.
        self.logs.append('fight start !')

        while self.is_left_win == None:
            character_turn = self.characters[self.character_turn]

            # pick spell to use.
            spell = None
            for s in character_turn.spells:
                if s.isCanUse():
                    spell = s
                    break

            # pick target.
            targets = [ c for c in self.characters if (
                spell.is_target_expected_oponent == (character_turn.is_left_team == c.is_left_team)
            ) ]
            spell.orderTargetPriority(targets)  # order.
            targets = targets[:spell.target_expected_count]

            # use spell.
            spell.bodyUse(
                launcher=character_turn,
                target=targets
            )

            # increase character turn (and turn).
            self.increaseCharacterTurn()

        # log.
        self.logs.append('fight end !')
        team_win = 'left' if self.is_left_win else 'right'
        self.logs.append(f'{team_win} win !')

    # ------>

    # re-order character turn.
    def orderTurn(self):

        # get character from both teams.
        left_team = [c for c in self.characters if c.is_left_team]
        right_team = [c for c in self.characters if not c.is_left_team]
        left_team.sort(key=lambda c: c.lvl, reverse=True)
        right_team.sort(key=lambda c: c.lvl, reverse=True)

        # eval first team pick.
        is_place_left_next = (
            len(left_team) >= len(right_team) if len(left_team) != len(right_team) else
            left_team[0].lvl >= right_team[0].lvl
        )

        self.characters.clear()

        # loop one by one characters team pick.
        while True:

            # end of pick (when one of theme is empty, finish by the other).
            if len(left_team) == 0:
                self.characters.extend(right_team)
                break
            if len(right_team) == 0:
                self.characters.extend(left_team)
                break

            # pick one team odd. 
            next_character = None
            if is_place_left_next:
                next_character = left_team.pop(0)
            else:
                next_character = right_team.pop(0)
            self.characters.append(next_character)
            is_place_left_next = not is_place_left_next

