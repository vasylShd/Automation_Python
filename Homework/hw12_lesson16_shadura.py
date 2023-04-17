# task 1
print('task 1')

from abc import abstractmethod, ABC

class Car(ABC):
    def __init__(self, brend, model, color,
                 car_class, fuel_type, total_power):
        self.brend = brend
        self.model = model
        self.color = color
        self.car_class = car_class
        self.fuel_type = fuel_type
        self.total_power = total_power

    @abstractmethod
    def driving_faraway(self, remaining_fuel):
        """Заготовка для розрахунку дальності поїздки"""
        pass


class ElectroCar(Car):
    def __init__(self, brend, model, color, car_class, fuel_type,
                 total_power, battery_capacity):
        super().__init__(brend, model, color, car_class, fuel_type, total_power)
        self.battery_capacity = battery_capacity
        self.mileage_per_charge_100_proc = None


    def charge_time(self, battery_remaining_proc, mains_power):
        if mains_power == 0:
            return 'Mains power - 0 kW. Plug it in'
        """Визначення часу зараду батареї в залежності від ємності, залишку і потужності мережі"""
        need_charge_kw = self.battery_capacity * (100 - battery_remaining_proc) // 100
        charging_time = round(need_charge_kw / mains_power, 1)
        return charging_time

    def driving_faraway(self, battery_remaining_proc):
        """Попередження, якщо машина може проїхати лише до 180 км на повній зарядці.
        Розрахунок дальності поїздки з урахуванням залишку батареї"""
        if self.mileage_per_charge_100_proc < 180:
            print('УВАГА! Краще не їздити на цій машині на далекі відстані!')
        return self.mileage_per_charge_100_proc * battery_remaining_proc / 100


class Tesla(ElectroCar):
    def __init__(self, brand, model, color, car_class, fuel_type, total_power,
                 battery_capacity):
        super().__init__(brand, model, color, car_class, fuel_type, total_power,
                         battery_capacity)

    def driving_faraway(self, battery_remaining_proc):
        """Розрахунок дальності поїздки з урахуванням залишку батареї"""
        return self.mileage_per_charge_100_proc * battery_remaining_proc / 100



my_leaf = ElectroCar('Nissan', 'Leaf', 'Grey', 'Hatchback', 'Electric', 120, 40)
my_leaf.mileage_per_charge_100_proc = 150
print(my_leaf.model)
print(f'Час заряду до 100% - {my_leaf.charge_time(10, 5)} год.')
print(f'Можна проїхати ще {my_leaf.driving_faraway(50)} км на даному залишку')

print()
my_tesla = Tesla('Tesla', 'Model X', 'Blue', 'Crossover', 'Electric', 700, 90)
my_tesla.mileage_per_charge_100_proc = 450
print(my_tesla.color)
print(my_tesla.battery_capacity)
print(f'Час заряду до 100% - {my_tesla.charge_time(30, 6)} год.')
print(f'Можна проїхати ще {my_tesla.driving_faraway(30)} км на даному залишку')
