# task 1
import csv
import json


class JSONToCSVConverter:
    def __init__(self):
        # pass
        self.__json_data = None

    def read_json_file(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__json_data = json.load(json_file)

    def write_csv_file(self, filename):
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            count = 0
            for row in self.__json_data:
                if count == 0:
                    header = row.keys()
                    writer.writerow(header)
                    count += 1
                writer.writerow(row.values())
            self.clean_up()

    def clean_up(self):
        self.__json_data = None


converter = JSONToCSVConverter()
converter.read_json_file('example.json')
converter.write_csv_file('example.csv')
