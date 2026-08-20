
import typing

if typing.TYPE_CHECKING:
    from .character import Character

class Battle:
    status_effect_proc_max: int = 30

    def __init__(self):
        self.status_effect_index = 0
        self.character_index = 0
        self.turn = 0
        self.character_turn = 0

        self.characters: list[Character] = []

        self.status_effect_proc_count = 0

    # ------>

    def getNextIndexStatusEffect(self) -> int:
        index_out = self.status_effect_index
        self.status_effect_index += 1
        return index_out
    
    def getNextIndexCharacter(self) -> int:
        index_out = self.character_index
        self.character_index += 1
        return index_out
    
    # ------>

    def spawn(self, character_to_spawn: "Character"):
        character_to_spawn.setIndex(self)
        self.characters.append(character_to_spawn)
        character_to_spawn.battle = self

    # ------>

    def getLogSimulateFight(self) -> list[str]:
        log = ['--- fight stats ---']

        def increaseCharacterTurn(battle: Battle):
            battle.character_turn = (battle.character_turn + 1) % len(battle.characters)
            if battle.character_turn == 0:
                self.turn += 1

        while not self.isFightEnd():
            character_turn = self.characters[self.character_turn]

            if character_turn.is_dead:
                increaseCharacterTurn(self)
                continue

            # do turn.
            self.status_effect_proc_count = 0
            log_turn = character_turn.doTurn()
            log.append(log_turn)

            # expire effects.
            for c in self.characters:
                c.status_effects.expire(self)

            increaseCharacterTurn(self)

        log.append('--- fight end ---')
        return log

    # ------>

    def orderTurn(self):
        characters_ordered: list[Character] = []

        # get character from both teams.
        left_team = self.getCharactersFiltered(True)
        right_team = self.getCharactersFiltered(False)
        left_team.sort(key=lambda c: c.initiative, reverse=True)
        right_team.sort(key=lambda c: c.initiative, reverse=True)

        # eval first team pick.
        is_place_left_next = (
            len(left_team) >= len(right_team) if len(left_team) != len(right_team) else
            left_team[0].initiative >= right_team[0].initiative
        )

        # loop one by one characters team pick.
        while True:

            # end of pick (when one of theme is empty, finish by the other).
            if len(left_team) == 0:
                characters_ordered.extend(right_team)
                break
            if len(right_team) == 0:
                characters_ordered.extend(left_team)
                break

            # pick one team odd. 
            next_character = None
            if is_place_left_next:
                next_character = left_team.pop(0)
            else:
                next_character = right_team.pop(0)
            characters_ordered.append(next_character)
            is_place_left_next = not is_place_left_next

        # apply new list.
        self.characters = characters_ordered

    # ------>

    def getCharactersFiltered(self, is_left_team: bool|None=None, is_dead: bool|None=False) -> list["Character"]:
        return [ c for c in self.characters if (
            (is_left_team == None or c.is_team_left == is_left_team) and
            (is_dead == None or c.is_dead == is_dead)
        )]
    
    def getCharacterTurn(self) -> "Character":
        return self.characters[self.character_turn]

    # ------>

    def isFightEnd(self) -> bool:
        right_team_character_count = len(self.getCharactersFiltered(False))
        if right_team_character_count == 0:
            return True
        left_team_character_count = len(self.getCharactersFiltered(True))
        if left_team_character_count == 0:
            return True
        return False
