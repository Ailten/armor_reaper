
from ..character import Character

from ..spells.bulletWater import BulletWater

class Slime(Character):

    def __init__(self):
        super().__init__({
            'name': 'Slime',
            'lvl': 1,
            'xp': 6,

            'hp': 32,
            'mp': 6,
            'sp': 10,

            'is_player': False
        })

        self.spells.append( BulletWater() )


