from item_factory import ItemFactory
from items import Toy, StuffedAnimal, Candy, InvalidDataError


class EasterFactory(ItemFactory):
    def __init__(self, **item_attributes):
        super().__init__(**item_attributes)

    @staticmethod
    def make_toy(**item_attributes) -> Toy:
        return RobotBunny(item_attributes)

    @staticmethod
    def make_stuffed_animal(**item_attributes) -> StuffedAnimal:
        return EasterBunny(item_attributes)

    @staticmethod
    def make_candy(**item_attributes) -> Candy:
        return CremeEggs(item_attributes)


class RobotBunny(Toy):

    colours = ["Orange", "Blue", "Pink"]

    def __init__(self, item_attributes):
        if item_attributes.get('colour') not in RobotBunny.colours:
            raise InvalidDataError(f"Colour can only be {' or '.join(RobotBunny.colours)}")
        super().__init__(**item_attributes)


class EasterBunny(StuffedAnimal):
    colours = ["White", "Grey", "Blue"]
    def __init__(self, item_attributes):
        if item_attributes.get("colour") not in EasterBunny.colours:
            raise InvalidDataError(f"Easter Bunnies have to come in the following colours: {' or '.join(EasterBunny.colours)}")
        if item_attributes.get("fabric") != "Linen":
            raise InvalidDataError("Easter Bunnies have to be made out of Linen")
        if item_attributes.get("stuffing") != "Polyester Fibrefill":
            raise InvalidDataError(f"Easter Bunnies have to be stuffed with Polyester Fibrefill")
        super().__init__(**item_attributes)


class CremeEggs(Candy):
    def __init__(self, item_attributes):
        super().__init__(**item_attributes)
