import time


def test_parts_sites(main_dashboard):
    car_1 = {
        "brand": "Ford",
        "model": "Transit",
        "manufacture_year": "2012",
        "body": "фургон",
        "engine": "1.5 дизель",
        "modification": None}
    car_2 = {
        "brand": "Mitsubishi",
        "model": "ASX",
        "manufacture_year": "2017",
        "body": "позашляховик",
        "engine": "1.6 бензин",
        "modification": "1.6 MIVEC 117 к.с."}

    main_dashboard.car_select(**car_1)                                       # вибір авто 1
    time.sleep(5)
    main_dashboard.garage_clearing()                                         # очистка гаража
    time.sleep(5)
    main_dashboard.car_select(**car_2)                                       # вибір авто 2
    time.sleep(5)
    main_dashboard.set_my_location("Київ")                                   # вибір місцезнаходження клієнта
    time.sleep(5)
    main_dashboard.input_data_in_search_field('Гальмівні колодки')           # пошук запчастин "Гальмівні колодки"
    time.sleep(5)
    main_dashboard.input_min_max_price(200, 4000)                            # вибір мін-мікс ціни (від 200 до 4000)
    time.sleep(5)
    main_dashboard.input_data_in_search_field('Моторні оливи')               # пошук запчастин "Моторні оливи"
    time.sleep(5)
    main_dashboard.pagination(3)                                             # перехід на іншу сторінку (№ 3)
    time.sleep(5)
    main_dashboard.input_data_in_search_field('Свічки запалювання')          # пошук запчастин "Свічки запалювання"
    time.sleep(5)
    main_dashboard.pagination(2)            # негативний тест (сторінка тільки одна) - див вивід pytest (PageNumbError)
    time.sleep(5)
    main_dashboard.manufacturers_choice("Mitsubishi")                       # вибір виробника запчастин
    time.sleep(7)
