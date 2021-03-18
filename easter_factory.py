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
    num_sound = list(range[0, 100])

    attributes = {
        "colour": [colours, f"Colour can only be {' or '.join(colours)}."],
        "has_batteries": [["Y"], f"Robot Bunny requires batteries. Property has_batteries should be 'Y'."],
        "num_sound": [num_sound, f"Robot Bunny must have sound effects between {num_sound[0]} and {num_sound[-1]}"]
    }

    def __init__(self, item_attributes):
        try:
            super().check_attributes(item_attributes, RobotBunny.attributes.items())
        except InvalidDataError as e:
            raise e
        self._num_sound = item_attributes.get("num_sound")
        self._colour = item_attributes.get("colour")
        super().__init__(**item_attributes)


class EasterBunny(StuffedAnimal):
    colours = ["White", "Grey", "Pink", "Blue"]

    attributes = {
        "colour": [colours, f"Easter Bunnies have to come in the following colours: {' or '.join(colours)}."],
        "fabric": [["Linen"], "Easter Bunny must be made of Linen."],
        "stuffing": [["Polyester Fibrefill"], "Easter Bunny must be stuffed with Polyester Fibrefill."]
    }

    def __init__(self, item_attributes):
        try:
            super().check_attributes(item_attributes, EasterBunny.attributes.items())
        except InvalidDataError as e:
            raise e

        self._colour = item_attributes.get("colour")
        super().__init__(**item_attributes)


class CremeEggs(Candy):

    pack_size = list(range(1, 100))

    attributes = {
        "has_nuts": [["Y"], "Creme eggs may contain traces of nuts. Property has_nuts should be 'Y'."],
        "has_lactose": [["Y"], "Creme eggs are not lactose free. Property has_lactose should be 'Y'."],
        "pack_size": [pack_size, f"Creme eggs must come in a pack size between {pack_size[0]} and {pack_size[1]}"]
    }

    def __init__(self, item_attributes):
        try:
            super().check_attributes(item_attributes, CremeEggs.attributes.items())
        except InvalidDataError as e:
            raise e
        self._pack_size = item_attributes.get("pack_size")
        super().__init__(**item_attributes)
