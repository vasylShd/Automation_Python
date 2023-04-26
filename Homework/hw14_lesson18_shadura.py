
class Train:
    def __init__(self, name, direction):
        self.__name = name
        self.__direction = direction
        self.__traincars = dict()

    @property
    def name(self):
        return self.__name

    def move(self):
        for i in self.__direction:
            print(i)

    def __len__(self):
        return len(self.__traincars)

    def __setitem__(self, key, value):
        self.__traincars[key] = value

    def __getitem__(self, item):
        return self.__traincars[item]


class TrainCar:
    def __init__(self, number):
        self.__number = number
        self.__passengers = dict()

    @property
    def number(self):
        return self.__number

    def __len__(self):
        return len(self.__passengers)

    def __setitem__(self, key, value):
        self.__passengers[key] = {'name': key, 'boarding': value[0], 'destination': value[1], 'place': value[2]}

    def __getitem__(self, item):
        return self.__passengers[item]

    def __str__(self):
        for key, value in self.__passengers.items():
            print( f'name: {key}, \ndestination: {value["boarding"]} - {value["destination"]}, \nplace: {value["place"]}\n')
        return ''


train1 = Train('67/68', 'Boston-NewYork')

trainCar1 = TrainCar(1)
trainCar2 = TrainCar(2)
train1[1] = trainCar1
train1[2] = trainCar2

trainCar1['Kevin Kosner'] = ('Boston South Station', 'Kingston', 2)
trainCar1['Sandra Bulock'] = ('Boston South Station', 'New London', 7)
trainCar1['Tom Cruise'] = ('Route 128', 'Old Saybrook', 11)

trainCar2['Bruce Willis'] = ('Kingston', 'New York Penn Station' , 4)
trainCar2['Sylvester Stallone'] = ('New London', 'New York Penn Station', 7)
trainCar2['Leonardo DiCaprio'] = ('Stamford', 'New Rochelle', 3)

print(f'Count of traincars - {len(train1)}')
print(f'Count of passengers in traincar_1 - {len(train1[1])}\n')

print('passengers of traincar_1 --------------------------------------------')
print(train1[1])
print('passengers of traincar_2 --------------------------------------------')
print(train1[2])

print(train1[1]['Sandra Bulock'])
print(train1[2]['Leonardo DiCaprio'])
