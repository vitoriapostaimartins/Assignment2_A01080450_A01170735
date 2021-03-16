from enum import Enum


class Inventory:
    def __init__(self):
        self._items = []

    def add_to_inventory(self, item):
        self._items.append(item)

    def check(self, orders):
        items_product_ids = [item._product_id for item in self._items]
        items_to_order = []
        for order in orders:
            if order._product_id not in items_product_ids:
                items_to_order.append(order)
        return items_to_order

class StockEnum(Enum):
    pass
