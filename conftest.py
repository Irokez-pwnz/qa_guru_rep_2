import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.bing.com/')
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()