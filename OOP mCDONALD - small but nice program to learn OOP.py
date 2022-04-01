from abc import ABC, abstractmethod
from typing import List

class Item(ABC):
    @abstractmethod
    def get_price(self):
        pass

class Cheesburger(Item):
    def __init__(self, **kwargs):
        pass
    def get_price(self):
        return 6.50


class McNuggets(Item):
    def __init__(self, nuggets: int):
        assert isinstance(nuggets,int), 'no chyba jest zle'
        assert nuggets>0, 'no jestszcze lepiej'
        self.nuggets = nuggets

    def get_price(self):
        return 2.00+0.50*self.nuggets


class BigMac(Item):
    def __init__(self):
        pass

    def get_price(self):
        return 7.00

class Order:
    def __init__(self, items: List[Item]):
        self.items = items

    def calc_price(self) -> float:
        return sum(item.get_price() for item in self.items)


if __name__ == '__main__':
    cheesbirger1 = Cheesburger(pickle = False)
    cheesbirger2 = Cheesburger()
    nuggats = McNuggets(9)
    bigmac = BigMac()

    order = Order([
        cheesbirger1,
        cheesbirger2,
        nuggats,
        bigmac
    ])

    print(order.calc_price())