import csv

# task 1
print('task 1')


def csv_reader(file_csv, line_list):
    '''function that reads a csv file'''
    with open(file_csv) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            line_list.append(row)
    return line_list


def csv_writer(file_csv, line_list):
    '''function that writes data to a csv file'''
    with open(file_csv, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(line_list)
        # for row in line_list:


data_list_1 = [['hostname', 'vendor', 'model', 'location'],
               ['sw1', 'Cisco', '3750', 'London'],
               ['sw2', 'Cisco', '3850', 'Dresden'],
               ['sw3', 'Cisco', '3650', 'Liverpool']]

data_list_2 = [['sw4', 'Cisco', '3550', 'Paris'],
               ['sw5', 'Cisco', '3250', 'Warsaw']]

data_list_3 = []

csv_writer('file_csv_1.csv', data_list_1)

data_list_3 = csv_reader('file_csv_1.csv', data_list_3)

data_list_3.extend(data_list_2)

csv_writer('file_csv_2.csv', data_list_3)


# task 2
print('task 2')

def numbers_square():
    '''function that returns the squares of all numbers in the range 0 - 100000'''
    counter = 0
    while counter <= 100000:
        yield counter ** 2
        counter += 1


squares_till_100000 = numbers_square()

for i in squares_till_100000:
    print(i)
