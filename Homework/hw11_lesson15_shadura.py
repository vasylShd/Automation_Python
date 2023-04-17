# task 1
print('task 1')

class Dog:
    def __init__(self, name: str, gender: str, color: str,
                 age: int, weight: float, height: float):
        self.name = name
        self.gender = gender
        self.color= color
        self.age = age
        self.weight = weight
        self.height = height

    @staticmethod
    def bark(dog):
        print(f'{dog} say GAV-GAV!!!')

my_dog = Dog('Lucky', 'boy', 'red', 6, 3, 0.3)
print(my_dog.weight)
Dog.bark('Dog')
my_dog.bark(my_dog.name)


# task 2
print('\ntask 2')
import datetime

class Post:
    DEPART_COUNT = 0

    def __init__(self, depart_numb: int, address: str, ship_type: str,
                 employees_nmb: int, area: float, open_time: datetime,
                 close_time: datetime, rating: float):
        Post.DEPART_COUNT += 1
        self.depart_numb = depart_numb
        self.address = address
        self.ship_tipe = ship_type
        self.employees_nmb = employees_nmb
        self.area = area
        self.open_time = open_time
        self.close_time = close_time
        self.actual_rating = rating

    def __str__(self):
        return f'Post office {self.depart_numb} located at {self.address}' \
               f'\nIt opens at {self.open_time} and closes at {self.close_time}'


    @classmethod
    def total_departs(cls):
        return cls.DEPART_COUNT


nova_poshta_7 = Post(7, 'Kyiv, Oleny Teligy str, 36', 'till 30 kg',
                     9, 120, '09:00', '20:00', 4.2)

nova_poshta_14 = Post(14, 'Kyiv, Peremogy str, 15', 'till 100 kg',
                     12, 180, '09:00', '20:00', 4.5)

print(nova_poshta_7.close_time)
print(nova_poshta_14)

print(f'Total opened departs: {Post.total_departs()}')
