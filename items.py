import abc


class Item(abc.ABC):
    def __init__(self, **item_attributes):
        self._product_id = item_attributes.get("product_id")
        self._name = item_attributes.get("name")
        self._description = item_attributes.get("description")
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

    @staticmethod
    def check_attributes(item_attributes, dictionary):
        for key, value in dictionary:
            if item_attributes.get(key) not in value[0]:
                raise InvalidDataError(f"{value[1]}")

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
    battery_options = ["Y", "N"]
    age_range = list(range(0, 16))

    attributes = {
        "has_batteries": [battery_options, f"Has batteries must be indicated as {' or '.join(battery_options)}"],
        "min_age": [age_range, f"Minimum age must be between {age_range[0]} and {age_range[-1]}"]
    }

    def __init__(self, **item_attributes):
        try:
            super().check_attributes(item_attributes, Toy.attributes.items())
        except InvalidDataError as e:
            raise e
        self._has_batteries = item_attributes.get("has_batteries")
        self._min_age = item_attributes.get("min_age")
        super().__init__(**item_attributes)


class StuffedAnimal(Item):
    stuffing_types = ["Polyester Fibrefill", "Wool"]
    sizes = ["S", "M", "L"]
    fabric_types = ["Linen", "Cotton", "Acrylic"]

    attributes = {"stuffing": [stuffing_types, f"Stuffing can only be {', '.join(stuffing_types)}"],
                  "size": [sizes, f"Sizes can only be {', '.join(sizes)}"],
                  "fabric": [fabric_types, f"Fabric types can only be {', '.join(fabric_types)}"]}

    def __init__(self, **item_attributes):

        try:
            super().check_attributes(item_attributes, StuffedAnimal.attributes.items())
        except InvalidDataError as e:
            raise e

        self._stuffing = item_attributes.get("stuffing")
        self._size = item_attributes.get("size")
        self._fabric = item_attributes.get("fabric")

        super().__init__(**item_attributes)


class Candy(Item):

    def __init__(self, **item_attributes):
        self._has_nuts = item_attributes.get("has_nuts")
        self._lactose_free = item_attributes.get("lactose_free")
        super().__init__(**item_attributes)


class InvalidDataError(Exception):
    def __init__(self, error_string):
        super().__init__("InvalidDataError - " + error_string)
