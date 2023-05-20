from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import By
from .base_page import BasePage, Cookies, LocalStorage
from ..core.locator import Locator
from ..locator.dashboard_locators import DashBoardLocatorColection
from ..pages.subcategories_maintenance_parts import SubCategoryPickPage
import time


class PrimeDashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__main_car_object = DashBoardLocatorColection()

    def try_registration_by_phone_numb(self, phone_numb):
        registration_form = self.__main_car_object.try_registration[0]
        self._click(Locator(By.XPATH, registration_form))
        time.sleep(5)
        input_phone = self._wait_until_element_appears(Locator(By.XPATH, self.__main_car_object.try_registration[1]))
        input_phone.clear()
        input_phone.send_keys(phone_numb)
        cancel = self.__main_car_object.try_registration[2]
        self._click(Locator(By.XPATH, cancel))


    def move_to_main_page(self):
        self._click(Locator(By.XPATH, self.__main_car_object.main_page))


    def choice_category(self, name):
        self.__main_car_object.select_category = name
        self._click(Locator(By.XPATH, self.__main_car_object.select_category))
        return SubCategoryPickPage(self._driver)


    def garage_clearing(self):
        try:
            self._click(Locator(By.XPATH, self.__main_car_object.garage_locators[0]))
            self._click(Locator(By.XPATH, self.__main_car_object.garage_locators[1]))
        except:
            pass

    def car_select(self, **kwargs):
        self.__main_car_object.car_parameters = kwargs
        car_parameters_list = self.__main_car_object.car_parameters
        for parameter in car_parameters_list:
            try:
                self._click(Locator(By.XPATH, parameter))
            except:
                pass

    def set_my_location(self, city):
        self.__main_car_object.my_location = city
        self._click(Locator(By.XPATH, self.__main_car_object.my_location[0]))
        self._click(Locator(By.XPATH, self.__main_car_object.my_location[1]))

    def input_data_in_search_field(self, element):
        self.__main_car_object.search_element = element
        search_field = self._wait_until_element_appears(Locator(By.XPATH, self.__main_car_object.search_element[0]))
        search_field.send_keys(element)
        self._click(Locator(By.XPATH, self.__main_car_object.search_element[1]))


    def input_min_max_price(self, min_price, max_price):
        input_price_min = self._wait_until_element_appears(Locator(By.XPATH, self.__main_car_object.set_price[0]))
        input_price_min.clear()
        input_price_min.send_keys(min_price)
        input_price_max = self._wait_until_element_appears(Locator(By.XPATH, self.__main_car_object.set_price[1]))
        input_price_max.clear()
        input_price_max.send_keys(max_price)
        self._click(Locator(By.XPATH, self.__main_car_object.set_price[2]))

    def manufacturers_choice(self, manufacturer):
        self.__main_car_object.manufacturers = manufacturer
        self._click(Locator(By.XPATH, self.__main_car_object.manufacturers))

    def pagination(self, page_numb):
        self.__main_car_object.pagination = page_numb
        try:
            self._click(Locator(By.XPATH, self.__main_car_object.pagination))
        except:
            print(' PageNumbError - There are fewer pages for this product than requested!')

    def add_product_to_cart(self):
        select_product_1 = self.__main_car_object.add_product_to_cart[1]
        self._click(Locator(By.XPATH, select_product_1))
        buy_button = self.__main_car_object.add_product_to_cart[0]
        time.sleep(2)
        self._click(Locator(By.XPATH, buy_button))
        time.sleep(5)
        self._click(Locator(By.XPATH, self.__main_car_object.cart_open_close[1]))

    def cart_check(self):
        try:
            self._click(Locator(By.XPATH, self.__main_car_object.cart_open_close[0]))
            time.sleep(5)
            self._click(Locator(By.XPATH, self.__main_car_object.cart_open_close[1]))
        except:
            pass

class CookiesGet(Cookies):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def cookies_get(self):
        cookies = self.driver.get_cookies()
        return cookies

class LocalStorageGet(LocalStorage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def local_storage_get(self):
        arguments = self.driver.execute_script("return Object.keys(window.localStorage);")
        return arguments

