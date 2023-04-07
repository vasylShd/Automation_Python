# task 1
print('task 1')


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


print(sum(4, 8))
print(multiplication(5, 7))

# task 2
