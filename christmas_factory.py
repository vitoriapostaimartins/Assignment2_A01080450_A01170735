from item_factory import ItemFactory
from items import StuffedAnimal, Candy, Toy


class ChristmasFactory(ItemFactory):
    def __init__(self, **item_attributes):
        super().__init__(**item_attributes)

    def make_toy(self, **item_attributes) -> Toy:
        return SantasWorkshop(item_attributes)

    def make_stuffed_animal(self, **item_attributes) -> StuffedAnimal:
        return Reindeer(item_attributes)

    def make_candy(self, **item_attributes) -> Candy:
        return CandyCane(item_attributes)


# santa's workshop
class SantasWorkshop(Toy):
    def __init__(self, item_attribute):
        super().__init__(**item_attribute)


# reindeer
class Reindeer(StuffedAnimal):
    def __init__(self, item_attribute):
        super().__init__(**item_attribute)


# candy canes
class CandyCane(Candy):
    def __init__(self, item_attributes):
        super().__init__(**item_attributes)
