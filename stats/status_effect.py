
from .battle import Battle
from .status_effect_proc import StatusEffectProc

import typing

if typing.TYPE_CHECKING:
    from .character import Character

class StatusEffect:

    def __init__(self, battle: Battle):
        self.id = Battle.getNextIndexStatusEffect()

        self.whenShouldProc: list[StatusEffectProc] = []

        self.character_id_launch = None
        self.character_id_target = None
        self.turn_when_apply = 0
        self.turn_sould_stay = 1  # 0 or -1 == infinit.

        self.priority = 1000  # barely used.

    # ------>

    def proc(self, status_effect_proc: StatusEffectProc, package: dict):

        # check max status_effect call (for the character_turn).
        character_self = package.get("character_self")
        if type(character_self) is Character:
            battle = character_self.battle
            battle.status_effect_proc_count += 1
            if battle.status_effect_proc_count >= battle.status_effect_proc_max:
                return

        match status_effect_proc:
            case StatusEffectProc.WhenAtk:
                self.whenAtk(package)
                return
            case StatusEffectProc.WhenHeal:
                self.whenHeal(package)
                return
            case StatusEffectProc.WhenTakeDamage:
                self.whenTakeDamage(package)
                return
            case StatusEffectProc.WhenTakeHeal:
                self.whenTakeHeal(package)
                return
            case StatusEffectProc.WhenDead:
                self.whenDead(package)
                return
            case StatusEffectProc.WhenIsApply:
                self.whenIsApply(package)
                return
            case StatusEffectProc.WhenIsRemove:
                self.whenIsRemove(package)
                return

    # ------>

    def whenAtk(self, package: dict):
        pass
    def whenHeal(self, package: dict):
        pass
    def whenTakeDamage(self, package: dict):
        pass
    def whenTakeHeal(self, package: dict):
        pass
    def whenDead(self, package: dict):
        pass
    def whenIsApply(self, package: dict):
        pass
    def whenIsRemove(self, package: dict):
        pass