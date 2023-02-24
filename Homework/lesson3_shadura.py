# # task 1
import random

min = random.randint(0, 59)

if min >= 0 and min < 15:
    print('{} is in I-quarter'.format(min))
elif min >= 15 and min < 30:
    print('{} is in II-quarter'.format(min))
elif min >= 30 and min < 45:
    print('{} is in III-quarter'.format(min))
else:
    print('{} is in IV-quarter'.format(min))


# task 2
birth_month = input('Enter your birth month number: ')

if birth_month.isdigit():
    birth_month = int(birth_month)
    if birth_month == 1 or birth_month == 2 or birth_month == 12:
        print('Зима - За вікном падав сніг.')
    elif birth_month >= 3 and birth_month <= 5:
        print('Весна - Все довкола розцвітало.')
    elif birth_month >= 6 and birth_month <= 8:
        print('Літо - Діти насолоджувались літніми канікулами.')
    elif birth_month >= 9 and birth_month <= 11:
        print('Осінь - Все довкола загоралось яскравими фарбами.')
    else:
        print('Incorrect data, please enter again!')
else:
    print('Incorrect data, please enter again!')


# task 3
num = random.randint(1, 1000)
num = str(num)
sum_dgts = 0
for i in num:
    sum_dgts += int(i)
last_dgt = int(num[-1])
if sum_dgts % 3 == 0 and last_dgt % 2 == 0:
    print('Число {} ділиться на 6'.format(num))
else:
    print('Число {} не ділиться на 6'.format(num))
