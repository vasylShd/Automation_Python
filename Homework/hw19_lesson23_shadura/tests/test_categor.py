import time


def test_part_type(dash):
    dash.select_car_manufacture_year()
    dash.input_data_in_search_field('Гальмівні колодки', '//div[@class="search-wrap opened"]/ul[1]/li/a')
    time.sleep(5)
    dash.input_data_in_search_field('Моторні оливи', '//div[@class="search-wrap opened"]/ul//a[text()="Моторні оливи "]')
    time.sleep(5)