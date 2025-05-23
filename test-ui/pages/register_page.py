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
    REGISTER_BUTTON = (By.ID, "register-btn")
    ERROR_MESSAGE = (By.ID, "register-error")
    SUCCESS_MESSAGE = (By.ID, "register-success")

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

    def select_by_value(self, locator, value):
        from selenium.webdriver.support.ui import Select
        select_elem = self.find_element(locator)
        select = Select(select_elem)
        select.select_by_value(str(value))

    def open_register(self):
        self.open("/register")
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        # Chờ box-loading xuất hiện (tối đa 3s), nếu không xuất hiện thì bỏ qua
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(("css selector", ".box-loading"))
            )
        except TimeoutException:
            pass
        # Sau đó chờ box-loading biến mất (tối đa 10s)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(("css selector", ".box-loading"))
            )
        except TimeoutException:
            pass

    def register(self, username, password, email):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.input_text(self.EMAIL_INPUT, email)
        self.click(self.REGISTER_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
