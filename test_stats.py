

# Test.


from stats import Battle
from stats.characters import Rogue, Slime


chevalier = Rogue()

slime = Slime()


fight = Battle()
fight.spawn(chevalier)
fight.spawn(slime)
fight.orderTurn()

j = fight.getLogSimulateFight()
print('\n'.join(j))


# FIXME: infinit loop at death.
