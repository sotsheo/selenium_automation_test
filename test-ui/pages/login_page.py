"""
Page Object cho màn hình Login
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".Toastify__toast-body")  # Selector cho Toastify
    FIELD_ERROR_MESSAGES = (By.CLASS_NAME, "error-message")  # Cho validate required

    def open_login(self):
        self.open("/")

    def login(self, email, password):
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self, timeout=15):
        """
        Lấy nội dung lỗi từ Toastify, chờ tối đa 15s nếu cần.
        """
        try:
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return elem.text
        except Exception:
            return ""
