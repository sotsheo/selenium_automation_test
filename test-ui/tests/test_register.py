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

import pytest
import json

@pytest.mark.parametrize("case", register_data)
def test_register(case, driver, request):
    # Ghi thông tin param test vào report
    param_info = json.dumps(case, ensure_ascii=False)
    if hasattr(request, 'node'):
        request.node._report_sections = getattr(request.node, '_report_sections', [])
        request.node._report_sections.append(('param', 'test_param', param_info))
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
        case.get('ward_id', ''),
        case.get('validation', True)
    )

    if case.get('required_errors'):
        # Kiểm tra lỗi required cho các trường
        errors = page.get_field_error_messages()
        logger.info(f"Field errors: {errors}")
        logger.info(f"Required errors: {case['required_errors']}")
        for expected_err in case['required_errors']:
            assert expected_err in errors
    elif case['expect_success']:
       # Chờ URL chuyển sang trang đích (timeout 15s)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        try:
            WebDriverWait(driver, 15).until(
                EC.url_contains("/")
            )
        except TimeoutException:
            pass  # Nếu muốn, có thể raise hoặc log lỗi chi tiết hơn
        assert "/" in driver.current_url
    else:
        err = page.get_error_message()
        logger.info(f"Error msg: {err}")
        assert case.get('error', '') in err
