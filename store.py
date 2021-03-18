import datetime
import time

from inventory import Inventory
from processors import OrderProcessor, ItemProcessor


class Store:
    NO_ITEMS = 100

    def __init__(self):
        self._orders = []
        self._inventory = Inventory()

    @property
    def orders(self):
        return self._orders

    @property
    def inventory(self):
        return self._inventory

    def add_to_inventory(self, items):
        self._inventory.add_to_inventory(items)

    def process_orders(self, order_name):
        """
        Process orders excel file to get order objects.
        :param order_name:
        :return:
        """

        # Process orders from excel file
        order_processor = OrderProcessor()
        self._orders = order_processor.process_orders(order_name)

        # Check inventory for order quantities
        print("before: \n", self._inventory)

        while True:
            # Check if there are items to order
            items_to_order = self._inventory.check(self._orders)
            processed_items = ItemProcessor.process_items(items_to_order)
            self.add_to_inventory(processed_items)

            # After ordering all items, break
            if not items_to_order:
                break

        # For orders that have enough quantity in the inventory, remove from inventory
        for order in self._orders:
            self._inventory.remove_from_inventory(order.product_id, order.item_attributes.get('quantity'))
        print("after: \n", self._inventory)

    def check_inventory(self):
        self.inventory.check_stock()


class DailyTransactionReport:
    @staticmethod
    def create_report(orders):
        # get the current time
        file_time = datetime.datetime.now()
        year, month, day, hour, minute = map(str, file_time.strftime("%y %m %d %H %M").split())
        file_name = f"DTR_{day}{month}{year}_{hour}{minute}.txt"

        with open(file_name, mode="w", encoding="utf-8") as text_file:
            data = "HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT) \n" \
                   f"{file_time.strftime('%d-%m-%Y %H:%M')} \n"

            for order in orders:
                order_no = order.order_number

                order_item = order.item
                order_product_id = order.item_attributes.get("product_id")
                order_name = order.name
                order_quantity = order.item_attributes.get("quantity")
                if order.error:
                    data += f"Order {order_no}, Could not process order data was corrupted, {order.error}\n"
                else:
                    data += f"Order {order_no}, Item {order_item}, Product ID {order_product_id}, Name \"{order_name}\", Quantity {order_quantity}\n"

            text_file.write(data)
