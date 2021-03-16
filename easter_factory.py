from item_factory import ItemFactory
from items import Toy, StuffedAnimal, Candy


class EasterFactory(ItemFactory):
    def __init__(self):
        super().__init__()
        pass


class RobotBunny(Toy):
    def __init__(self):
        super().__init__()
        pass


class EasterBunny(StuffedAnimal):
    def __init__(self):
        super().__init__()
        pass

class CremeEggs(Candy):
    def __init__(self):
        super().__init__()
        pass
