import time


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

car_3 = {
        "brand": "Audi",
        "model": "Q7",
        "manufacture_year": "2015",
        "body": "позашляховик",
        "engine": "4.2 дизель",
        "modification": "None"}

def test_select_car(prime_dashboard):
    # CASE 1 - Тестування вібору авто ---------------------------------------------------------------------------------
    prime_dashboard.car_select(**car_1)                                       # вибір авто 1
    time.sleep(3)

def test_select_location(prime_dashboard):
    # CASE 2 - Тестування зміни локації проживання клієнта ------------------------------------------------------------
    time.sleep(3)
    prime_dashboard.set_my_location("Київ")                                    # вибір місцезнаходження клієнта
    time.sleep(3)

def test_select_parts_by_categories(prime_dashboard):
    # CASE 3 - Тестування вибору запчастин через вибір категорій і підкатегорій ---------------------------------------
    prime_dashboard.garage_clearing()  # очистка гаража
    time.sleep(3)
    prime_dashboard.car_select(**car_2)  # вибір авто 2
    time.sleep(5)
    pick_category = prime_dashboard.choice_category('Запчастини для ТО')       # Вибір категорії "Запчастини для ТО"
    time.sleep(5)
    pick_subcategory = pick_category.choice_maintenance_parts_section('Амортизатор') # Вибір підкатегорії "Амортизатор"
    time.sleep(5)
    pick_category = prime_dashboard.choice_category('Електрика та Освітлення') # Вибір категорії "Електрика та Освітлення"
    time.sleep(5)
    pick_subcategory = pick_category.choice_maintenance_parts_section('Генератор') # Вибір підкатегорії "Генератор"
    time.sleep(5)

def test_select_parts_by_searchfield(prime_dashboard):
    # CASE 4 - Тестування пошуку запчастин через поле пошуку, встановлення мін і макс ціни, пагінація -----------------
    prime_dashboard.garage_clearing()  # очистка гаража
    time.sleep(3)
    prime_dashboard.move_to_main_page()  # перехід на головну сторінку
    time.sleep(3)
    prime_dashboard.car_select(**car_3)                                       # вибір авто 3
    time.sleep(5)
    prime_dashboard.input_data_in_search_field('Гальмівні колодки')           # пошук запчастин "Гальмівні колодки"
    time.sleep(5)
    prime_dashboard.input_min_max_price(200, 4000)                            # вибір мін-мікс ціни (від 200 до 4000)
    time.sleep(5)
    prime_dashboard.input_data_in_search_field('Моторні оливи')               # пошук запчастин "Моторні оливи"
    time.sleep(5)
    prime_dashboard.pagination(3)                                             # перехід на іншу сторінку (№ 3)
    time.sleep(5)

def test_select_manufacturers(prime_dashboard):
    # CASE 5 - Тестування вибору виробника запчастини -----------------------------------------------------------------
    prime_dashboard.garage_clearing()  # очистка гаража
    time.sleep(3)
    prime_dashboard.move_to_main_page()  # перехід на головну сторінку
    time.sleep(3)
    prime_dashboard.car_select(**car_2)  # вибір авто 2
    time.sleep(5)
    prime_dashboard.input_data_in_search_field('Свічки запалювання')  # пошук запчастин "Свічки запалювання"
    time.sleep(5)
    prime_dashboard.pagination(2)  # негативний тест (сторінка тільки одна) - див вивід pytest (PageNumbError)
    time.sleep(5)
    prime_dashboard.manufacturers_choice("Mitsubishi")                        # вибір виробника запчастин
    time.sleep(7)
