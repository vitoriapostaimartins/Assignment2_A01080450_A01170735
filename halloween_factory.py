from item_factory import ItemFactory
from items import Toy, StuffedAnimal, Candy


class HalloweenFactory(ItemFactory):
    def __init__(self, **item_attributes):
        super().__init__(**item_attributes)

    def make_toy(self, **item_attributes) -> Toy:
        return RCSpider(item_attributes)

    def make_stuffed_animal(self, **item_attributes) -> StuffedAnimal:
        return DancingSkeleton(item_attributes)

    def make_candy(self, **item_attributes) -> Candy:
        return PumpkinCaramelToffee(item_attributes)


class RCSpider(Toy):
    def __init__(self, item_attribute):
        super().__init__(**item_attribute)


class DancingSkeleton(StuffedAnimal):
    def __init__(self, item_attribute):
        super().__init__(**item_attribute)


class PumpkinCaramelToffee(Candy):
    def __init__(self, item_attribute):
        super().__init__(**item_attribute)
