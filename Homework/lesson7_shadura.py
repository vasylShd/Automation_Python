# task 1
print('task 1\n')

side_list = ['' for x in range(1, 5)]


def enter_side(sides):
    '''The function is for entering sides of a figure'''
    for i in range(len(sides)):
        sides[i] = float(input(f'Enter side {i + 1}: '))


def rectangle_area(side_1, side_2):
    '''This function calculates the rectangle area'''
    return side_1 * side_2


def check_rectangle():
    '''This function checks if the figure is square, rectangle or other quadrilateral'''
    a, b, c, d = int(side_list[0]), int(side_list[1]), int(side_list[2]), int(side_list[3])
    if len(side_set) == 1:
        print('This is Square')
    elif a ** 2 + b ** 2 == c ** 2 + d ** 2:
        print('This is Rectangle')
        print('Area of the rectangle:', rectangle_area(a, b))
    else:
        print('This is not rectangle. Enter correct data')


while True:
    enter = input('Press "enter" or enter "stop": ')
    if enter == 'stop':
        break
    enter_side(side_list)
    side_set = set(side_list)
    check_rectangle()

# task 2
print('\ntask 2\n')
import random
from string import ascii_lowercase

names_list = ['you', 'press', 'services', 'loretta', 'berezka', 'katalina', 'bilka']
domains_list = ['net', 'com', 'ua', 'us', 'tv', 'uk', 'hk', 'cy']


def create_email(names, domains):
    while True:
        enter = input('Press "enter" or enter "stop": ')
        if enter == 'stop':
            break
        name = random.choice(names)
        domain = random.choice(domains)
        rand_number = random.randint(100, 999)
        rand_str = ''.join(random.choice(ascii_lowercase) for i in range(random.randint(5, 7)))
        print(f'{name}.{rand_number}@{rand_str}.{domain}')


create_email(names_list, domains_list)

# additional tasks
from functools import reduce

print('\ntask 3.1\nНапишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.\n')

list1 = [3, 4, 5, 7, 2, 6]
list2 = [4, 6, 8, 3, 5, 6, 9, 1]

list_3 = lambda l1, l2: list(set(l1) & set(l2))
print(list_3(list1, list2))

print('\ntask 3.2\nНапишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда\n')

number = input('Enter number: ')
check_number = lambda number: print('This is number') if number.isdigit() else print('This isn`t number')
check_number(number)

print('\ntask 3.3\nНапишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за '
      'допомогою лямбда.\n')

list1 = [3, 4, 5, 7, 2, 6]
list2 = [4, 6, 8, 3, 5, 6, 9, 1]
list3 = [3, 5, 2]
list4 = [6, 7, 3, 2, 7, 5, 9, 3, 6, 7]
list5 = [3, 5, 7, 2]
lists = [list1, list2, list3, list4, list5]

long_list = reduce(lambda x, y: x if (len(x) > len(y)) else y, lists)
short_list = reduce(lambda x, y: x if (len(x) < len(y)) else y, lists)
print('Longest lists- ', long_list)
print('Shortest list- ', short_list)

print('\ntask 3.4\nНапишіть програму на Python для обчислення добутку заданого списку чисел за допомогою лямбда\n')

list_a = [3, 5, 7, 45, 7, 23, 5, 9]
multiple = reduce(lambda x, y: x * y, list_a)
print(multiple)
