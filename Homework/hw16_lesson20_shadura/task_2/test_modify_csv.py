from .modify_csv import add_line_to_csv
from .modify_csv import del_last_line_from_csv


class TestMofify:
    def lines_counter(self):
        with open('example_for_test.csv', 'r') as file_csv:
            lines = file_csv.readlines()
            sum_lines = sum(1 for line in lines)
        return sum_lines

    def test_add_line(self):
        sum_lines_start = self.lines_counter()
        add_line_to_csv('example_for_test.csv', ['Mark,Jonson,37,Male,14040'])
        sum_lines_add = self.lines_counter()
        assert sum_lines_start + 1 == sum_lines_add

    def test_del_last_line(self):
        sum_lines_start = self.lines_counter()
        del_last_line_from_csv('example_for_test.csv')
        sum_lines_del = self.lines_counter()
        assert sum_lines_start - 1 == sum_lines_del
