# task 1
print('task 1')

def singleton(_class):
    def inner(*args):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args))
        return getattr(_class, 'instance')
    return inner

@singleton
class Purse:
    def __init__(self, valuta, name='unknow'):
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def up_balance(self, howmaney):
        self.__money += howmaney
        return howmaney

    def down_balance(self, howmaney):
        if self.__money - howmaney < 0:
            print('No money!')
            raise ValueError('No money!')
        self.__money -= howmaney
        return howmaney

    def info(self):
        print('Money- ', self.__money, '\nName- ', self.name, '\nValuta- ', self.valuta)


wallet_1 = Purse('USD', 'Vas')
wallet_1.up_balance(100)
wallet_1.info()
print()
wallet_2 = Purse('UAH', 'VS')
wallet_2.info()


# task 2  - see direction 'factory'




