from .status_effect import StatusEffect

class StatusEffectCollection:
    
    def __init__(self):
        self.status_effects = []

    # ------>

    def add(self, status_effect_to_add: StatusEffect):
        self.status_effects.append(status_effect_to_add)

    def sub(self, status_effect_to_sub: StatusEffect):
        self.status_effects.remove(status_effect_to_sub)

    # ------>

    