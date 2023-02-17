# https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/index.html

'''
1. Number.....unchangeable
    int
    float
2. String.....unchangeable, ordered
3. List..................changeable, ordered
4. Dictionary.............changeable, ordered
5. Tuple......unchangeable, ordered
6. Set....................changeable, unordered.........unique datas, not-dublicate
7. Boolean
'''

# dir(modul)  - shows all methods

'''
Numbers
---------------------------------------------------
int()        - int("11111111", 2) - 255
bin(numbr)   - bin(10)            - '0b1010'
hex(numbr)   - hex(10)            - '0xa'

String
----------------------------------------------------
metods:
str[::-1]    ........разворот строки
','.join(str1)........собирает список строк в одну строку с разделителем, который указан перед join
str.title()   .......выполняют преобразование регистра строки
str1.upper()  .......выполняют преобразование регистра строки 
str1.lower()   ......выполняют преобразование регистра строки
str1.swapcase()  ....выполняют преобразование регистра строки
str1.capitalize() ...выполняют преобразование регистра строки
str1.islower()
str1.isupper()
str1.count('') ......используется для подсчета того, сколько раз символ или подстрока встречаются в строке
str1.find('') .......можно передать подстроку или символ, и он покажет, на какой позиции находится первый символ подстроки (для первого совпадения)
str1.startswith() ...Проверка на то, начинается или заканчивается ли строка на определенные символы
str1.endswith() .....Проверка на то, начинается или заканчивается ли строка на определенные символы
str1.replace('', '').Замена последовательности символов в строке на другую последовательность
str1.strip()  .......избавиться от /n, /t, очень удобно использовать метод strip()
str1.split('')  .....разбивает строку на части, используя как разделитель символ (или символы) и возвращает список строк
len(str1)  ..........длина строки
print('{}'.format('10.1.1.1'))
print("{:.3f}".format(10.0/3))
{ip}/{mask}'.format(mask=24, ip='10.1.1.1')
'{1}/{0}'.format(24, '10.1.1.1')
С помощью форматирования строк можно выводить результат столбцами. В форматировании строк можно указывать,
какое количество символов выделено на данные. Если количество символов в данных меньше, чем выделенное 
количество символов, недостающие символы заполняются пробелами.
Выравнивание по правой стороне:
vlan, mac, intf = ['100', 'aabb.cc80.7000', 'Gi0/1']
print("{:>15} {:>15} {:>15}".format(vlan, mac, intf))
            100  aabb.cc80.7000           Gi0/1
Выравнивание по левой стороне:
print("{:15} {:15} {:15}".format(vlan, mac, intf))
100             aabb.cc80.7000  Gi0/1


List
------------------------------------------------------
list1 = [1, 2, 3]
list1 = list('')
list1.reverse()
len(list1)
sorted(list1)
list1.append('')
list1.extend(list2)
list1.pop(-1)
list1.remove('')
list1.index('')
list1.insert(1, '')
list.sort()

Dictionary
-------------------------------------------------------
dict1 = {key:value, k:v}
dict1 = dict([('key', 'value'), ('key', 'value')])
dict1 = dict.fromkeys(list_of_keys)
dict1.clear()
dict2 = dict.copy()
dict1.get('key', 'key', 'key')
dict1.setdefault('key')
dict1.keys()
dict2.values()
dict1.items()
del dict1['key']
dict1.update(dict2)

Tuple
-------------------------------------------------------
tuple1 = tuple()
tuple1 = (1, 2, 3)
tuple1[3]
sorted(tuple1)

Set
------------------------------------------------------
set1 = set()
set1 = set(list1)
set1.add('')
set1.discard('')
set1.clear()
set1.union(set2)        (|)
set1.intersection(set2)  &  

Checking of types
-----------------------------------------------------                          
isdigit
isalpha
isalnum
type
'''

# first_name = 'Vas'
# print(hex(id(first_name)))
# first_name = 'Oleg'
# print(hex(id(first_name)))
# last_name = 'Vas'
# print(hex(id(last_name)))

# object: id, type, value
# is, is not
a = 3
b = 5
# b = a
# print(a is b)
#
# # type()
# print(type(a))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a**2)
# print(round((8 - 5 + 4 / 3 * 2)**2, 2))

# float_value = 5.987986782563
# print(round(float_value, 5))
from math import sqrt
import math
import random

# print(sqrt(16))
# print(dir(math))
# print(dir(random))
# print(random.randint(3, 9))
# print(random.randrange(15, 25, 2))
# print(random.choice(['jhg', 'jyftyy', 'hggfd']))


# string
# print(dir(str))

# full_nume = '\n\t' + 'jggj' + '\n\t' + 'jhgjh'
# print(full_nume.lstrip())


from lesson_1 import test_1

test_1()

import lesson_1
lesson_1.test_1()

# pip install isort  (сортировка файлов)
