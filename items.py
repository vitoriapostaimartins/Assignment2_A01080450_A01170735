import abc


class Item(abc.ABC):
    def __init__(self, product_id=-1, name="", description="", **item_attributes):
        self._product_id = product_id
        self._name = name
        self._description = description
        self._item_attributes = item_attributes

    @property
    def product_id(self):
        return self._product_id

    @property
    def item_attributes(self):
        return self._item_attributes

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def __str__(self):
        kwargs_items = "Kwargs Items: \n"
        for key, item in self.item_attributes.items():
            if item is not None:
                kwargs_items += f"\n {key}: {item}"

        return f"product id:{self._product_id} \n" \
               f"name:{self._name} \n" \
               f"description:{self._description}\n" \
               f"{kwargs_items}"


class Toy(Item):
    def __init__(self, battery_operated=False, min_age=0, **kwargs):
        super().__init__(**kwargs)
        self._battery_operated = battery_operated
        self._min_age = min_age


# stuffed animals

class StuffedAnimal(Item):
    stuffing_types = ["Polyester Fiberfill", "Wool"]
    sizes = ["Small", "Medium", "Large"]
    fabric_types = ["Linen", "Cotton", "Acrylic"]

    def __init__(self, stuffing=False, size="", fabric="", **kwargs):
        super().__init__(**kwargs)

        if stuffing not in StuffedAnimal.stuffing_types:
            raise InvalidDataError(f"Stuffing can only be {', '.join(StuffedAnimal.stuffing_types)}")
        self._stuffing = stuffing  # fiberfill or wool

        if size not in StuffedAnimal.sizes:
            raise InvalidDataError(f"Sizes can only be {', '.join(StuffedAnimal.sizes)}")
        self._size = size

        if fabric not in StuffedAnimal.fabric_types:
            raise InvalidDataError(f"Fabric types can only be {', '.join(StuffedAnimal.fabric_types)}")
        self._fabric = fabric


# candy
class Candy(Item):
    def __init__(self, has_nuts=False, lactose_free=False, **kwargs):
        super().__init__(**kwargs)
        self._has_nuts = has_nuts
        self._lactose_free = lactose_free


class InvalidDataError(Exception):
    def __init__(self, error_string):
        super().__init__("InvalidDataError - " + error_string)
