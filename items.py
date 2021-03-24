"""
Module that contains Item abstract base class and the concrete classes that extend it.
This module also contains InvalidDataError, for when an attribute in an item is
found to be invalid.
"""

import abc


class Item(abc.ABC):
    """
    Class that represents an Item that a Store sells.
    """

    def __init__(self, **item_attributes):
        """
        Initialize an Item object with attributes in a dictionary.
        :param item_attributes: a dictionary
        """
        self._product_id = item_attributes.get("product_id")
        self._name = item_attributes.get("name")
        self._description = item_attributes.get("description")
        self._item_attributes = item_attributes

    @property
    def product_id(self):
        """
        Get the product identifier of this Item.
        :return: a string
        """
        return self._product_id

    @property
    def item_attributes(self):
        """
        Get the item attributes from this Item.
        :return: a dictionary
        """
        return self._item_attributes

    @property
    def name(self):
        """
        Get the name of this Item.
        :return: a string
        """
        return self._name

    @property
    def description(self):
        """
        Get the description of this Item.
        :return: a string
        """
        return self._description

    @staticmethod
    def check_attributes(item_attributes, errors):
        """
        Check the attributes from an Item and raise exceptions if necessary.
        :param item_attributes: a dictionary
        :param errors: a dictionary
        """
        for attribute, message in errors:
            if item_attributes.get(attribute) not in message[0]:
                raise InvalidDataError(f"{message[1]}")

    def __str__(self):
        """
        Get a string containing relevant information about this Item.
        :return: a string
        """
        kwargs_items = "Kwargs Items: \n"
        for attribute, value in self.item_attributes.items():
            if value is not None:
                kwargs_items += f"\n {attribute}: {value}"

        return f"product id:{self.product_id} \n" \
               f"name:{self.name} \n" \
               f"description:{self.description}\n" \
               f"{kwargs_items}"


class Toy(Item):
    """
    Class representing a toy sold at the store.
    """
    battery_options = ["Y", "N"]
    age_range = list(range(0, 16))

    attribute_errors = {
        "has_batteries": [battery_options, f"Has batteries must be indicated as {' or '.join(battery_options)}"],
        "min_age": [age_range, f"Minimum age must be between {age_range[0]} and {age_range[-1]}"]
    }

    def __init__(self, **item_attributes):
        """
        Initialize a Toy with indicators for battery and minimum age requirement.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, Toy.attribute_errors.items())
        except InvalidDataError as e:
            raise e
        self._has_batteries = item_attributes.get("has_batteries")
        self._min_age = item_attributes.get("min_age")
        super().__init__(**item_attributes)


class StuffedAnimal(Item):
    """
    Class representing a stuffed animal sold at the store.
    """
    stuffing_types = ["Polyester Fibrefill", "Wool"]
    sizes = ["S", "M", "L"]
    fabric_types = ["Linen", "Cotton", "Acrylic"]

    attribute_errors = {"stuffing": [stuffing_types, f"Stuffing can only be {', '.join(stuffing_types)}"],
                  "size": [sizes, f"Sizes can only be {', '.join(sizes)}"],
                  "fabric": [fabric_types, f"Fabric types can only be {', '.join(fabric_types)}"]}

    def __init__(self, **item_attributes):
        """
        Initialize a stuffed animal with stuffing, size, and fabric.
        :param item_attributes: a dictionary
        """
        try:
            super().check_attributes(item_attributes, StuffedAnimal.attribute_errors.items())
        except InvalidDataError as e:
            raise e

        self._stuffing = item_attributes.get("stuffing")
        self._size = item_attributes.get("size")
        self._fabric = item_attributes.get("fabric")

        super().__init__(**item_attributes)


class Candy(Item):
    """
    Class representing a Candy sold at the store.
    """

    def __init__(self, **item_attributes):
        """
        Initialize a Candy item, with indicators for nut and lactose content.
        :param item_attributes: a dictionary
        """
        self._has_nuts = item_attributes.get("has_nuts")
        self._lactose_free = item_attributes.get("lactose_free")
        super().__init__(**item_attributes)


class InvalidDataError(Exception):
    """
    Exception thrown when an item or order has invalid data.
    """

    def __init__(self, error_string, order=None):
        """
        Initialize a InvalidDataError Exception with a error string, optionally, an Order object.
        .
        :param error_string: a string
        :param order: an Order object
        """
        error_string = "InvalidDataError - " + error_string
        if order is not None:
            order.error = error_string
        super().__init__(error_string)
