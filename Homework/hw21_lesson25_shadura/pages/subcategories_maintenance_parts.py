from selenium.webdriver.support.select import By
from ..pages.base_page import BasePage
from ..core.locator import Locator
from ..locator.dashboard_locators import DashBoardLocatorColection
from ..pages.jump_to_subcategiry import JumpToSubCategory

class SubCategoryPickPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__add_car_object = DashBoardLocatorColection()

    def choice_maintenance_parts_section(self, subcategory):
        self.__add_car_object.select_subcategory = subcategory
        self._click(Locator(By.XPATH, self.__add_car_object.select_subcategory))
        return JumpToSubCategory(self._driver)



