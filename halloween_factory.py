from item_factory import ItemFactory
from items import Toy, StuffedAnimal, Candy


class HalloweenFactory(ItemFactory):
    def __init__(self):
        super().__init__()
        pass


class RCSpider(Toy):
    def __init__(self):
        super().__init__()
        pass


class DancingSkeleton(StuffedAnimal):
    def __init__(self):
        super().__init__()
        pass


class PumpkinCaramelToffee(Candy):
    def __init__(self):
        super().__init__()
        pass
