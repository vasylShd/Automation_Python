
class DashBoardLocatorColection():
    def __init__(self):
        self.__select_category = None
        self.__select_subcategory = None
        self.__car_parameters = None
        self.__my_location = None
        self.__search_element = None
        self.__pagination = None
        self.__manufacturers = None
        self.__main_page = '//header[@class="header"]//a[@class="header__logo"]'
        self.__garage = '//div[@class="garage-topline-car"]/i[@class="garage-topline-car__icon"]'
        self.__garage_clear = '//div[@class="garage-box-item"]/a[@class="garage-box-car__delete"]'
        self.__price_min_field = '//div[@class="filter__list"]/div/input[@class="from"]'
        self.__price_max_field = '//div[@class="filter__list"]/div/input[@class="to"]'
        self.__button_ok = '//div[@class="filter__list"]/div/input[@class="ok"]'

    @property
    def main_page(self):
        return self.__main_page

    @property
    def select_category(self):
        return f'//div[@class="menu__box complite"]//ul[@class="menu-list"]//a[contains(text(), "{self.__select_category}")]'

    @select_category.setter
    def select_category(self, new_category):
        self.__select_category = new_category


    @property
    def select_subcategory(self):
        return f'//div[@class="rubric"]//a[contains(text(), "{self.__select_subcategory}")]'

    @select_subcategory.setter
    def select_subcategory(self, new_subcategory):
        self.__select_subcategory = new_subcategory


    @property
    def garage_locators(self):
        return self.__garage, self.__garage_clear


    @property
    def car_parameters(self):
        car_brand = f'//div[@class="fva__table fva__table_visible" and @data-type="marka"]//div[contains(text(), ' \
                    f'"{self.__car_parameters["brand"]}")]'
        car_model = f'//div[@class="fva__table fva__table_visible" and @data-type="model"]//div[contains(text(), ' \
                    f'"{self.__car_parameters["model"]}")]'
        car_manufacture_year = f'//div[@class="fva__table fva__table_visible"]//div[contains(text(), ' \
                               f'"{self.__car_parameters["manufacture_year"]}")]'
        car_body = f'//div[@class="fva__table fva__table_visible" and @data-type="body"]//div[contains(text(), ' \
                   f'"{self.__car_parameters["body"]}")]'
        engine_type = f'//div[@class="fva__table fva__table_visible" and @data-type="engine"]//div[contains(text(), ' \
                      f'"{self.__car_parameters["engine"]}")]'
        car_modification = f'//div[@class="fva__table fva__table_visible" and @data-type="modification"]//div[contains(text(), ' \
                           f'"{self.__car_parameters["modification"]}")]'
        list_car_parameters = [car_brand, car_model, car_manufacture_year, car_body, engine_type, car_modification]
        return list_car_parameters

    @car_parameters.setter
    def car_parameters(self, new_parameters):
        self.__car_parameters = new_parameters


    @property
    def my_location(self):
        location_point = '//div[@id="customer-city-header"]/span'
        my_location = f'//ul[@class="main-cities-list"]/li[@data-city-name="{self.__my_location}"]'
        return location_point, my_location

    @my_location.setter
    def my_location(self, new_location):
        self.__my_location = new_location


    @property
    def search_element(self):
        search_field_locator = '// *[ @ id = "search_with-hints"]'
        input_search_element = f'//div[@class="search-wrap opened"]/ul//a[contains(text(), "{self.__search_element}")]'
        return search_field_locator, input_search_element

    @search_element.setter
    def search_element(self, new_element):
        self.__search_element = new_element


    @property
    def set_price(self):
        return self.__price_min_field, self.__price_max_field, self.__button_ok


    @property
    def pagination(self):
        return f'//div[@class="catalog__goods-column-pane"]/div[2]/ul/li[{self.__pagination}]'

    @pagination.setter
    def pagination(self, page_numb):
        self.__pagination = page_numb


    @property
    def manufacturers(self):
        return f'//label[@class="filter-label"]/span[contains(text(), "{self.__manufacturers}")]'

    @manufacturers.setter
    def manufacturers(self, new_manufacturer):
        self.__manufacturers = new_manufacturer



