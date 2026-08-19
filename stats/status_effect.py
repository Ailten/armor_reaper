
from .battle import Battle

class StatusEffect:
    id_count: int = 0

    def __init__(self, battle: Battle):
        self.id = Battle.getNextIndexStatusEffect()