from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import By
from .base_pag import BasePage


class Dash(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__driver = driver
        self.__car_manufacture_year = '//div[@class="fva__table fva__table_visible"]/div[3]/div[9]'
        self.__input_search_field_locator = '// *[ @ id = "search_with-hints"]'

    def select_car_manufacture_year(self):
        search_year = self._wait_until_element_appears((By.XPATH, self.__car_manufacture_year)).click()
        # search_year = self.__driver.find_element(By.XPATH, self.__car_manufacture_year).click()

    def input_data_in_search_field(self, name, select_name):
        element = self._wait_until_element_appears((By.XPATH, self.__input_search_field_locator))
        element.send_keys(f'{name}')
        select_element = self._wait_until_element_appears((By.XPATH, select_name)).click()

