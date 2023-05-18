from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import By
from .base_page import BasePage
from ..core.locator import Locator
from ..locator.dashboard_locators import DashBoardLocatorColection
from ..pages.subcategories_maintenance_parts import SubCategoryPickPage


class PrimeDashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__main_car_object = DashBoardLocatorColection()

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
