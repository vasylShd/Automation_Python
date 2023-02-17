# task 1
name = input('Enter your name: ')
last_name = input('Enter your lastname: ')
# name = 'vasyl'
# last_name = 'shadura'

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

r = int(input('Enter circle radius: '))
l = 2 * pi * r
s = pi * r**2
print('circle length:', '{:.1f}'.format(l))
print('circle area:', '{:.1f}'.format(s))




