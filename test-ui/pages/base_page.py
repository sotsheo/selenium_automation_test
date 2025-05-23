"""
BasePage: Class cha cho các Page Object, chứa hàm chung.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Config.BASE_URL

    def get_field_error_messages(self, timeout=5):
        """
        Lấy tất cả text lỗi từ các element có class 'error-message' (validate required).
        """
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )
        except Exception:
            return []
        elems = self.driver.find_elements(By.CLASS_NAME, "error-message")
        return [e.text for e in elems if e.text.strip()]

    def open(self, url_path=""):
        self.driver.get(self.base_url + url_path)

    def find_element(self, locator, timeout=Config.TIMEOUT):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Không tìm thấy element: {locator}")

    def click(self, locator):
        elem = self.find_element(locator)
        elem.click()

    def input_text(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        elem = self.find_element(locator)
        return elem.text
