import pandas as pd
from factory_mapping import FactoryMapping, ItemEnum
from items import InvalidDataError
from order import Order


class OrderProcessor:
    def __init__(self):
        self._factory_mapping = FactoryMapping()

    @property
    def factory_mapping(self):
        return self._factory_mapping

    def process_orders(self, order_name):
        orders = []
        df = pd.read_excel(order_name)
        df = df.where(pd.notnull(df), None)
        data = df.to_dict(orient='records')

        for row in data:
            order = self._get_order(row, orders)
            orders.append(order)

        return orders

    def _get_order(self, row, orders):
        # get factory
        holiday = row.get("holiday")
        factory_class = self.factory_mapping.get_factory(holiday)
        row.pop("holiday")

        # build order and add to orders list
        order = Order(**row, factory=factory_class)
        order_numbers = [item.order_number for item in orders]
        if order.error is None:
            try:
                self._check_duplicates(order, order_numbers)
            except InvalidDataError as e:
                pass
        return order

    def _check_duplicates(self, order, orders):
        if order.order_number in orders:
            raise InvalidDataError("Order Number cannot be a duplicate", order)


class ItemProcessor:

    def process_items(self, orders):
        items = []
        for order in orders:

            # Get the corresponding method to create the item
            try:
                dict_methods = self._get_factory_methods(order)
            except InvalidDataError as e:
                raise e

            if order.error is None:
                try:
                    items, order = self._make_items(order, dict_methods, items)
                except InvalidDataError as e:
                    raise e
        return items

    def _get_factory_methods(self, order):
        if order.factory is None:
            raise InvalidDataError("Order factory cannot be empty.", order)

        factory = order.factory

        # map each create method to the factory
        dict_methods = {
            ItemEnum.TOY.value: factory.make_toy,
            ItemEnum.STUFFED_ANIMAL.value: factory.make_stuffed_animal,
            ItemEnum.CANDY.value: factory.make_candy
        }

        return dict_methods

    def _make_items(self, order, dict_methods, items):
        # calls the factory create method based on the item type
        item_type = order.item

        if item_type is None:
            raise InvalidDataError("Order must have an item type", order)

        item_method = dict_methods.get(item_type)
        item_attributes = order.item_attributes

        # create 100 of each item
        for x in range(0, 100):
            try:
                item = item_method(**item_attributes)
                items.append(item)
            except InvalidDataError as e:
                order.error = e
                break
        return [items, order]
