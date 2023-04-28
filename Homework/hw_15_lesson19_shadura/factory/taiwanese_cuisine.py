from abc import ABC


class TaiwanDishes(ABC):
    name: str = ''

    def __init__(self):
        self.weight = None
        self.meat_present = False
        self.price: int = 0

    def description(self):
        if self.meat_present:
            nope = ''
        else:
            nope = 'not'
        return f'The dish "{self.name}" has weight: {self.weight} gram, it has {nope} meat and it costs: {self.price} TWD'


class TaiwanDessert(ABC):
    name: str = ''

    def __init__(self):
        self.weight = None
        self.sugar_present = False
        self.price: int = 0

    def description(self):
        if self.sugar_present:
            nope = ''
        else:
            nope = 'not'
        return f'The dessert "{self.name}" has weight: {self.weight} gram, it has {nope} sugar and it costs: {self.price} TWD'


class TaiwanDrinks(ABC):
    name: str = ''

    def __init__(self):
        self.volume = None
        self.alcogol_present = False
        self.price: int = 0

    def description(self):
        if self.alcogol_present:
            nope = ''
        else:
            nope = 'not'
        return f'The drink "{self.name}" has volume: {self.volume} ml, it has {nope} alcohol and it costs: {self.price} TWD'
