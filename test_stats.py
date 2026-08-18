

# Test.


from stats import *


chevalier = Character()
chevalier.name = 'chevalier'

slime = Character()
slime.name = 'slime'
slime.is_team_left = False


fight = Battle()
fight.spawn(chevalier)
fight.spawn(slime)
fight.orderTurn()

j = fight.getLogSimulateFight()
print('\n'.join(j))
