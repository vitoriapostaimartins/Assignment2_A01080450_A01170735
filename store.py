"""
Module that contains the Store class and DailyTransactionReport class.
"""
import datetime
from inventory import Inventory
from items import InvalidDataError
from processors import OrderProcessor, ItemProcessor


class Store:
    """
    Class that represents a store with an inventory. The can take orders or
    place more orders for items not available in its inventory.
    """
    NO_ITEMS = 100

    def __init__(self):
        """
        Initialize a Store object with an empty list of Orders and an empty Inventory.
        """
        self._current_orders = []
        self._order_files = []
        self._inventory = Inventory()

    @property
    def order_files(self):
        """
        Get the lists of orders made from each excel file processed wrapped in a list.
        :return: list of lists of Orders
        """
        return self._order_files

    @property
    def current_orders(self):
        """
        Get the list of orders that are currently being processes from this Store.
        :return: a list
        """
        return self._current_orders

    @current_orders.setter
    def current_orders(self, value):
        """
        Set the list of orders that are currently being processed in this Store.
        :param value: a list
        """
        self._current_orders = value

    @property
    def inventory(self):
        """
        Get the Inventory from this Store.
        :return: an Inventory object
        """
        return self._inventory

    def _add_to_inventory(self, items):
        """
        Add a list of items to this Store's Inventory.
        :param items: a list of Items
        """
        self.inventory.add_to_inventory(items)

    def process_orders(self, order_name):
        """
        Process orders excel file to get Order objects.
        :param order_name: a string
        """
        order_processor = OrderProcessor()
        item_processor = ItemProcessor()

        # Process orders from excel file

        self.current_orders = (order_processor.process_orders(order_name))
        self.order_files.append(self.current_orders)

        # Check inventory for order quantities
        while True:

            # Check if there are items to order
            items_to_order = self.inventory.check_inventory(self.current_orders)

            # Process the items to order, adding the created items to the inventory
            try:
                processed_items = item_processor.process_items(items_to_order)
            except InvalidDataError:
                continue
            self._add_to_inventory(processed_items)

            # After ordering all items, break
            if not items_to_order:
                break

        self._remove_from_inventory()

    def _remove_from_inventory(self):
        """
        Remove orders that have enough quantity in the inventory.
        """
        for order in self.current_orders:
            quantity = order.item_attributes.get('quantity')
            self.inventory.remove_from_inventory(order.product_id, quantity)

    def check_inventory(self):
        """
        Check this Store's Inventory stock.
        """
        self.inventory.check_stock()


class DailyTransactionReport:
    """
    Class that represents the daily transaction report for a store.
    """

    @staticmethod
    def create_report(orders_list):
        """
        Create daily transaction report and write it to a new file and indicate the time of exiting the system in the
         file name.
        :param orders_list:  a list of lists of Orders [[]]
        :return: a string
        """

        # get the current time
        file_time = datetime.datetime.now()
        year, month, day, hour, minute = map(str, file_time.strftime("%y %m %d %H %M").split())

        # set the properly-formatted file name
        file_name = f"DTR_{day}{month}{year}_{hour}{minute}.txt"

        with open(file_name, mode="a", encoding="utf-8") as text_file:
            data = "HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT) \n" \
                   f"{file_time.strftime('%d-%m-%Y %H:%M')} \n"

            # For each list of orders in orders list, get the transaction details
            order_data = ""
            for orders in orders_list:
                order_data += DailyTransactionReport.get_order_details(orders)

            data += order_data
            text_file.write(data)

        return file_name

    @staticmethod
    def get_order_details(orders):
        """
        Get the details for each order and add them as a line to a multi-line string.
        :param orders: a list
        :return: a string
        """

        # Get the details for each order in the orders list
        data = "-"*30 + "\n\n"
        for order in orders:
            order_no = order.order_number
            order_item = order.item
            order_product_id = order.item_attributes.get("product_id")
            order_name = order.name
            order_quantity = order.item_attributes.get("quantity")

            # If the order has any invalid data, append the error message to the details
            if order.error:
                data += f"Order {order_no}, Could not process order data was corrupted, {order.error}\n"
            else:
                data += f"Order {order_no}, Item {order_item}, Product ID {order_product_id}, Name \"{order_name}\", " \
                        f"Quantity {order_quantity}\n "

        return data + "\n"
