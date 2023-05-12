import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from ..pages.dashboards import MainDashboard

service = Service('chromedriver/chromedriver')

@pytest.fixture(scope='session')
def main_driver():
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
def main_dashboard(main_driver):
    yield MainDashboard(main_driver)
