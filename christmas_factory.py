from item_factory import ItemFactory
from items import StuffedAnimal, Candy, Toy, InvalidDataError


class ChristmasFactory(ItemFactory):
    def __init__(self, **item_attributes):
        super().__init__(**item_attributes)

    @staticmethod
    def make_toy(**item_attributes) -> Toy:
        return SantasWorkshop(item_attributes)

    @staticmethod
    def make_stuffed_animal(**item_attributes) -> StuffedAnimal:
        return Reindeer(item_attributes)

    @staticmethod
    def make_candy(**item_attributes) -> Candy:
        return CandyCane(item_attributes)


# santa's workshop
class SantasWorkshop(Toy):

    num_rooms = list(range(0, 100))

    attributes = {
        "has_batteries": [["N"], "Santa's workshop doesn't have batteries. Property has_batteries should be 'N'."],
        "num_rooms": [num_rooms, f"Number of rooms must be between {num_rooms[0]} and {num_rooms[-1]}"]
    }

    def __init__(self, item_attributes):

        try:
            item_attributes['dimensions'] = list(map(int, item_attributes.get("dimensions").split(",")))
        except ValueError:
            raise InvalidDataError("Dimensions have to be non-zero positive numbers")

        try:
            super().check_attributes(item_attributes, SantasWorkshop.attributes.items())
        except InvalidDataError as e:
            raise e

        for measurement in item_attributes.get("dimensions"):
            if measurement <= 0:
                raise InvalidDataError("Dimensions have to be non-zero positive numbers")

        self._dimensions = item_attributes.get("dimensions")
        self._num_rooms = item_attributes.get("num_rooms")

        super().__init__(**item_attributes)


class Reindeer(StuffedAnimal):
    attributes = {
        "fabric": [["Cotton"], "Reindeer have to be made out of Cotton."],
        "stuffing": [["Wool"], "Reindeer have to be stuffed with Wool."],
        "has_glow": [["Y"], "Reindeer have to be have a glow in the dark nose. Property has_glow should be 'Y'."]
    }

    def __init__(self, item_attributes):
        try:
            super().check_attributes(item_attributes, Reindeer.attributes.items())
        except InvalidDataError as e:
            raise e

        self._has_glow = item_attributes.get("has_glow")

        super().__init__(**item_attributes)


class CandyCane(Candy):
    colours = ["Red", "Green"]

    attributes = {
        "colour": [colours, f"Colour can only be {' or '.join(colours)}"],
        "has_nuts": [["N"], "Candy cane does not contain nuts. Property has_nuts should be 'N'."],
        "has_lactose": [["N"], "Candy cane is lactose free. Property has_lactose should be 'N'."]
    }

    def __init__(self, item_attributes):
        try:
            super().check_attributes(item_attributes, CandyCane.attributes.items())
        except InvalidDataError as e:
            raise e

        self._colour = item_attributes.get('colour')

        super().__init__(**item_attributes)
