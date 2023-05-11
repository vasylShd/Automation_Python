from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import By
from .base_pag import BasePage


class Dash(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__driver = driver
        self.__input_search_field_locator = '// *[ @ id = "search_with-hints"]'

    def restart_select_car(self):
        garage = '//div[@class="garage-topline-car"]/i[@class="garage-topline-car__icon"]'
        self._wait_until_element_appears((By.XPATH, garage)).click()
        garage_clear = '//div[@class="garage-box-item"]/a[@class="garage-box-car__delete"]'
        self._wait_until_element_appears((By.XPATH, garage_clear)).click()

    # def car_select(self, brand=None, model=None, manufacture_year=None, body=None, engine=None, modification=None):
    def car_select(self, **kwargs):
        # car_brand = f'//div[@class="fva__table fva__table_visible" and @data-type="marka"]//div[contains(text(), "{brand}")]'
        # car_model = f'//div[@class="fva__table fva__table_visible" and @data-type="model"]//div[contains(text(), "{model}")]'
        # car_manufacture_year = f'//div[@class="fva__table fva__table_visible"]//div[contains(text(), "{manufacture_year}")]'
        # car_body = f'//div[@class="fva__table fva__table_visible" and @data-type="body"]//div[contains(text(), "{body}")]'
        # engine_type = f'//div[@class="fva__table fva__table_visible" and @data-type="engine"]//div[contains(text(), "{engine}")]'
        # car_modification = f'//div[@class="fva__table fva__table_visible" and @data-type="modification"]//div[contains(text(), "{modification}")]'

        car_brand = f'//div[@class="fva__table fva__table_visible" and @data-type="marka"]//div[contains(text(), ' \
                    f'"{kwargs["brand"]}")]'
        car_model = f'//div[@class="fva__table fva__table_visible" and @data-type="model"]//div[contains(text(), ' \
                    f'"{kwargs["model"]}")]'
        car_manufacture_year = f'//div[@class="fva__table fva__table_visible"]//div[contains(text(), ' \
                               f'"{kwargs["manufacture_year"]}")]'
        car_body = f'//div[@class="fva__table fva__table_visible" and @data-type="body"]//div[contains(text(), ' \
                   f'"{kwargs["body"]}")]'
        engine_type = f'//div[@class="fva__table fva__table_visible" and @data-type="engine"]//div[contains(text(), ' \
                      f'"{kwargs["engine"]}")]'
        car_modification = f'//div[@class="fva__table fva__table_visible" and @data-type="modification"]//div[contains(text(), ' \
                           f'"{kwargs["modification"]}")]'

        list_param = [car_brand, car_model, car_manufacture_year, car_body, engine_type, car_modification]
        for i in list_param:
            try:
                self._wait_until_element_appears((By.XPATH, i)).click()
            except:
                pass

    def set_my_location(self, city):
        location_point = '//div[@id="customer-city-header"]/span'
        set_location_point = self._wait_until_element_appears((By.XPATH, location_point)).click()
        location = f'//ul[@class="main-cities-list"]/li[@data-city-name="{city}"]'
        set_location = self._wait_until_element_appears((By.XPATH, location)).click()

    # def select_car_manufacture_year(self, year):
    #     search_year = self._wait_until_element_appears((By.XPATH, f'//div[@class="fva__table fva__table_visible"]//div[contains(text(), "{year}")]')).click()

    def input_data_in_search_field(self, name, select_name):
        element = self._wait_until_element_appears((By.XPATH, self.__input_search_field_locator))
        element.send_keys(f'{name}')
        select_element = self._wait_until_element_appears((By.XPATH, select_name)).click()

    def input_min_max_price(self, min_price, max_price):
        price_min_field = '//div[@class="filter__list"]/div/input[@class="from"]'
        price_max_field = '//div[@class="filter__list"]/div/input[@class="to"]'
        button_ok = '//div[@class="filter__list"]/div/input[@class="ok"]'
        input_price_min = self._wait_until_element_appears((By.XPATH, price_min_field))
        input_price_min.clear()
        input_price_min.send_keys(min_price)
        input_price_max = self._wait_until_element_appears((By.XPATH, price_max_field))
        input_price_max.clear()
        input_price_max.send_keys(max_price)
        press_ok = self._wait_until_element_appears((By.XPATH, button_ok)).click()

    def manufacturers_choice(self, manufacturer):
        manufacturers_check_box = f'//label[@class="filter-label"]/span[contains(text(), "{manufacturer}")]'
        select_manufacturer = self.__driver.find_element(By.XPATH, manufacturers_check_box).click()

    def pagination(self, page_numb):
        try:
            next_page = f'//div[@class="catalog__goods-column-pane"]/div[2]/ul/li[{page_numb}]'
            select_next_page = self._wait_until_element_appears((By.XPATH, next_page)).click()
        except:
            print(' PageNumbError - There are fewer pages for this product than requested!')
