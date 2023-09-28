import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

@pytest.mark.parametrize("url", ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
                                 ])
def test_add_to_basket_button_exists(browser, url):

    browser.get(url)

    is_button_exists = True
    try:
        add_to_basket_link = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
        )
    except TimeoutException:
        is_button_exists = False

    time.sleep(30)

    assert is_button_exists



