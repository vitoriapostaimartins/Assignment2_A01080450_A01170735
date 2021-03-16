import abc


class ItemFactory(abc.ABC):
    def __init__(self, **item_attributes):
        self._item_attributes = item_attributes

    @abc.abstractmethod
    def make_toy(self):
        pass

    @abc.abstractmethod
    def make_stuffed_animal(self):
        pass

    @abc.abstractmethod
    def make_candy(self):
        pass