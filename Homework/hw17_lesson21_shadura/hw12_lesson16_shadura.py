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
                 total_power, battery_capacity, mileage_per_charge_100_proc):
        super().__init__(brend, model, color, car_class, fuel_type, total_power)
        self.battery_capacity = battery_capacity
        self.mileage_per_charge_100_proc = mileage_per_charge_100_proc
        self.charge_time_to_full = None
        self.prcnt_battery_distance = None

    def charge_time(self, battery_remaining_proc, mains_power):
        if mains_power == 0:
            return 'Mains power - 0 kW. Plug it in'
        """Визначення часу зараду батареї в залежності від ємності, залишку і потужності мережі"""
        need_charge_kw = self.battery_capacity * (100 - battery_remaining_proc) // 100
        self.charge_time_to_full = round(need_charge_kw / mains_power, 1)
        return self.charge_time_to_full

    def driving_faraway(self, battery_remaining_proc):
        """Попередження, якщо машина може проїхати лише до 180 км на повній зарядці.
        Розрахунок дальності поїздки з урахуванням залишку батареї"""
        if self.mileage_per_charge_100_proc < 180:
            print('УВАГА! Краще не їздити на цій машині на далекі відстані!')
        self.prcnt_battery_distance = self.mileage_per_charge_100_proc * battery_remaining_proc / 100
        return self.prcnt_battery_distance


class Tesla(ElectroCar):
    def __init__(self, brand, model, color, car_class, fuel_type, total_power,
                 battery_capacity, mileage_per_charge_100_proc):
        super().__init__(brand, model, color, car_class, fuel_type, total_power,
                         battery_capacity, mileage_per_charge_100_proc)

    def driving_faraway(self, battery_remaining_proc):
        """Розрахунок дальності поїздки з урахуванням залишку батареї"""
        self.prcnt_battery_distance = self.mileage_per_charge_100_proc * battery_remaining_proc / 100
        return self.prcnt_battery_distance

# car1 = Tesla('Tesla', 'model x', 'Blue', 'sedan', 'electro', 700, 100, 450)
# print(car1.driving_faraway(50))
# print(car1.prcnt_battery_distance)
