"""
Module that houses the HalloweenFactory class and classes for each item type made by the factory.
"""
from item_factory import ItemFactory
from items import Toy, StuffedAnimal, Candy, InvalidDataError


class HalloweenFactory(ItemFactory):
    """
    Class that represents a Factory for all Items related to the Halloween season.
    It is responsible for creating all types of Halloween Items offered by a Store.
    """
    def __init__(self, **item_attributes):
        """
        Initialize a Halloween Factory object with a dictionary of attributes of the Halloween Item it should yield.
        :param item_attributes: a dictionary
        """
        super().__init__(**item_attributes)

    @staticmethod
    def make_toy(**item_attributes) -> Toy:
        """
        Create a Toy type item with an Halloween theme.
        :param item_attributes: a dictionary
        :return: a RCSpider Toy
        """
        return RCSpider(item_attributes)

    @staticmethod
    def make_stuffed_animal(**item_attributes) -> StuffedAnimal:
        """
        Create a Stuffed Animal type item with an Halloween theme.
        :param item_attributes: a dictionary
        :return: a DancingSkeleton StuffedAnimal
        """
        return DancingSkeleton(item_attributes)

    @staticmethod
    def make_candy(**item_attributes) -> Candy:
        """
        Create a Candy type item with a Halloween theme.
        :param item_attributes: a dictionary
        :return: a PumpkinCaramelToffee Candy
        """
        return PumpkinCaramelToffee(item_attributes)


class RCSpider(Toy):
    """
    Class that represents a RCSpider Toy. It holds class attributes, as well as an initializer.
    """
    spider_types = ["Tarantula", "Wolf Spider"]
    speed_range = list(range(0, 100))
    jump_height = list(range(0, 100))

    attribute_errors = {
        "spider_type": [spider_types, f"Spider type can only be {' or '.join(spider_types)}."],
        "has_batteries": [["Y"], "RCSpider requires batteries. Property has_batteries should be 'Y'."],
        "speed": [speed_range, f"RCSpider must have speed between {speed_range[0]} and {speed_range[-1]}"],
        "jump_height": [jump_height, f"RCSpider must have jump height between {jump_height[0]} and {jump_height[-1]}"]
    }

    def __init__(self, item_attributes):
        """
        Initialize a RCSpider that glows with batteries, speed, jump height, and spider type.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, RCSpider.attribute_errors.items())
        except InvalidDataError as e:
            raise e

        self._spider_type = item_attributes.get("spider_type")
        self._has_batteries = item_attributes.get("has_batteries")
        self._speed = item_attributes.get("speed")
        self._has_glow = item_attributes.get("has_glow")
        super().__init__(**item_attributes)


class DancingSkeleton(StuffedAnimal):
    """
    Class that represents an DancingSkeleton Stuffed Animal. It holds class attributes, as well as an initializer.
    """
    attribute_errors = {
        "has_glow": [["Y"], "Dancing Skeletons have to glow in the dark. Property has_glow should be 'Y'."],
        "fabric": [["Acrylic"], "Dancing Skeletons must be made of Acrylic."],
        "stuffing": [["Polyester Fibrefill"], "Dancing Skeletons must be stuffed with Polyester Fibrefill."]
    }

    def __init__(self, item_attributes):
        """
        Initialize an DancingSkeleton that glows in the dark.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, DancingSkeleton.attribute_errors.items())
        except InvalidDataError as e:
            raise e

        self._has_glow = item_attributes.get("has_glow")

        super().__init__(**item_attributes)


class PumpkinCaramelToffee(Candy):
    """
    Class that represents a Pumpkin Caramel Toffee candy, that can come in different varieties and may contain lactose and nuts.
    """
    varieties = ["Sea Salt", "Regular"]

    attribute_errors = {
        "variety": [varieties, f"Variety must be {' or '.join(varieties)}."],
        "has_nuts": [["Y"], "Pumpkin Caramel Toffee may contain traces of nuts. Property has_nuts should be 'Y'."],
        "has_lactose": [["Y"], "Pumpkin Caramel Toffee is not lactose free. Property has_lactose should be 'Y'."]
    }

    def __init__(self, item_attributes):
        """
        Initialize a PumpkinCaramelToffee with a variety type (Sea Salt or Regular).
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, PumpkinCaramelToffee.attribute_errors.items())
        except InvalidDataError as e:
            raise e
        self._variety = item_attributes.get("variety")
        super().__init__(**item_attributes)
