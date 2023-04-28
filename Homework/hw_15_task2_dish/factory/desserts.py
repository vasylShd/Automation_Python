from taiwanese_cuisine import TaiwanDessert


class ShavedIce(TaiwanDessert):
    name: str = 'Shaved Ice'

    def __init__(self):
        super().__init__()
        self.weight = 150
        self.sugar_present = True
        self.price = 270


class PineappleCake(TaiwanDessert):
    name: str = 'Pineapple Cake'

    def __init__(self):
        super().__init__()
        self.weight = 210
        self.sugar_present = False
        self.price = 340
