# task 1
print('task 1')
list_1 = [2, 4, 7, 4, 2, 9, 4]
list_2 = [4, 1, 7, 8, 3, 1, 9]
set_1 = set(list_1)
set_2 = set(list_2)
list_3 = sorted(list(set_1.intersection(set_2)))

for i in list_3:
    print(i, end=' ')

# task 2
print('\n\ntask 2')
students_score = {
    'Lena': 45,
    'Ivan': 67,
    'Oksana': 82,
    'Maksim': 49,
    'Artem': 77
}
average_score = sum(students_score.values()) / len(students_score)
print('Average score: ', average_score)

for key, value in students_score.items():
    if value > average_score:
        print(key, ':', value)

# task 3
print('\ntask 3')
number_list = [4, 6, 7, 6, 6, 3, 4, 9, 2, 6, 9]
number_set = set(number_list)

for i in number_set:
    print(i, '--', number_list.count(i))

# task 4
print('\ntask 4')
list_1 = list(input('Enter first list of numbers (exmpl: 64635...): '))
list_2 = list(input('Enter second list of numbers (exmpl: 54241478...): '))
set_inter = set(list_1).intersection(set(list_2))
list_inter = sorted(list(set_inter))

for i in list_inter:
    print(i, end=' ')

# task 5
print('\n\ntask 5')
text_1 = 'one two three one four five seven ten seven one'
text_1 = text_1.split(' ')
set_1 = set(text_1)
set_2 = set()

for i in set_1:
    set_2.add((i, text_1.count(i)))

for i in list(set_2):
    print(i, end=' ')
