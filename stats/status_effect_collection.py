from .status_effect import StatusEffect
from .status_effect_proc import StatusEffectProc
from .battle import Battle

import typing

if typing.TYPE_CHECKING:
    from .character import Character

class StatusEffectCollection:
    loop_proc_max: int = 6
    
    def __init__(self):
        self.status_effects: list[StatusEffect] = []

        self.loop_proc_count = 0

    # ------>

    def add(self, status_effect_to_add: StatusEffect):
        for i in range(len(self.status_effects)):  # add in right priority.
            se = self.status_effects[i]
            if se.priority > status_effect_to_add:
                self.status_effects.insert(i, status_effect_to_add)
                return
        self.status_effects.append(status_effect_to_add)

    def sub(self, status_effect_to_sub: StatusEffect):
        self.status_effects.remove(status_effect_to_sub)

    # ------>

    def proc(self, status_effect_proc: StatusEffectProc, package: dict):
        if self.loop_proc_count >= self.loop_proc_max:
            return
        self.loop_proc_count += 1

        copy_status_effects = self.status_effects[::]  # copy list, to prevent error from editing (add, remove) it during browse (and losing index).
        for se in copy_status_effects:
            
            if not status_effect_proc in se.whenShouldProc:
                continue

            se.proc(status_effect_proc, package)

        self.loop_proc_count -= 1

    # ------>
    
    def expire(self, battle: Battle):
        i = len(self.status_effects)
        while i != 0:
            i -= 1
            se = self.status_effects[i]

            if se.turn_sould_stay < 1:  # infinit turn.
                continue

            turn_when_expire = se.turn_when_apply + se.turn_sould_stay
            if battle.turn < turn_when_expire:
                continue
            if battle.turn > turn_when_expire:  # barelly used.
                self.sub(se)
                continue
            
            if battle.getCharacterTurn().id == se.character_id_launch:
                self.sub(se)
                continue

    def expireByDeath(self, battle: Battle, character_who_dead: "Character"):
        i = len(self.status_effects)
        while i != 0:
            i -= 1
            se = self.status_effects[i]

            if se.turn_sould_stay < 1:  # infinit turn (do not remove infinit effect when launcher dead).
                continue

            if se.character_id_launch == character_who_dead.id:
                self.sub(se)
                continue
