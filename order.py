class Order:
    def __init__(self, order_number=-1, item='', name='', **order_attributes):
        try:
            if order_attributes.get("quantity") <= 0:
                raise InvalidDataError("Order quantity has to be a non-zero positive number.")
        except ValueError:
            raise InvalidDataError("Order quantity has to be a non-zero positive number.")

        self._order_number = order_number
        self._error = None
        self._item = item
        self._name = name
        self._product_id = order_attributes.get("product_id")
        self._factory = order_attributes.get("factory")
        self._item_attributes = order_attributes


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
