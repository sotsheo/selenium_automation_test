"""
Test case cho màn hình Register
"""
import pytest
import json
import os
from utils.driver_factory import get_driver
from utils.logger import setup_logger
from pages.register_page import RegisterPage
from utils.config import Config

# Load test data
with open(os.path.join(Config.DATA_DIR, 'register_test_data.json'), encoding='utf-8') as f:
    register_data = json.load(f)

logger = setup_logger()

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("case", register_data)
def test_register(case, driver):
    page = RegisterPage(driver)
    page.open_register()
    logger.info(f"Test register với user={case['name']}, expect_success={case['expect_success']}")
    page.register(
        case.get('name', ''),
        case.get('password', ''),
        case.get('email', ''),
        case.get('phone', ''),
        case.get('cmnd', ''),
        case.get('address', ''),
        case.get('province_id', ''),
        case.get('district_id', ''),
        case.get('ward_id', '')
    )
    if case.get('required_errors'):
        # Kiểm tra lỗi required cho các trường
        errors = page.get_field_error_messages()
        logger.info(f"Field errors: {errors}")
        for expected_err in case['required_errors']:
            assert expected_err in errors
    elif case['expect_success']:
        msg = page.get_success_message()
        logger.info(f"Success msg: {msg}")
        assert msg and "thành công" in msg.lower()
    else:
        err = page.get_error_message()
        logger.info(f"Error msg: {err}")
        assert case.get('error', '') in err
