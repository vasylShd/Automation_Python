# task 1
name = input('Enter your name: ')
last_name = input('Enter your lastname: ')

full_name = name + ' ' + last_name
print('Personal data: ', full_name)

print(full_name.lower())
print(full_name.upper())
full_name = name.capitalize() + ' ' + last_name.capitalize()
print(full_name)

print(name * 5)

name = '\t' + name + '\t\n'
print(name)
name = name.strip()
print(name)

# task 2
from math import pi

circle_rad = float(input('Enter circle radius: '))
circle_len = 2 * pi * circle_rad
circle_ar = pi * circle_rad**2
print('circle length:', '{:.1f}'.format(circle_len))
print('circle area:', '{:.1f}'.format(circle_ar))

# task 3
usd_rate = 36.56
grn_amount = int(input('Enter grn amount: '))
grn_to_usd = grn_amount / usd_rate
grn_to_usd = round(grn_to_usd, 2)
print('Dollars amount at cuttent rate is: {}'.format(grn_to_usd))

