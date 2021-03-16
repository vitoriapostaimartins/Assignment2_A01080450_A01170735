import abc


class Item(abc.ABC):
    def __init__(self, product_id=-1, name="", description="", **item_attributes):
        self._product_id = product_id
        self._name = name
        self._description = description
        self.item_attributes = item_attributes

    def __str__(self):
        kwargs_items = "Kwargs Items: \n"
        for key, item in self.item_attributes.items():
            kwargs_items += f"\n {key}: {item}"

        return f"{self._product_id} \n" \
               f"{self._name} \n" \
               f"{self._description}\n" \
               f"{kwargs_items}"


class Toy(Item):
    def __init__(self, battery_operated=False, min_age=0, **kwargs):
        super().__init__(**kwargs)
        self._battery_operated = battery_operated
        self._min_age = min_age


# stuffed animals

class StuffedAnimal(Item):
    def __init__(self, stuffing=False, size="", fabric="", **kwargs):
        super().__init__(**kwargs)
        self._stuffing = stuffing  # fiberfill or wool
        self._size = size
        self._fabric = fabric


# candy
class Candy(Item):
    def __init__(self, has_nuts=False, lactose_free=False, **kwargs):
        super().__init__(**kwargs)
        self._has_nuts = has_nuts
        self._lactose_free = lactose_free
