"""
Test case cho màn hình Login
"""
import pytest
import json
import os
from utils.driver_factory import get_driver
from utils.logger import setup_logger
from pages.login_page import LoginPage
from utils.config import Config

# Load test data
with open(os.path.join(Config.DATA_DIR, 'login_test_data.json'), encoding='utf-8') as f:
    login_data = json.load(f)

logger = setup_logger()

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("case", login_data)
def test_login(case, driver):
    page = LoginPage(driver)
    page.open_login()
    logger.info(f"Test login với email={case['email']}, expect_success={case['expect_success']}")
    page.login(case['email'], case['password'])
    if case.get('required_errors'):
        # Test trường hợp thiếu email/password, check lỗi required
        errors = page.get_field_error_messages()
        logger.info(f"Field errors: {errors}")
        for expected_err in case['required_errors']:
            assert expected_err in errors
    elif case['expect_success']:
        # Chờ URL chuyển sang trang đích (timeout 15s)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        try:
            WebDriverWait(driver, 15).until(
                EC.url_contains("/monthly-expenses")
            )
        except TimeoutException:
            pass  # Nếu muốn, có thể raise hoặc log lỗi chi tiết hơn
        assert "/monthly-expenses" in driver.current_url
    else:
        err = page.get_error_message()
        logger.info(f"Error msg: {err}")
        assert case['error'] in err
