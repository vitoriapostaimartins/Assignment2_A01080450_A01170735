# orderprocessor
from enum import auto, Enum
import pandas as pd
import openpyxl
import collections as co

from christmas_factory import ChristmasFactory
from easter_factory import EasterFactory
from halloween_factory import HalloweenFactory
from item_factory import ItemFactory
from order import Order


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
    def __init__(self):
        pass


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


# holidayenum
class HolidayEnum(Enum):
    CHRISTMAS = 'Christmas'
    HALLOWEEN = 'Halloween'
    EASTER = 'Easter'
