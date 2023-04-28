from main_dishes import BeefNoodleSoup, HotPot, BraisedPorkRice, CenturyEgg, StinkyTofu, XiaoLongBao
from desserts import ShavedIce, PineappleCake
from drinks import GaoLiang, TaihuBeer, PearlTea, OolongTea


class OrderPart:
    def __init__(self, client_name):
        self.client_name = client_name

    def get_main_dish(self, name: str):
        if name == 'Beef Noodle Soup':
            return BeefNoodleSoup()
        elif name == 'Hot Pot':
            return HotPot()
        elif name == 'Braised Pork Rice':
            return BraisedPorkRice()
        elif name == 'Century Egg':
            return CenturyEgg()
        elif name == 'Stinky Tofu':
            return StinkyTofu()
        elif name == 'Xiao Long Bao':
            return XiaoLongBao()

    def get_dessert(self, name: str):
        if name == 'Shaved Ice':
            return ShavedIce()
        elif name == 'Pineapple Cake':
            return PineappleCake()

    def get_drinks(self, name: str):
        if name == 'Gao Liang':
            return GaoLiang()
        elif name == 'Taihu Beer':
            return TaihuBeer()
        elif name == 'Pearl Tea':
            return PearlTea()
        elif name == 'Oolong Tea':
            return OolongTea()


order_1 = OrderPart('Wang Li')
print(order_1.client_name)
first_dishes_1 = order_1.get_main_dish('Beef Noodle Soup')
dessert_1 = order_1.get_dessert('Pineapple Cake')
drink_1 = order_1.get_drinks('Taihu Beer')

print(f'Dear, {order_1.client_name}, You ordered {first_dishes_1.name}, {dessert_1.name}, {drink_1.name}. \
Plese pay {first_dishes_1.price + dessert_1.price + drink_1.price} TWD for your order.')

print(first_dishes_1.description())
print(dessert_1.description())
print(drink_1.description())
print()

order_2 = OrderPart('Yang Liu')
print(order_2.client_name)
first_dishes_2 = order_2.get_main_dish('Century Egg')
dessert_2 = order_2.get_dessert('Shaved Ice')
drink_2 = order_2.get_drinks('Oolong Tea')

print(f'Dear, {order_2.client_name}, You ordered {first_dishes_2.name}, {dessert_2.name}, {drink_2.name}. \
Plese pay {first_dishes_2.price + dessert_2.price + drink_2.price} TWD for your order.')

print(first_dishes_2.description())
print(dessert_2.description())
print(drink_2.description())
