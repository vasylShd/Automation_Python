# open(file_name, mode, buffering, encoding, errors, newline, closefd, opener)
# ignore, replace, strict.....

# r - read only
# w - write only (перезапис существ)
# x - exclusive file (створ только новый)
# a - append to file
# b - binary file   -> rb, wb, xb
# t - text file -> rt, wt, xt,
# +
# close()

with open('test_10.txt') as file:
    pass

file = open('test_10.txt', 'r')

# file = open('/Automation_python_Hillel/Lessons/test_10.txt', 'r')

# reading-----------------------------------------------------------
# file.readline()
# file.read()         # (15)  -кол символ
# file.readlines()    # список строк

# result = file.read(15)     # (15)  -кол символ
result = file.readlines()

print(result)

# for line in file:
#     if cu

file.close()

# writing ----------------------------------------------------------
# write to file
#  mode -> w, wt

# r+   - read and write
# w+   - write and read
# a+   - append and read

file_to_write = open('demo_file.txt', 'w')
file_to_write.write('Hello word')

str_1 = 'Its_my_7_Life'
str_2 = 'it`s 4 now or never'
str_3 = 'But I ain`t gonna live forever'
str_4 = 'I_just_want_to_LIVE_7_while_I_am_alive'
str_5 = 'Yeah_this_is_for_1_who_stood_their_ground'
str_6 = 'For Tommy and Gina_who_never_backed_down'
strings = [str_1, str_2, str_3, str_4, str_5, str_6]

for st in strings:
    file_to_write.write(st + '\n')
file_to_write.close()

with open('test_10.txt', 'rb') as file:
    print(file.readlines())

with open('dog.jpeg', 'rb') as reader:
    print(reader.read(1))
    print(reader.read(2))

with open('test_10.txt', 'a') as file:
    file.write('\nhelllllllllll')

with open('test_10.txt', 'r') as reader, open('demo_file.txt', 'w') as writer:
    reader_reult = reader.readlines()
    writer.writelines(reader_reult)

with open('test_10.txt', 'r+') as file:
    lines = file.read()
    file.write('demo_string r+\n')

# ПОЗИЦИИ
# tell()   -> return current position
with open('test_10.txt', 'r') as file:
    print(file.readline(3))
    print(file.tell())

# seek(offset, from_where)   ->  change current position   ------------ ????????????????????????????????????????
with open('test_10.txt', 'r') as file:
    lines = file.read(2)
    print(lines)
    current_posision = file.tell()
    file.seek(0, current_posision)
    lines = file.read(3)
    print(lines)


# АТРИБУТЫ
# close -> true if file is close, false if open
# encoding
# mode
# name
# newlines
##### softspace
with open('test_10.txt', 'r') as file:
    print(file.closed)
    print(file.encoding)
    print(file.mode)
    print(file.name)
    print(file.newlines)


# rename and remove
from os import rename, remove
import os

# rename('test_10.txt', 'test_10_10.txt')
directoris = os.listdir()
print(directoris)
director = os.scandir()

from pathlib import Path
directs = Path()
for dir in directs.iterdir():
    print(dir.name)

print()
print()

# JSON

data = {
    'first_name': 'Olya',
    'last_name': 'Melnyk',
    'age': 35,
    'hobbits': ['running', 'singin'],
    'carrier': {
        'place': 'company name'
    }
}

import json
# serialing            # запись
# deserialing

# dict  -> object {}
# list, tuple -> array []
# str  -> string
# int, float - > number
# True/False  -> true/false
# None -> null

with open('demo_json.json', 'w') as writerr:
    json.dump(data, writerr)      # запись строки
    json_str = json.dumps(data)   # просто берет строку, без записи
    print(json_str)

with open('demo_json.json', 'w') as writerr:
    json.dump(data, writerr, indent=4)    # indent=4 - отступ

#  object {}  -> dict
# array [] -> list, tuple
# string  -> str
# number  ->  int, float - >
# true/false   -> True/False

# load()                  # считывание
with open('demo_json.json', 'r') as rearerr:
    dat = json.load(rearerr)      # считывание
    print(dat)

# если строка вида: {"first_name": "Olya", "last_name": "Melnyk", "age": 35, "carrier": {"place": "company name"}}
data = json.loads('{"first_name": "Olya", "last_name": "Melnyk", "age": 35, "carrier": {"place": "company name"}}')
print(data)
print(data['last_name'])


# task перезапись файл с сортировкой строк по длинне
def reader(file_name):
    file  = open(file_name, 'r')
    lines = file.readlines()
    lines = sorted(lines, key=len)
    file.close()
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line)

reader('test_10.txt')


# task созд словарь и запись в json
import json

json_string = [
    {
        'name': 'ivan',
        'age': 40
    },
    {
        'name': 'Olena',
        'age': 35
    },
    {
        'name': 'Maryna',
        'age': 25
    }
]
with open('names_json.json', 'w') as file:
    json.dump(json_string, file, indent=4)

with open('names_json.json', 'r') as file:
    data = json.load(file)
    for i in data:
        print(i['name'], i['age'])