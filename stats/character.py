
from .jauche import Jauche
from .stats_element import StatsElement
from .element import Element
from .status_effect_collection import StatusEffectCollection
from .battle import Battle
from .spell import Spell
from .status_effect_proc import StatusEffectProc
from .status_effect import StatusEffect

from typing import Optional

class Character:

    def __init__(self):
        self.name = 'anon'
        self.is_team_left = True
        self.battle: Battle|None = None
        self.is_dead = False

        self.level = 1
        self.xp = 0

        self.hp = Jauche(10)
        self.stamina = Jauche(10)
        self.mana = Jauche(10)

        self.stats_mult = StatsElement()
        self.damages_incr = StatsElement()
        self.heal_incr = StatsElement()
        self.res_incr = StatsElement()
        self.res_mult = StatsElement()

        self.initiative = 0  # use to start turn early.
        self.dexterity = 0  # use to boost CC chance.
        self.luck = 0  # use to boost loot rate.

        self.status_effects = StatusEffectCollection()

        self.spells: list[Spell] = []

    # ------>

    def atk(self, val: int|float, elem: Element, target: "Character") -> tuple[int, list[str]]:
        val_eval = val
        val_eval *= self.stats_mult.get(elem) / 100.0 + 1.0
        val_eval += self.damages_incr.get(elem)
        val_eval = max(int(val_eval), 0)

        # status_effect.
        package_effect = {
            "character_self": self,
            "val": val,
            "val_eval": val_eval,
            "elem": elem,
            "target": target
        }
        self.status_effects.proc(StatusEffectProc.WhenAtk, package_effect)
        val_eval = package_effect.get(val_eval)

        damage_maked, log = target.takeDamage(val_eval, elem, damage_dealer = target)

        return (
            damage_maked,
            log
        )

    def heal(self, val: int|float, elem: Element, target: "Character") -> tuple[int, list[str]]:
        val_eval = val 
        val_eval += self.heal_incr.get(elem)
        val_eval *= self.stats_mult.get(elem) + 1.0
        val_eval = max(int(val_eval), 0)

        # status_effect.
        package_effect = {
            "character_self": self,
            "val": val,
            "val_eval": val_eval,
            "elem": elem,
            "target": target
        }
        self.status_effects.proc(StatusEffectProc.WhenHeal, package_effect)
        val_eval = package_effect.get(val_eval)

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
        val_eval = max(int(val_eval), 0)

        # status_effect.
        package_effect = {
            "character_self": self,
            "val": val,
            "val_eval": val_eval,
            "elem": elem,
            "damage_dealer": damage_dealer
        }
        self.status_effects.proc(StatusEffectProc.WhenTakeDamage, package_effect)
        val_eval = package_effect.get(val_eval)

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
        val_eval = int(val)

        # status_effect.
        package_effect = {
            "character_self": self,
            "val": val,
            "val_eval": val_eval,
            "elem": elem,
            "heal_dealer": heal_dealer
        }
        self.status_effects.proc(StatusEffectProc.WhenTakeHeal, package_effect)
        val_eval = package_effect.get(val_eval)
        
        self.hp.add(val_eval)

        return (
            val_eval, 
            [f"{self.name} take +{val_eval} HP ({elem.getName()})."]
        )

    # ------>

    def death(self, killer: Optional["Character"]) -> str:
        self.is_dead = True

        # status_effect.
        package_effect = {
            "character_self": self,
            "killer": killer
        }
        self.status_effects.proc(StatusEffectProc.WhenDead, package_effect)

        return f"{self.name} is dead !"

    # ------>

    def setIndex(self, battle: Battle):
        self.id = battle.getNextIndexCharacter()

    # ------>

    def doTurn(self) -> list[str]:
        log: list[str] = []

        # choose spell to use (and target).
        spell_choose = target = None
        spell_choose_and_target = self.chooseASpellToUse()
        if spell_choose_and_target == None:
            spell_choose = Spell.getDefaultSpell()
        else:
            spell_choose, target = spell_choose_and_target

        # use the spell (and get log generate).
        log_spell_used = spell_choose.use(self, target)
        log.extend(log_spell_used)

        return log
    
    def chooseASpellToUse(self) -> tuple[Spell, Optional["Character"]|list["Character"]]|None:
        spell_can_use = self.getSpellUsable()
        if len(spell_can_use) == 0:
            return None
        
        spell_choose = spell_can_use[0]
        target = self.battle.getCharactersFiltered(is_left_team=not self.is_team_left)[0]
        return (
            spell_choose,
            target
        )
    
    # ------>

    def getSpellUsable(self) -> list[Spell]:
        return [s for s in self.spells if s.isCanUse(self, self.battle)]

    # ------>

    def addStatusEffet(self, status_effect_to_add: StatusEffect):
        self.status_effects.add(status_effect_to_add)

        # status_effect.
        package_effect = {
            "character_self": self
        }
        self.status_effects.proc(StatusEffectProc.WhenIsApply, package_effect)

    def subStatusEffect(self, status_effect_to_sub: StatusEffect):
        self.status_effects.sub(status_effect_to_sub)

        # status_effect.
        package_effect = {
            "character_self": self
        }
        self.status_effects.proc(StatusEffectProc.WhenIsRemove, package_effect)

        # remove status_effect (by death).
        for c in self.battle.characters:
            c.status_effects.expireByDeath(self.battle, self)




