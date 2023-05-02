import csv


def add_line_to_csv(file, new_str):
    with open(file, 'a', newline='') as new_file_csv:
        writer = csv.writer(new_file_csv)
        writer.writerow(new_str)

def del_last_line_from_csv(file):
    with open(file, 'r') as file_csv:
        lines = file_csv.readlines()
    with open(file, 'w') as new_csv:
        new_csv.writelines(lines[:-1])
