def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        print('integer division or modulo by zero')


if __name__ == '__main__':
    def exponentiation(a, b):
        return a ** b

    