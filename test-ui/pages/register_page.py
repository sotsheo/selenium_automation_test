"""
Page Object cho màn hình Register
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegisterPage(BasePage):
    NAME_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "password")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.NAME, "phone")
    CMND_INPUT = (By.NAME, "cmnd")
    ADDRESS_INPUT = (By.NAME, "address")
    PROVINCE_SELECT = (By.NAME, "province_id")
    DISTRICT_SELECT = (By.NAME, "district_id")
    WARD_SELECT = (By.NAME, "ward_id")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".Toastify__toast-body")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_register_form(self, name, password, email, phone, cmnd, address, province_id, district_id, ward_id):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.PASSWORD_INPUT, password)
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PHONE_INPUT, phone)
        self.input_text(self.CMND_INPUT, cmnd)
        self.input_text(self.ADDRESS_INPUT, address)
        self.select_by_value(self.PROVINCE_SELECT, province_id)
        self.select_by_value(self.DISTRICT_SELECT, district_id)
        self.select_by_value(self.WARD_SELECT, ward_id)

    def select_by_value(self, locator, value, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait, Select
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        select_elem = self.find_element(locator)
        # Chờ option xuất hiện
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(opt.get_attribute("value") == str(value) for opt in select_elem.find_elements(By.TAG_NAME, "option"))
            )
        except TimeoutException:
            raise Exception(f"Không tìm thấy option với value={value} trong select {locator}")
        select = Select(select_elem)
        select.select_by_value(str(value))

    def open_register(self):
        self.open("/register")
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        # Sau đó chờ box-loading biến mất (tối đa 5s)
        try:
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located(("css selector", ".box-loading"))
            )
        except TimeoutException:
            pass

    def register(self, name, password, email, phone, cmnd, address, province_id, district_id, ward_id, validation= False):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.PASSWORD_INPUT, password)
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PHONE_INPUT, phone)
        self.input_text(self.CMND_INPUT, cmnd)
        self.input_text(self.ADDRESS_INPUT, address)
        self.select_by_value(self.PROVINCE_SELECT, province_id)
        self.select_by_value(self.DISTRICT_SELECT, district_id)
        self.select_by_value(self.WARD_SELECT, ward_id)
        if validation:
            self.click(self.REGISTER_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
