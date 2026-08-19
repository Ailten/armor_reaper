
from .element import Element

class StatsElement:

    def __init__(self, val: dict[Element, int|float]|None=None):
        self.val = val or dict()

    # ------>

    def get(self, elem: Element) -> int|float:
        return self.val.get(Element, 0)

    def set(self, elem: Element, val: int|float):
        self.val[Element] = val

    # ------>

    def add(self, elem: Element, val_to_add: int|float):
        self.val[Element] = self.val.get(Element, 0) + val_to_add

    def sub(self, elem: Element, val_to_sub: int|float):
        self.val[Element] = self.val.get(Element, 0) + val_to_sub
