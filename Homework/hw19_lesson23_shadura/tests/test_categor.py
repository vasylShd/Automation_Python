import time


def test_part_type(dash):
    car_1 = {
        "brand": "Ford", "model": "Transit", "manufacture_year": "2012", "body": "фургон", "engine": "1.5 дизель",
        "modification": None}
    car_2 = {
        "brand": "Tesla", "model": "Model X", "manufacture_year": "2017", "body": None, "engine": None,
        "modification": "P100D AWD 772 к.с."}
    car_3 = {
        "brand": "Mitsubishi", "model": "ASX", "manufacture_year": "2017", "body": "позашляховик",
        "engine": "1.6 бензин", "modification": "1.6 MIVEC 117 к.с."}
    dash.car_select(**car_1)
    time.sleep(5)
    dash.restart_select_car()
    time.sleep(5)
    dash.car_select(**car_2)
    time.sleep(5)
    dash.restart_select_car()
    time.sleep(5)
    dash.car_select(**car_3)
    time.sleep(5)
    dash.set_my_location("Київ")
    time.sleep(5)
    dash.input_data_in_search_field('Гальмівні колодки',
                                    '//div[@class="search-wrap opened"]/ul//a[text()="Гальмівні колодки"]')
    time.sleep(5)
    dash.input_min_max_price(200, 4000)
    time.sleep(5)
    dash.input_data_in_search_field('Моторні оливи',
                                    '//div[@class="search-wrap opened"]/ul//a[text()="Моторні оливи "]')
    time.sleep(5)
    dash.pagination(3)
    time.sleep(5)
    dash.input_data_in_search_field('Свічки запалювання',
                                    '//div[@class="search-wrap opened"]/ul//a[text()="Свічки запалювання "]')
    time.sleep(5)
    dash.pagination(2)  # negative test, see pytest output (PageNumbError)
    time.sleep(5)
    dash.manufacturers_choice("Mitsubishi ")
    time.sleep(5)
