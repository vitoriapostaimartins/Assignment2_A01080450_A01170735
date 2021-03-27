"""Module that contains Inventory class and its methods to add/remove items, checking the inventory, as well as its
properties. """


class Inventory:
    """
    Class that represents an Inventory for a Store.
    """

    def __init__(self):
        """
        Initialize an Inventory Object.
        """
        self._items = {}

    @property
    def items(self):
        """
        Get the items that are in this inventory.
        :return: a dictionary
        """
        return self._items

    @items.setter
    def items(self, value):
        """
        Set the items in this inventory.
        :param value: a dictionary
        """
        self._items = value

    def add_to_inventory(self, items):
        """
        Add items to this inventory.
        :param items: a list of Item objects
        """
        for item in items:
            product_id = item.product_id
            if self.items.get(product_id):
                self.items[product_id] += 1
            else:
                self.items[product_id] = 1

    def remove_from_inventory(self, product_id, quantity):
        """
        Remove a quantity of an item from this inventory by its product id.
        :param product_id: a string
        :param quantity: an int
        """
        if self.items.get(product_id):
            self.items[product_id] -= quantity

    def check_inventory(self, orders):
        """
        Check the items to order and add them to a list of items to be ordered if the
        item doesn't exist in the inventory, or the quantity in the inventory is not
        enough.
        :param orders: a list
        :return: a list
        """
        items_product_ids = [product_id for product_id in self.items.keys()]
        items_to_order = []
        for order in orders:
            # check if item is not in inventory OR inventory doesn't have enough of item
            if self.validate_order(order, items_product_ids) and order.error is None:
                items_to_order.append(order)
        return items_to_order

    def validate_order(self, order, items_product_ids):
        """
        Check whether the item to order already exists in the inventory
        or if the quantity to order is greater than the amount available
        in the inventory.
        :param items_product_ids: a string
        :param order: an Order
        :return: a boolean
        """
        return order.product_id not in items_product_ids \
            or order.item_attributes['quantity'] > self.items.get(order.product_id)

    def check_stock(self):
        """
        Check the current status of each item in the inventory, and
        print out the status indicator.
        """
        for product_id, quantity in self.items.items():
            stock = ""
            if quantity == 0:
                stock = "Out of stock"
            elif quantity < 3:
                stock = "Very low"
            elif quantity < 10:
                stock = "Low"
            elif quantity >= 10:
                stock = "In Stock"
            print(f"{product_id} has an inventory of {quantity} and its status is {stock}")

    def __str__(self):
        """
        Return each a string with the product id and item quantity.
        :return: a string
        """
        return_str = ""
        for product_id, quantity in self.items.items():
            return_str += f"{product_id} : {quantity} \n"
        return return_str
