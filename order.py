class Order:
    def __init__(self, order_number=-1, item='', name='', **order_attributes):
        self._order_number = order_number
        self._item = item
        self._name = name
        self._product_id = order_attributes.get("product_id")
        self._factory = order_attributes.get("factory")
        self._item_attributes = order_attributes

    @property
    def item_attributes(self):
        return self._item_attributes
