from item_factory import ItemFactory
from items import Toy, StuffedAnimal, Candy, InvalidDataError


class HalloweenFactory(ItemFactory):
    def __init__(self, **item_attributes):
        super().__init__(**item_attributes)

    @staticmethod
    def make_toy(**item_attributes) -> Toy:
        return RCSpider(item_attributes)

    @staticmethod
    def make_stuffed_animal(**item_attributes) -> StuffedAnimal:
        return DancingSkeleton(item_attributes)

    @staticmethod
    def make_candy(**item_attributes) -> Candy:
        return PumpkinCaramelToffee(item_attributes)


class RCSpider(Toy):
    spider_types = ["Tarantula", "Wolf Spider"]
    speed_range = list(range(0, 100))
    jump_height = list(range(0, 100))

    attributes = {
        "spider_type": [spider_types, f"Spider type can only be {' or '.join(spider_types)}."],
        "has_batteries": [["Y"], "RCSpider requires batteries. Property has_batteries should be 'Y'."],
        "speed": [speed_range, f"RCSpider must have speed between {speed_range[0]} and {speed_range[-1]}"],
        "jump_height": [jump_height, f"RCSpider must have jump height between {jump_height[0]} and {jump_height[-1]}"]
    }

    def __init__(self, item_attributes):
        try:
            super().check_attributes(item_attributes, RCSpider.attributes.items())
        except InvalidDataError as e:
            raise e

        self._spider_type = item_attributes.get("spider_type")
        self._has_batteries = item_attributes.get("has_batteries")
        self._speed = item_attributes.get("speed")
        self._has_glow = item_attributes.get("has_glow")
        super().__init__(**item_attributes)


class DancingSkeleton(StuffedAnimal):
    attributes = {
        "has_glow": [["Y"], "Dancing Skeletons have to glow in the dark. Property has_glow should be 'Y'."],
        "fabric": [["Acrylic"], "Dancing Skeletons must be made of Acrylic."],
        "stuffing": [["Polyester Fibrefill"], "Dancing Skeletons must be stuffed with Polyester Fibrefill."]
    }

    def __init__(self, item_attributes):
        try:
            super().check_attributes(item_attributes, DancingSkeleton.attributes.items())
        except InvalidDataError as e:
            raise e

        self._has_glow = item_attributes.get("has_glow")

        super().__init__(**item_attributes)


class PumpkinCaramelToffee(Candy):
    varieties = ["Sea Salt", "Regular"]

    attributes = {
        "variety": [varieties, f"Variety must be {' or '.join(varieties)}."],
        "has_nuts": [["Y"], "Pumpkin Caramel Toffee may contain traces of nuts. Property has_nuts should be 'Y'."],
        "has_lactose": [["Y"], "Pumpkin Caramel Toffee is not lactose free. Property has_lactose should be 'Y'."]
    }

    def __init__(self, item_attributes):
        try:
            super().check_attributes(item_attributes, PumpkinCaramelToffee.attributes.items())
        except InvalidDataError as e:
            raise e
        self._variety = item_attributes.get("variety")
        super().__init__(**item_attributes)
