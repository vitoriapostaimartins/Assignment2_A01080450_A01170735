from item_factory import ItemFactory
from items import Toy, StuffedAnimal, Candy


class EasterFactory(ItemFactory):
    def __init__(self, **item_attributes):
        super().__init__(**item_attributes)

    def make_toy(self, **item_attributes) -> Toy:
        return RobotBunny(item_attributes)

    def make_stuffed_animal(self, **item_attributes) -> StuffedAnimal:
        return EasterBunny(item_attributes)

    def make_candy(self, **item_attributes) -> Candy:
        return CremeEggs(item_attributes)


class RobotBunny(Toy):
    def __init__(self, item_attributes):
        super().__init__(**item_attributes)


class EasterBunny(StuffedAnimal):
    def __init__(self, item_attributes):
        super().__init__(**item_attributes)


class CremeEggs(Candy):
    def __init__(self, item_attributes):
        super().__init__(**item_attributes)
