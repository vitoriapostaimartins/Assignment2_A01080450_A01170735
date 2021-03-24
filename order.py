"""
Module that contains Order class and methods to validate the order.
"""

from items import InvalidDataError


class Order:
    """
    Class that represents an Order made to a store.
    """

    def __init__(self, order_number=None, item=None, **kwargs):
        """
        Initialize an Order object.
        :param order_number: an int
        :param item: a String
        :param kwargs: a dictionary
        """
        self._error = None
        try:
            self._check_order(order_number, item, **kwargs)
        except InvalidDataError:
            pass
        self._order_number = order_number
        self._item = item
        self._name = kwargs.get("name")
        self._product_id = kwargs.get("product_id")
        self._factory = kwargs.get("factory")
        self._item_attributes = kwargs

    def _check_order_number(self, order_number):
        """
        Check if the order_number passed in is valid.Throw an error
        for invalid values.
        :param order_number: an int
        """
        try:
            if order_number <= 0:
                raise InvalidDataError("Order number has to be a non-zero positive number.", self)
        except (ValueError, TypeError):
            raise InvalidDataError("Order number has to be a non-zero positive number.", self)

    def _check_order_quantity(self, **kwargs):
        """
        Check if the order quantity is valid (i.e. greater than 0). Throw an error
        for invalid values.
        :param kwargs: a dictionary
        """
        try:
            if kwargs.get("quantity") <= 0:
                raise InvalidDataError("Order quantity has to be a non-zero positive number.", self)
        except (ValueError, TypeError):
            raise InvalidDataError("Order quantity has to be a non-zero positive number.", self)

    def _check_order_details(self, **order_attributes):
        """
        Check if the order name, product_id, and description are valid. Throw an error
        for invalid values.
        :param order_attributes: a dictionary
        """
        order_attributes_items = {
            "name": "Order name cannot be empty.",
            "product_id": "Product ID cannot be empty.",
            "description": "Product description cannot be empty."
        }

        # Loop through each attribute, throwing an error if invalid
        for attribute, error in order_attributes_items.items():
            if order_attributes.get(attribute) is None or order_attributes.get(attribute).strip() == '':
                raise InvalidDataError(error, self)

    def _check_order(self, order_number, item, **kwargs):
        """
        Perform validation on an order, based on the attributes passed in.
        :param order_number: an int
        :param item: a string
        :param kwargs: a dictionary
        """

        # Check the order quantity
        self._check_order_quantity(**kwargs)

        # Check the order number
        self._check_order_number(order_number)

        if item is None or item.strip() == '':
            raise InvalidDataError("Order must have an item.", self)

        # Check name, product_id, and description
        self._check_order_details(**kwargs)

    @property
    def order_number(self):
        """
        Get the order number.
        :return: an int
        """
        return self._order_number

    @property
    def error(self):
        """
        Get the value of the Order's error if there is one.
        :return: a String if there is an error, None otherwise
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Store the value of the Order's error if one occurs.
        :param error: a string
        """
        self._error = error

    @property
    def item(self):
        """
        Get the item type of an Order.
        :return: a string
        """
        return self._item

    @property
    def name(self):
        """
        Get the item name of an Order.
        :return: a string
        """
        return self._name

    @property
    def product_id(self):
        """
        Get the product ID of an Order.
        :return: a string
        """
        return self._product_id

    @property
    def factory(self):
        """
        Get the factory for the item in the Order.
        :return: an ItemFactory
        """
        return self._factory

    @property
    def item_attributes(self):
        """
        Get the attributes for the item in an Order
        :return: a dictionary
        """
        return self._item_attributes
