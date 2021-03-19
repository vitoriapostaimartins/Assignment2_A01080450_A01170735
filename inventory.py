from enum import Enum


class Inventory:
    def __init__(self):
        self._items = {}

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value


    def add_to_inventory(self, items):
        for item in items:
            product_id = item.product_id
            if self.items.get(product_id):
                self.items[product_id] += 1
            else:
                self.items[product_id] = 1

    def remove_from_inventory(self, product_id, quantity):
        # check inventory for product id
        if self.items.get(product_id):
            self.items[product_id] -= quantity

    def check(self, orders):  # TODO test
        items_product_ids = [product_id for product_id in self.items.keys()]
        items_to_order = []
        for order in orders:
            # check if item is not in inventory OR inventory doesn't have enough of item
            if self.validate_order(order, items_product_ids) and order.error is None:
                items_to_order.append(order)
        return items_to_order

    def validate_order(self, order, items_product_ids):
        """
        Checks
        :param items_product_ids:
        :param order:
        :return:
        """
        return order.product_id not in items_product_ids \
            or order.item_attributes['quantity'] > self.items.get(order.product_id)

    def check_stock(self):
        for key, value in self.items.items():
            stock = ""
            if value == 0:
                stock = "Out of stock"
            elif value < 3:
                stock = "Very low"
            elif value < 10:
                stock = "Low"
            elif value >= 10:
                stock = "In Stock"
            print(f"{key} has an inventory of {value} and its status is {stock}")

    def __str__(self):
        return_str = ""
        for key, item in self.items.items():
            return_str += f"{key} : {item} \n"
        return return_str
