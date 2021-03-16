from item_factory import ItemFactory
from items import StuffedAnimal, Candy, Toy


class ChristmasFactory(ItemFactory):
    def __init__(self):
        super().__init__()
        pass


# santa's workshop
class SantasWorkshop(Toy):
    def __init__(self):
        super().__init__()
        pass


# reindeer
class Reindeer(StuffedAnimal):
    def __init__(self):
        super().__init__()
        pass


# candy canes
class CandyCane(Candy):
    def __init__(self):
        super().__init__()
        pass
