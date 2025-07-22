from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


def test_valid_search(driver):
    search_field = driver.find_element(By.NAME, "q")
    search_field.send_keys('warhammer 40000 blood angels' + Keys.RETURN)
    wiki_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(., 'Blood Angels - Warhammer 40k Wiki')]")
        )
    )
    assert wiki_link.is_displayed()


def test_valid_search_2(driver):
    search_field = driver.find_element(By.NAME, "q")
    search_field.send_keys('askjdashdhajsdnkajsdajksd' + Keys.RETURN)
    result = WebDriverWait(driver, 7).until(
        EC.visibility_of_element_located((By.XPATH,
    "//h1[contains(text(),'Не удалось найти ни одного результата для')]")))
    assert result.is_displayed()


