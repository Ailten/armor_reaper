
from .element import Element

class StatsElement:

    def __init__(self, val: dict[Element, int|float]|None=None):
        self.val = val or dict()

    # ------>

    def get(self, elem: Element, default_val: int|None=None) -> int|float:
        return self.val.get(elem, default_val or 0)

    def set(self, elem: Element, val: int|float):
        self.val[elem] = val

    # ------>

    def add(self, elem: Element, val_to_add: int|float):
        self.val[elem] = self.val.get(elem, 0) + val_to_add

    def sub(self, elem: Element, val_to_sub: int|float):
        self.val[elem] = self.val.get(elem, 0) + val_to_sub

    # ------>

    def resetVal(self, val: dict[Element, int|float]|None=None):
        self.val = val or dict()

