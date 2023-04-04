import datetime
import time

# task 2
print('task 2')

new_list = [1, 2, 'text', 4, 5]

try:
    for i in new_list:
        print(float(i))
except ValueError as vler:
    print('Warning! ValueError!')
    print(f'One element ("{i}") of the list is not number! The element {vler} error! ')
    print('The element will be removed!')
    new_list.remove(i)
    for i in new_list:
        print(float(i))
finally:
    print('Elements chenged to float and output of the elements is finished.')


# task 3
print('\ntask3')


def diff_date(date_in, days, plus):
    '''Function that adds or subtracts a certain number of days from a given date'''
    if plus == '+':
        return date_in + datetime.timedelta(days=days)
    else:
        return date_in - datetime.timedelta(days=days)

form_data = '%Y.%m.%d %H:%M'
dat = input(f'Enter date in format "{form_data}": ')
days = int(input('Enter count of days: '))
plus_minus = input('Enter date shift direction ("+" or "-"): ')

dat = datetime.datetime.strptime(dat, form_data)
print(diff_date(dat, days, plus_minus).strftime('%Y.%m.%d %H:%M'))
