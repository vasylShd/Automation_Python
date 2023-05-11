import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from ..pages.dashboar import Dash

service = Service('chromedriver/chromedriver')

@pytest.fixture(scope='session')
def driv():
    driver = Chrome(service=service)
    try:
        driver.maximize_window()
        # driver.get('https://dok.ua/ua/doc/car/12007')
        driver.get('https://dok.ua/ua/')
        yield driver

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

@pytest.fixture
def dash(driv):
    yield Dash(driv)
