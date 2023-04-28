from taiwanese_cuisine import TaiwanDrinks


class GaoLiang(TaiwanDrinks):
    name: str = 'Gao Liang'

    def __init__(self):
        super().__init__()
        self.volume = 50
        self.alcogol_present = True
        self.price = 350


class TaihuBeer(TaiwanDrinks):
    name: str = 'Taihu Beer'

    def __init__(self):
        super().__init__()
        self.volume = 500
        self.alcogol_present = True
        self.price = 120


class PearlTea(TaiwanDrinks):
    name: str = 'Pearl Tea'

    def __init__(self):
        super().__init__()
        self.volume = 300
        self.alcogol_present = False
        self.price = 140


class OolongTea(TaiwanDrinks):
    name: str = 'Oolong Tea'

    def __init__(self):
        super().__init__()
        self.volume = 250
        self.alcogol_present = False
        self.price = 80
