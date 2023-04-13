import random
from collections import Counter


# task 1

def function_name(func):
    def inner(*args, **kwargs):
        result = func(*args)
        return f'{result} \nFunction name is "{func.__name__}"'

    return inner


@function_name
def sum(a, b):
    return a + b


@function_name
def multiplication(a, b):
    return a * b


if __name__ == '__main__':
    print('task 1')

    print(sum(4, 8))
    print(multiplication(5, 7))

# task 2

if __name__ == '__main__':
    print('\ntask 2')

    list_rand = [random.randint(1, 10) for item in range(100)]

    count = Counter(list_rand)

    for k, v in count.items():
        print(f'{k} - {v}')
