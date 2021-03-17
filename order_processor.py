# orderprocessor
from enum import Enum
import pandas as pd

from christmas_factory import ChristmasFactory
from easter_factory import EasterFactory
from halloween_factory import HalloweenFactory
from item_factory import ItemFactory
from items import InvalidDataError
from order import Order


# holidayenum
class HolidayEnum(Enum):
    CHRISTMAS = 'Christmas'
    HALLOWEEN = 'Halloween'
    EASTER = 'Easter'


class ItemEnum(Enum):
    TOY = "Toy"
    STUFFED_ANIMAL = "StuffedAnimal"
    CANDY = "Candy"


class OrderProcessor:
    def __init__(self):
        self._factory_mapping = FactoryMapping()

    def process_orders(self, order_name):
        orders = []
        df = pd.read_excel(order_name)
        df = df.where(pd.notnull(df), None)
        data = df.to_dict(orient='records')

        for row in data:
            # get factory
            holiday = row.get("holiday")
            factory_class = self._factory_mapping.get_factory(holiday)
            row.pop("holiday")

            # build order and add to orders list
            order = Order(**row, factory=factory_class)
            orders.append(order)

        return orders

    @staticmethod
    def read_columns(data):
        has_batteries = pd.DataFrame(data, columns=['has_batteries'])
        print(has_batteries)


# itemprocessor
class ItemProcessor:

    @staticmethod
    def process_items(orders):
        items = []
        for order in orders:
            factory = order.factory

            dict_methods = {
                ItemEnum.TOY.value: factory.make_toy,
                ItemEnum.STUFFED_ANIMAL.value: factory.make_stuffed_animal,
                ItemEnum.CANDY.value: factory.make_candy
            }

            item_type = order.item
            item_method = dict_methods.get(item_type)
            item_attributes = order.item_attributes

            for x in range(0, 100):
                try:
                    item = item_method(**item_attributes)
                    items.append(item)
                except InvalidDataError as e:
                    order.error = e
                    break

        return items


# factory mapping
class FactoryMapping:
    def __init__(self):
        self._factory_mapper = {
            HolidayEnum.CHRISTMAS.value: ChristmasFactory(),
            HolidayEnum.HALLOWEEN.value: HalloweenFactory(),
            HolidayEnum.EASTER.value: EasterFactory()
        }

    def get_factory(self, item_type) -> ItemFactory:
        factory_class = self._factory_mapper.get(item_type)
        return factory_class
