"""
Module that holds the system's processors: OrderProcessor and ItemProcessor.
"""
import pandas as pd
from factory_mapping import FactoryMapping, ItemEnum
from items import InvalidDataError
from order import Order


class OrderProcessor:
    """
    Class that represents a processor for Order objects. it is responsible for reading the information of an Excel file
    and generating Order objects if appropriate.
    """

    def __init__(self):
        """
        Initialize an OrderProcessor object with a FactoryMapping object to access the Factory objects as necessary.
        """
        self._factory_mapping = FactoryMapping()

    @property
    def factory_mapping(self):
        """
        Get the FactoryMapping object that this OrderProcessor holds.
        :return:
        """
        return self._factory_mapping

    def process_orders(self, order_name):
        """
        Process the orders that an Excel file holds.
        :param order_name: a string
        :return: a list of objects of type Order
        """
        orders = []
        df = pd.read_excel(order_name)
        df = df.where(pd.notnull(df), None)
        data = df.to_dict(orient='records')

        for row in data:
            order = self._get_order(row, orders)
            orders.append(order)

        return orders

    def _get_order(self, row, orders):
        """
        Extract attributes from a row in an Excel file and create a new Order.
        :param row: a dictionary
        :param orders: a list of Orders
        :return: an Order object
        """

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
            except InvalidDataError:
                pass
        return order

    def _check_duplicates(self, order, orders):
        """
        Check if the order number for an order has already been used for another order.
        Throw an error for duplicate order numbers.
        :param order: an Order
        :param orders: a list
        """
        if order.order_number in orders:
            raise InvalidDataError("Order Number cannot be a duplicate", order)


class ItemProcessor:
    """
    Class that is responsible for processing the items to order in a store.
    """

    def process_items(self, orders):
        """
        Process the items to be ordered from a list of orders passed in.
        Return the list of items created.
        :param orders: a list
        :return: a list
        """
        items = []

        # Loop through each order and create the specified item
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
        """
        Map each value in ItemEnum to a factory create method based on the factory
        obtained from the order. Return the create methods as a dictionary.
        :param order: an Order
        :return: a dictionary
        """
        if order.factory is None:
            raise InvalidDataError("Order holiday is invalid.", order)

        factory = order.factory

        # map each create method to the factory
        dict_methods = {
            ItemEnum.TOY.value: factory.make_toy,
            ItemEnum.STUFFED_ANIMAL.value: factory.make_stuffed_animal,
            ItemEnum.CANDY.value: factory.make_candy
        }

        return dict_methods

    def _make_items(self, order, dict_methods, items):
        """
        Create a quantity of 100 for the specified item type.
        :param order: an Order
        :param dict_methods: a dictionary
        :param items: a list
        :return: a list
        """
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
