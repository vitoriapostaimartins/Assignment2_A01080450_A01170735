from items import InvalidDataError


class Order:
    def __init__(self, order_number=None, item=None, **order_attributes):
        self._error = None
        try:
            self._check_order(order_number, item, **order_attributes)
        except InvalidDataError as e:
            pass
        self._order_number = order_number
        self._item = item
        self._name = order_attributes.get("name")
        self._product_id = order_attributes.get("product_id")
        self._factory = order_attributes.get("factory")
        self._item_attributes = order_attributes

    def _check_order(self, order_number, item, **order_attributes):
        try:
            if order_attributes.get("quantity") <= 0:
                raise InvalidDataError("Order quantity has to be a non-zero positive number.", self)
        except (ValueError, TypeError):
            raise InvalidDataError("Order quantity has to be a non-zero positive number.", self)

        try:
            if order_number <= 0:
                raise InvalidDataError("Order number has to be a non-zero positive number.", self)
        except (ValueError, TypeError):
            raise InvalidDataError("Order number has to be a non-zero positive number.", self)

        order_attributes_items = {
            "name": "Order name cannot be empty.",
            "product_id": "Product ID cannot be empty.",
            "description": "Product description cannot be empty."
        }

        if item is None or item.strip() == '':
            raise InvalidDataError("Order must have an item.", self)

        for key, value in order_attributes_items.items():
            if order_attributes.get(key) is None or order_attributes.get(key).strip() == '':
                raise InvalidDataError(value, self)

    @property
    def order_number(self):
        return self._order_number

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):
        self._error = error

    @property
    def item(self):
        return self._item

    @property
    def name(self):
        return self._name

    @property
    def product_id(self):
        return self._product_id

    @property
    def factory(self):
        return self._factory

    @property
    def item_attributes(self):
        return self._item_attributes
