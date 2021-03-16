from order_processor import OrderProcessor


class Store:
    def __init__(self):
        self._orders = []
        pass

    def process_orders(self, order_name):
        order_processor = OrderProcessor()
        self._orders = order_processor.process_orders(order_name)
        pass


class DailyTransactionReport:
    def __init__(self):
        pass
