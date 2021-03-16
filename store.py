from inventory import Inventory
from order_processor import OrderProcessor, ItemProcessor


class Store:
    def __init__(self):
        self._orders = []
        self._inventory = Inventory()
        pass

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
        items_to_order = self._inventory.check(self._orders)
        ItemProcessor.process_items(items_to_order)



class DailyTransactionReport:
    def __init__(self):
        pass
