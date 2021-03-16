class Order:
    def __init__(self, order_number=-1, item='', name='', product_id=0, **order_attributes):
        self._order_number = order_number
        self._item = item
        self._name = name
        self._product_id = product_id
        self._factory = order_attributes.get("factory")
        self._item_attributes = order_attributes
