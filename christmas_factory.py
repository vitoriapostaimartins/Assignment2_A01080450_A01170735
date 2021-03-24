"""
Module that houses the ChristmasFactory class and classes for each item type made by the factory
"""
from item_factory import ItemFactory
from items import StuffedAnimal, Candy, Toy, InvalidDataError


class ChristmasFactory(ItemFactory):
    """
    Class that represents a Factory for all Items related to the Christmas season.
    It is responsible for creating all types of Christmas Items offered by a Store.
    """
    def __init__(self, **item_attributes):
        """
        Initialize a Christmas Factory object with a dictionary of attributes of the Christmas Item it should yield.
        :param item_attributes: a dictionary
        """
        super().__init__(**item_attributes)

    @staticmethod
    def make_toy(**item_attributes) -> Toy:
        """
        Create a Toy type item with a Christmas theme.
        :param item_attributes: a dictionary
        :return: a SantasWorkshop Toy
        """
        return SantasWorkshop(item_attributes)

    @staticmethod
    def make_stuffed_animal(**item_attributes) -> StuffedAnimal:
        """
        Create a Stuffed Animal type item with a Christmas theme.
        :param item_attributes: a dictionary
        :return: a Reindeer StuffedAnimal
        """
        return Reindeer(item_attributes)

    @staticmethod
    def make_candy(**item_attributes) -> Candy:
        """
        Create a Candy type item with a Christmas theme.
        :param item_attributes: a dictionary
        :return: a CandyCane Candy
        """
        return CandyCane(item_attributes)


# santa's workshop
class SantasWorkshop(Toy):
    """
    Class that represents an Santa's Workshop Toy. It holds class attributes, as well as an initializer.
    """
    num_rooms = list(range(0, 100))

    attribute_errors = {
        "has_batteries": [["N"], "Santa's workshop doesn't have batteries. Property has_batteries should be 'N'."],
        "num_rooms": [num_rooms, f"Number of rooms must be between {num_rooms[0]} and {num_rooms[-1]}"]
    }

    def __init__(self, item_attributes):
        """
        Initialize a SantasWorkshop toy with specified dimensions and number of rooms.
        :param item_attributes: a dictionary
        """
        try:
            self._check_attributes(item_attributes)
        except (ValueError, InvalidDataError) as e:
            raise e

        self._dimensions = item_attributes.get("dimensions")
        self._num_rooms = item_attributes.get("num_rooms")

        super().__init__(**item_attributes)

    def _check_attributes(self, item_attributes):
        """
        Validate the item attributes before instantiating the SantasWorkshop object.
        Raise an InvalidDataError for any invalid values encountered.
        :param item_attributes: a dictionary
        """
        try:
            item_attributes['dimensions'] = list(map(int, item_attributes.get("dimensions").split(",")))
        except ValueError:
            raise InvalidDataError("Dimensions have to be non-zero positive numbers")

        try:
            super().check_attributes(item_attributes, SantasWorkshop.attribute_errors.items())
        except InvalidDataError as e:
            raise e

        for measurement in item_attributes.get("dimensions"):
            if measurement <= 0:
                raise InvalidDataError("Dimensions have to be non-zero positive numbers")

class Reindeer(StuffedAnimal):
    """
    Class that represents a reindeer stuffed animal that should have
    cotton fabric, wool stuffing, and a glow-in-the-dark nose.
    """
    attribute_errors = {
        "fabric": [["Cotton"], "Reindeer have to be made out of Cotton."],
        "stuffing": [["Wool"], "Reindeer have to be stuffed with Wool."],
        "has_glow": [["Y"], "Reindeer have to be have a glow in the dark nose. Property has_glow should be 'Y'."]
    }

    def __init__(self, item_attributes):
        """
        Initialize a Reindeer with fabric, stuffing, and glow-in-the-dark nose.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, Reindeer.attribute_errors.items())
        except InvalidDataError as e:
            raise e

        self._has_glow = item_attributes.get("has_glow")

        super().__init__(**item_attributes)


class CandyCane(Candy):
    """
    Class that represents a candy cane, that can have colours Red or Green and
    is lactose and nut-free.
    """
    colours = ["Red", "Green"]

    attribute_errors = {
        "colour": [colours, f"Colour can only be {' or '.join(colours)}"],
        "has_nuts": [["N"], "Candy cane does not contain nuts. Property has_nuts should be 'N'."],
        "has_lactose": [["N"], "Candy cane is lactose free. Property has_lactose should be 'N'."]
    }

    def __init__(self, item_attributes):
        """
        Initialize a CandyCane with a colour that is either red or green.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, CandyCane.attribute_errors.items())
        except InvalidDataError as e:
            raise e

        self._colour = item_attributes.get('colour')

        super().__init__(**item_attributes)
