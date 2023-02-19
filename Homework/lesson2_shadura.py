# task 1
name = input('Enter your name: ')
last_name = input('Enter your lastname: ')

full_name = name + ' ' + last_name
print('Personal data: ', full_name)

full_name = name.capitalize() + ' ' + last_name.capitalize()
print(full_name)

print(name * 5)

name = '\t' + name + '\t\n'
print(name)
name = name.strip()
print(name)

# task 2
from math import pi

radius = int(input('Enter circle radius: '))
c = 2 * pi * r
s = pi * r**2
print('circle length:', '{:.1f}'.format(c))
print('circle area:', '{:.1f}'.format(s))

# task 3
usd_rate = 36.56
grn_amount = int(input('Enter grn amount: '))
grn_to_usd = grn_amount / usd_rate
grn_to_usd = round(grn_to_usd, 2)
print('Dollars amount at cuttent rate is: {}'.format(grn_to_usd))

