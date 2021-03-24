"""
Module that houses the ItemFactory abstract base class.
"""
import abc
from items import Toy, StuffedAnimal, Candy


class ItemFactory(abc.ABC):
    """
    Class that represents an Item Factory. It is responsible for creating all types of Items offered by a Store.
    """
    def __init__(self, **item_attributes):
        """
        Initialize a ItemFactory object with a dictionary of attributes of the Item it should yield.
        :param item_attributes: a dictionary
        """
        self._item_attributes = item_attributes

    @staticmethod
    @abc.abstractmethod
    def make_toy() -> Toy:
        """
        Create a Toy type item.
        :return: a Toy
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def make_stuffed_animal() -> StuffedAnimal:
        """
        Create a StuffedAnimal type item.
        :return: a StuffedAnimal
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def make_candy() -> Candy:
        """
        Create a Candy type item.
        :return: a Candy
        """
        pass
