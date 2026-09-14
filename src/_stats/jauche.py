
class Jauche:
    
    def __init__(self, val: int):
        self.val = val
        self.max_val = val

    # ------>

    def add(self, val_to_add: int):
        self.val += val_to_add
        self.val = min(self.val, self.max_val)

    def sub(self, val_to_sub: int):
        self.val -= val_to_sub
        self.val = max(self.val, 0)

    # ------>

    def resetVal(self, val: int, max_val: int):
        self.val = val
        self.max_val = max_val

    
