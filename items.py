import abc


class Item(abc.ABC):
    def __init__(self, **kwargs):
        self._product_id
        self._name
        self._description
        pass


class Toy(Item):
    def __init__(self, **kwargs):
        super().__init__()
        self._battery_operated
        self._min_age
        pass


# stuffed animals

class StuffedAnimal(Item):
    def __init__(self):
        super().__init__()
        self._stuffing # fiberfill or wool
        self._size
        self._fabric
        pass


# candy
class Candy(Item):
    def __init__(self):
        super().__init__()
        self._has_nuts
        self._lactose_free
        pass
