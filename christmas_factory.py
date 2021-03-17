from item_factory import ItemFactory
from items import StuffedAnimal, Candy, Toy, InvalidDataError


class ChristmasFactory(ItemFactory):
    def __init__(self, **item_attributes):
        super().__init__(**item_attributes)

    @staticmethod
    def make_toy(**item_attributes) -> Toy:
        return SantasWorkshop(item_attributes)

    @staticmethod
    def make_stuffed_animal(**item_attributes) -> StuffedAnimal:
        return Reindeer(item_attributes)

    @staticmethod
    def make_candy(**item_attributes) -> Candy:
        return CandyCane(item_attributes)


# santa's workshop
class SantasWorkshop(Toy):
    def __init__(self, item_attribute):
        super().__init__(**item_attribute)


# reindeer
class Reindeer(StuffedAnimal):
    def __init__(self, item_attribute):
        if item_attribute.get("fabric") != "Cotton":
            raise InvalidDataError(f"Reindeer have to be made out of Cotton")
        if item_attribute.get("stuffing") != "Wool":
            raise InvalidDataError(f"Reindeer have to be stuffed with Wool")
        if item_attribute.get("has_glow") != "Y":
            raise InvalidDataError(f"Reindeer have to be have a glow in the dark nose")
        super().__init__(**item_attribute)


# candy canes
class CandyCane(Candy):
    colours = ["Red", "Green"]

    def __init__(self, item_attributes):
        if item_attributes.get('colour') not in CandyCane.colours:
            raise InvalidDataError(f"Colour can only be {' or '.join(CandyCane.colours)}")
        super().__init__(**item_attributes)
