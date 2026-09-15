
class Jauche:
    
    def __init__(self, val: int):
        self.val = val
        self.max_val = val

    # ------>

    def add(self, val_to_add: int) -> int:
        value_apply = min(val_to_add, self.max_val-self.val)
        self.val += value_apply
        return value_apply

    def sub(self, val_to_sub: int) -> int:
        value_apply = min(val_to_sub, self.val)
        self.val -= value_apply
        return value_apply

    # ------>

    def resetVal(self, val: int, max_val: int):
        self.val = val
        self.max_val = max_val

    
