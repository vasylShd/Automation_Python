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


# Не завжди спрацьовує!!!
# def test_registration_on_site(prime_dashboard):
    # Тестування частини регістраціі по телефону (без підтвердження по смс)
    # prime_dashboard.try_registration_by_phone_numb('+38 (096)2894281') # після вводу номера - відміна регістраціії
    # time.sleep(5)

def test_select_car(prime_dashboard):
    # CASE 1 - Тестування вибору авто -------------------------------------------------------------------------------------
    prime_dashboard.car_select(**car_1)                                        # вибір авто 1
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
    prime_dashboard.move_to_main_page()  # перехід на головну сторінку
    time.sleep(3)
    prime_dashboard.car_select(**car_1)  # вибір авто 1
    time.sleep(5)
    pick_category = prime_dashboard.choice_category('Запчастини для ТО')       # Вибір категорії "Запчастини для ТО"
    time.sleep(5)
    pick_subcategory = pick_category.choice_maintenance_parts_section('Амортизатор') # Вибір підкатегорії "Амортизатор"
    time.sleep(5)
    pick_category = prime_dashboard.choice_category('Двигун і Система вихлопу') # Вибір категорії "Двигун і Система вихлопу"
    time.sleep(5)
    pick_subcategory = pick_category.choice_maintenance_parts_section('Повітряний фільтр') # Вибір підкатегорії "Повітряний фільтр"
    time.sleep(5)

def test_cart_filling(prime_dashboard):
    # CASE 4 - Тестування додавання впбраного товару в корзину  ----------------------------------------------------------------
    prime_dashboard.garage_clearing()                                          # очистка гаража
    time.sleep(3)
    prime_dashboard.move_to_main_page()                                        # перехід на головну сторінку
    time.sleep(3)
    prime_dashboard.car_select(**car_2)                                        # вибір авто 2
    time.sleep(5)
    pick_category = prime_dashboard.choice_category('Гальмівна система')  # Вибір категорії "Гальмівна система"
    time.sleep(5)
    pick_subcategory = pick_category.choice_maintenance_parts_section('Гальмівні колодки')  # Вибір підкатегорії "Гальмівні колодки"
    time.sleep(5)
    prime_dashboard.add_product_to_cart()
    time.sleep(5)

def test_check_cart(prime_dashboard):
    # CASE 5 - Тестування перевірки доданого товару в корзині -------------------------------------------------------------------
    prime_dashboard.cart_check()
    time.sleep(5)


def test_select_parts_by_searchfield(prime_dashboard):
    # CASE 6 - Тестування пошуку запчастин через поле пошуку, встановлення мін і макс ціни, пагінація -----------------
    prime_dashboard.garage_clearing()                                         # очистка гаража
    time.sleep(3)
    prime_dashboard.move_to_main_page()                                       # перехід на головну сторінку
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
    # CASE 7 - Тестування вибору виробника запчастини -----------------------------------------------------------------
    prime_dashboard.garage_clearing()                                         # очистка гаража
    time.sleep(3)
    prime_dashboard.move_to_main_page()                                       # перехід на головну сторінку
    time.sleep(3)
    prime_dashboard.car_select(**car_2)                                       # вибір авто 2
    time.sleep(5)
    prime_dashboard.input_data_in_search_field('Свічки запалювання')          # пошук запчастин "Свічки запалювання"
    time.sleep(5)
    prime_dashboard.pagination(2)  # негативний тест (сторінка тільки одна) - див вивід pytest (PageNumbError)
    time.sleep(5)
    prime_dashboard.manufacturers_choice("Mitsubishi")                        # вибір виробника запчастин
    time.sleep(7)

def test_coocies_get(prime_cookies):
    # CASE 8 - Вивід "cookies" --------------------------------------------------------------------------------------------------
    print('This is cookies')
    for cookie in prime_cookies.cookies_get():
        print(cookie)

def test_local_storage(prime_localstorage):
    # CASE 9 - Вивід "localstorage"  -------------------------------------------------------------------------------------------
    time.sleep(3)
    print('\nThis is localstorage')
    print(prime_localstorage.local_storage_get())



