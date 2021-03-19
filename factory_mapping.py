from enum import Enum
from christmas_factory import ChristmasFactory
from easter_factory import EasterFactory
from halloween_factory import HalloweenFactory
from item_factory import ItemFactory


class HolidayEnum(Enum):
    CHRISTMAS = 'Christmas'
    HALLOWEEN = 'Halloween'
    EASTER = 'Easter'


class ItemEnum(Enum):
    TOY = "Toy"
    STUFFED_ANIMAL = "StuffedAnimal"
    CANDY = "Candy"


class FactoryMapping:
    def __init__(self):
        self._factory_mapper = {
            HolidayEnum.CHRISTMAS.value: ChristmasFactory(),
            HolidayEnum.HALLOWEEN.value: HalloweenFactory(),
            HolidayEnum.EASTER.value: EasterFactory()
        }

    @property
    def factory_mapper(self):
        return self._factory_mapper

    def get_factory(self, item_type) -> ItemFactory:
        factory_class = self.factory_mapper.get(item_type)
        return factory_class
