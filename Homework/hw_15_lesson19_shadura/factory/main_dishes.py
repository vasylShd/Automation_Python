from taiwanese_cuisine import TaiwanDishes


class BeefNoodleSoup(TaiwanDishes):
    name: str = 'Beef Noodle Soup'

    def __init__(self):
        super().__init__()
        self.weight = 270
        self.meat_present = True
        self.price = 100


class HotPot(TaiwanDishes):
    name: str = 'Hot Pot'

    def __init__(self):
        super().__init__()
        self.weight = 250
        self.meat_present = True
        self.price = 120


class BraisedPorkRice(TaiwanDishes):
    name: str = 'Braised Pork Rice'

    def __init__(self):
        super().__init__()
        self.weight = 220
        self.meat_present = True
        self.price = 270


class CenturyEgg(TaiwanDishes):
    name: str = 'Century Egg'

    def __init__(self):
        super().__init__()
        self.weight = 50
        self.meat_present = False
        self.price = 1050


class StinkyTofu(TaiwanDishes):
    name: str = 'Stinky Tofu'

    def __init__(self):
        super().__init__()
        self.weight = 150
        self.meat_present = False
        self.price = 700


class XiaoLongBao(TaiwanDishes):
    name: str = 'Xiao Long Bao'

    def __init__(self):
        super().__init__()
        self.weight = 300
        self.meat_present = True
        self.price = 650
