import re

# task 1
print('task 1')


def domains_to_list(dom_file):
    '''The function that shows domains from the file'''
    with open(dom_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line[1:], end='')


domains_to_list('domains.txt')

# task 2
print('\n\ntask 2')
persons = [
    '1. Melnyck Ukraine',
    '2. Adams USA',
    '3. Hjörleifsdóttir Iceland',
    '4. Schneider Germany',
    '5. Williams UK',
    '6. Trzcinowski Poland',
    '7. Hämäläinen Finland',
    '8. Dagres Greece',
    '9. Romano Italy',
    '10. Darakhvelidze Georgia'
]

with open('names.txt', 'w') as file:
    for person in persons:
        file.write(person + '\n')


def show_names(name_file):
    '''The function that shows last names from the file'''
    with open(name_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            last_name = re.search(r'.*?\s(?P<name>.*?)\s.*', line).group('name')
            print(last_name)


show_names('names.txt')


# task 3
print('\ntask 3')
date_dict_list = []

def date_reader(author_file, date_list):
    '''The function that returns a list of dictionaries with dates from the file'''
    with open(author_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            raw_date = re.match(r'(?P<date_name>(\w+\s){2}\d{4}).*', line)
            if raw_date:
                date = raw_date.group('date_name')
                date_list.append({f'date': date})
    return date_list

date_dict_list = date_reader('authors.txt', date_dict_list)

for date_dict in date_dict_list:
    print(date_dict)