# a = int(input('Enter a - '))
# b = int(input('Enter b - '))
#
# print(a + b) if a > b else print(a) if a == 5 else print(a - b)

# name = 'Chris'
#
# # 1. f strings
# print(f'Hello {name}')
#
# # 2. % operator
# print('Hey %s %s' % (name, name))
#
# # 3. format
# print(
#  "My name is {}".format((name))
# )

'''
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!

1.Красивое лучше, чем уродливое.
2.Явное лучше, чем неявное.
3.Простое лучше, чем сложное.
4.Сложное лучше, чем запутанное.
5.Плоское лучше, чем вложенное.
6.Разреженное лучше, чем плотное.
7.Читаемость имеет значение.
8.Особые случаи не настолько особые, чтобы нарушать правила.
9.При этом практичность важнее безупречности.
10.Ошибки никогда не должны замалчиваться.
11.Если они не замалчиваются явно.
12.Встретив двусмысленность, отбрось искушение угадать.
13.Должен существовать один и, желательно, только один очевидный способ сделать это.
14.Хотя он поначалу может быть и не очевиден, если вы не голландец [^1].
15.Сейчас лучше, чем никогда.
16.Хотя никогда зачастую лучше, чем прямо сейчас.
17.Если реализацию сложно объяснить — идея плоха.
18.Если реализацию легко объяснить — идея, возможно, хороша.
19.Пространства имён — отличная штука! Будем делать их больше!
'''

# function -> function, function_name
# variables -> x, variable_name, variable_1
# class -> ClassNane
# method -> method, class_method
# constant -> CONSTANT, LONG_CONSTANT
# module -> module.py, my_module.py
# package -> package


# not recomendet
x = "Mari"
# recomended
name = "Mari"


def multiple_by_two(x):
    return x * 2


# from demoPackage import (jjhgjh, jkghgf,
#                          cfhgfh
#                          )


class MyFirstClass:
    """
    this is first demo class
    this is second
    """

    def first_method(self, first_param, second_param,
                     third_param):
        pass

    def second_method(self):
        pass


class MySecondClass:
    pass


def demo_function():
    pass

def test_1():
    print(int(input('Enter numb - ')))

first_var = 5
second_var = 7  # TODO gjhfhfghfdhgdhgfdgfdghdhd
third_var = 3
result = (first_var + second_var
          - third_var
          )

x = 3
if x > 5:
    print("x is bigger than 5")

list_of_number = [
    1, 2, 5,
    5, 7, 9
]

# comment is till 72 simbols, not comment - 79 simbols

# spaces ' '
# -, +=, -+, ==, !=, >, <, >=, <=, is, is not, in, not in, and, or, not

# recommend
if x > 5 and x % 2 == 0:
    print("")

# format of file   - black file.py   (black - programm)
