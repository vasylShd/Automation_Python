from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import pytest

def test_dokUa():
    service = Service('chromedriver/chromedriver')
    driver = Chrome(service=service)
    start_page = 'https://dok.ua/ua/doc/car/12007'
    try:
        driver.get(start_page)
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)  # реалізація явного очікування

        # вибір року випуску авто
        select_manufacture_year = '//div[@class="fva__table fva__table_visible"]/div[3]/div[9]'
        wait.until(EC.element_to_be_clickable((By.XPATH, select_manufacture_year)))
        search_year = driver.find_element(By.XPATH, select_manufacture_year).click()

        # вибір поля для пошуку автозапчастини
        search_input_field_locator = '// *[ @ id = "search_with-hints"]'
        select_input_field = wait.until(EC.presence_of_element_located((By.XPATH, search_input_field_locator)))

        # ввід данних для пошуку і перехід на потрібну сторінку
        select_input_field.send_keys('Гальмівні колодки')
        selected_data = '//div[@class="search-wrap opened"]/ul[1]/li/a'
        wait.until(EC.element_to_be_clickable((By.XPATH, selected_data)))
        press_selected_data = driver.find_element(By.XPATH, selected_data).click()

        # встановлення у фільтрі мін ціни (750)
        price_min_field = '//div[@class="filter__list"]/div/input[@class="from"]'
        input_price_min = wait.until(EC.presence_of_element_located((By.XPATH, price_min_field)))
        input_price_min.clear()
        input_price_min.send_keys(750)
        time.sleep(3)
        assert input_price_min.get_attribute('value') == '750', "Error in test 1" # перевірка правильності вводу данних

        # встановлення у фільтрі макс ціни (12500)
        price_max_field = '//div[@class="filter__list"]/div/input[@class="to"]'
        input_price_max = wait.until(EC.presence_of_element_located((By.XPATH, price_max_field)))
        input_price_max.clear()
        input_price_max.send_keys(12500)

        # підтердження вибору
        button_ok = '//div[@class="filter__list"]/div/input[@class="ok"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, button_ok)))
        assert driver.find_element(By.XPATH, button_ok).is_enabled() == True, "Error in test 2" #перевірка знаходж єлем
        press_ok = driver.find_element(By.XPATH, button_ok).click()

        # пагінація. перехід на сторінку №2
        page_2 = '//div[@class="catalog__goods-column-pane"]/div[2]/ul/li[2]'
        wait.until(EC.element_to_be_clickable((By.XPATH, page_2)))
        driver.find_element(By.XPATH, page_2).click()
        time.sleep(10)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()
