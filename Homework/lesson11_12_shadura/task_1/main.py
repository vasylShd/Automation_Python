# without __init__ file
import package_1.algebraic_formulas.simple_math as smp_math
from package_1.algebraic_formulas.simple_math import multiplication as multi
from package_1.geometric_formulas import *
from package_1.geometric_formulas.figure_perimeter import circle_diameter as diamtr
from package_2.check_polindrom import polindrome as poli
import package_2.mail_adress as mail

# with __init__ file
from package_1 import diff, sthera_vol
from package_2 import polindrome


print('-----without __init__ file-----')
# import package_1.algebraic_formulas.simple_math as smp_math
print('Example 1')
print(smp_math.sum(10, 25))
print(smp_math.division(4, 0), '\n')

# from package_1.algebraic_formulas.simple_math import multiplication as multi
print('Example 2')
print(multi(7, 8), '\n')

# from package_1.geometric_formulas import *
print('Example 3')
print(body_capacity.parallelepiped_volume(10, 4, 2))
print(body_capacity.sphere_volume(4.5))
print(figure_area.circle_area(12))
print(figure_area.rectangle_are(4, 8))
print(figure_perimeter.triangle_perimeter(10, 12, 15), '\n')

# from package_1.geometric_formulas.figure_perimeter import circle_diameter as diamtr
print('Example 4')
print(diamtr(16), '\n')

# from package_2.check_polindrom import polindrome as poli
print('Example 5')
poli('TENET')

# import package_2.mail_adress as mail
print('\nExample 6')
print(mail.get_adress('main_support'), '\n')


print('-----with __init__ file-----')
# from package_1 import diff, sthera_vol
print('Example 7')
print(diff(47, 12))
print(sthera_vol(17), '\n')

# from package_2 import polindrome
print('Example 8')
polindrome('TELNET')
