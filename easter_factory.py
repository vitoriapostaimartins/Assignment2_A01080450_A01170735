"""
Module that houses the EasterFactory class and classes for each item type made by the factory.
"""
from item_factory import ItemFactory
from items import Toy, StuffedAnimal, Candy, InvalidDataError


class EasterFactory(ItemFactory):
    """
    Class that represents a Factory for all Items related to the Easter season.
    It is responsible for creating all types of Easter Items offered by a Store.
    """
    def __init__(self, **item_attributes):
        """
        Initialize a Easter Factory object with a dictionary of attributes of the Easter Item it should yield.
        :param item_attributes: a dictionary
        """
        super().__init__(**item_attributes)

    @staticmethod
    def make_toy(**item_attributes) -> Toy:
        """
        Create a Toy type item with an Easter theme.
        :param item_attributes: a dictionary
        :return: a RobotBunny Toy
        """
        return RobotBunny(item_attributes)

    @staticmethod
    def make_stuffed_animal(**item_attributes) -> StuffedAnimal:
        """
        Create a Stuffed Animal type item with an Easter theme.
        :param item_attributes: a dictionary
        :return: an EasterBunny StuffedAnimal
        """
        return EasterBunny(item_attributes)

    @staticmethod
    def make_candy(**item_attributes) -> Candy:
        """
        Create a Candy type item with an Easter theme.
        :param item_attributes: a dictionary
        :return: a CremeEggs Candy
        """
        return CremeEggs(item_attributes)


class RobotBunny(Toy):
    """
    Class that represents a RobotBunny Toy. It holds class attributes, as well as an initializer.
    """
    colours = ["Orange", "Blue", "Pink"]
    num_sound = list(range(0, 100))

    attribute_errors = {
        "colour": [colours, f"Colour can only be {' or '.join(colours)}."],
        "has_batteries": [["Y"], f"Robot Bunny requires batteries. Property has_batteries should be 'Y'."],
        "num_sound": [num_sound, f"Robot Bunny must have sound effects between {num_sound[0]} and {num_sound[-1]}"]
    }

    def __init__(self, item_attributes):
        """
        Initialize a RobotBunny with sounds, batteries, and a specified colour.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, RobotBunny.attribute_errors.items())
        except InvalidDataError as e:
            raise e
        self._num_sound = item_attributes.get("num_sound")
        self._colour = item_attributes.get("colour")
        super().__init__(**item_attributes)


class EasterBunny(StuffedAnimal):
    """
    Class that represents an EasterBunny Stuffed Animal. It holds class attributes, as well as an initializer.
    """
    colours = ["White", "Grey", "Pink", "Blue"]

    attribute_errors = {
        "colour": [colours, f"Easter Bunnies have to come in the following colours: {' or '.join(colours)}."],
        "fabric": [["Linen"], "Easter Bunny must be made of Linen."],
        "stuffing": [["Polyester Fibrefill"], "Easter Bunny must be stuffed with Polyester Fibrefill."]
    }

    def __init__(self, item_attributes):
        """
        Initialize an EasterBunny that has a specified colour.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, EasterBunny.attribute_errors.items())
        except InvalidDataError as e:
            raise e

        self._colour = item_attributes.get("colour")
        super().__init__(**item_attributes)


class CremeEggs(Candy):
    """
    Class that represents a Creme Egg candy, that can come in different pack sizes and may contain lactose and nuts.
    """

    pack_size = list(range(1, 100))

    attribute_errors = {
        "has_nuts": [["Y"], "Creme eggs may contain traces of nuts. Property has_nuts should be 'Y'."],
        "has_lactose": [["Y"], "Creme eggs are not lactose free. Property has_lactose should be 'Y'."],
        "pack_size": [pack_size, f"Creme eggs must come in a pack size between {pack_size[0]} and {pack_size[1]}"]
    }

    def __init__(self, item_attributes):
        """
        Initialize a CremeEgg with a pack size.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, CremeEggs.attribute_errors.items())
        except InvalidDataError as e:
            raise e
        self._pack_size = item_attributes.get("pack_size")
        super().__init__(**item_attributes)
