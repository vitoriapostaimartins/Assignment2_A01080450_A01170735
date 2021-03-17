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

    def __init__(self, item_attribute):
        if item_attribute.get('spider_type') not in RCSpider.spider_types:
            raise InvalidDataError(f"Spider type can only be {' or '.join(RCSpider.spider_types)}")
        super().__init__(**item_attribute)



class DancingSkeleton(StuffedAnimal):
    def __init__(self, item_attribute):
        if item_attribute.get("has_glow") != "Y":
            raise InvalidDataError(f"Dancing Skeletons have to glow in the dark")
        if item_attribute.get("fabric") != "Acrylic":
            raise InvalidDataError(f"Dancing Skeletons must be made of Acrylic")
        if item_attribute.get("stuffing") != "Polyester Fiberfill":
            raise InvalidDataError(f"Dancing Skeletons must be stuffed with Polyester Fiberfill")
        super().__init__(**item_attribute)


class PumpkinCaramelToffee(Candy):

    varieties = ["Sea Salt", "Regular"]

    def __init__(self, item_attribute):
        if item_attribute.get('variety') not in PumpkinCaramelToffee.varieties:
            raise InvalidDataError(f"Variety must be {' or '.join(PumpkinCaramelToffee.varieties)}")
        super().__init__(**item_attribute)

