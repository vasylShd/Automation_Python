import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from ..pages.dashboards_page import PrimeDashboard

service = Service('chromedriver/chromedriver')

@pytest.fixture(scope='session')
def prime_driver():
    driver = Chrome(service=service)
    try:
        driver.maximize_window()
        driver.get('https://dok.ua/ua/')
        yield driver

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


@pytest.fixture
def prime_dashboard(prime_driver):
    yield PrimeDashboard(prime_driver)