
from .jauche import Jauche
from .stats_element import StatsElement
from .element import Element
from .status_effect_collection import StatusEffectCollection
from .battle import Battle
from .spell import Spell

from typing import Optional

class Character:

    def __init__(self):
        self.name = 'anon'
        self.is_team_left = True
        self.battle: Battle|None = None
        self.is_dead = False

        self.hp = Jauche(10)
        self.stamina = Jauche(10)
        self.mana = Jauche(10)

        self.stats_mult = StatsElement()
        self.damages_incr = StatsElement()
        self.heal_incr = StatsElement()
        self.res_incr = StatsElement()
        self.res_mult = StatsElement()

        self.initiative = 0

        self.status_effects = StatusEffectCollection()

        self.spells: list[Spell] = []

    # ------>

    def atk(self, val: int|float, elem: Element, target: "Character") -> tuple[int, list[str]]:
        val_eval = val
        val_eval *= self.stats_mult.get(elem) / 100.0 + 1.0
        val_eval += self.damages_incr.get(elem)
        val_eval = max(val_eval, 0)

        damage_maked, log = target.takeDamage(val_eval, elem, damage_dealer = target)

        return (
            damage_maked,
            log
        )

    def heal(self, val: int|float, elem: Element, target: "Character") -> tuple[int, list[str]]:
        val_eval = val 
        val_eval += self.heal_incr.get(elem)
        val_eval *= self.stats_mult.get(elem) + 1.0
        val_eval = max(val_eval, 0)

        heal_maked, log = target.takeHeal(val_eval, elem, heal_dealer = target)

        return (
            heal_maked,
            log
        )

    # ------>

    def takeDamage(self, val: int|float, elem: Element, damage_dealer: Optional["Character"]) -> tuple[int, list[str]]:
        val_eval = val
        val_eval *= 1.0 - self.stats_mult.get(elem) / 100.0
        val_eval -= self.res_incr.get(elem)
        val_eval = max(val_eval, 0)

        self.hp.sub(val_eval)

        log = [f"{self.name} take -{val_eval} HP ({elem.getName()})."]

        if self.hp.val == 0:
            log_death = self.death(damage_dealer)
            log.append(log_death)

        return (
            val_eval,
            log
        )

    def takeHeal(self, val: int|float, elem: Element, heal_dealer: Optional["Character"]) -> tuple[int, list[str]]:
        val_eval = val
        
        self.hp.add(val_eval)

        return (
            val_eval, 
            [f"{self.name} take +{val_eval} HP ({elem.getName()})."]
        )

    # ------>

    def death(self, killer: Optional["Character"]) -> str:
        self.is_dead = True
        return f"{self.name} is dead !"

    # ------>

    def setIndex(self, battle: Battle):
        self.id = battle.getNextIndexCharacter()

    # ------>

    def doTurn(self) -> list[str]:
        log: list[str] = []

        # TODO: eval the most optimal spell to use (and use it).

        return log
