"""
Module that holds the FactoryMapping class, HolidayEnum and ItemEnum.
"""
from enum import Enum
from christmas_factory import ChristmasFactory
from easter_factory import EasterFactory
from halloween_factory import HalloweenFactory
from item_factory import ItemFactory


class HolidayEnum(Enum):
    """
    Enum for each holiday type, that holds the holiday name as a string.
    """
    CHRISTMAS = 'Christmas'
    HALLOWEEN = 'Halloween'
    EASTER = 'Easter'


class ItemEnum(Enum):
    """
    Enum for each item type, that holds the item type as a string.
    """
    TOY = "Toy"
    STUFFED_ANIMAL = "StuffedAnimal"
    CANDY = "Candy"


class FactoryMapping:
    """
    Class that maps a factory to each value in the HolidayEnum.
    """
    def __init__(self):
        """
        Initialize a FactoryMapping with a factory_mapper dictionary, which
        has key-value pairs of the HolidayEnum value and corresponding factory.
        """
        self._factory_mapper = {
            HolidayEnum.CHRISTMAS.value: ChristmasFactory(),
            HolidayEnum.HALLOWEEN.value: HalloweenFactory(),
            HolidayEnum.EASTER.value: EasterFactory()
        }

    @property
    def factory_mapper(self):
        """
        Get the factory mapper dictionary that contains the available factories and the seasons that they are
        associated to.
        :return: a dictionary
        """
        return self._factory_mapper

    def get_factory(self, item_type) -> ItemFactory:
        """
        Get the appropriate factory from an item type.
        :param item_type: a string
        :return: a object of ItemFactory type
        """
        factory_class = self.factory_mapper.get(item_type)
        return factory_class
