from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Khởi tạo ChromeDriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://shop-new-dev.mvno.help/")  # Thay URL của bạn vào đây

    def test_login_success(self):
        # case required 
        self.submit_login()
        time.sleep(2) 
        print("Case: Loi required all")
        self.get_error_input("message-agency_cd", "代理店コードを入力してください。", "Loi required")
        self.get_error_input("message-user_id", "ログインIDを入力してください。", "Loi required")
        self.get_error_input("message-password", "パスワードを入力してください。", "Loi required")

        print("Case: Loi required agency_cd")
        self.enter_input("password", "password")
        self.enter_input("user_id", "userid")
        self.submit_login()
        time.sleep(2) 
        self.get_error_input("message-agency_cd", "代理店コードを入力してください。", "Loi required")
        self.get_error_input("message-user_id", "s", "user_id Khong loi")
        self.get_error_input("message-password", "",  "password Khong loi")
        # Step 1: Nhập mã agency_cd
        # self.enter_input("agency_cd", "")
        # self.enter_input("user_id", "")
        # self.enter_user_id("admin")
        # self.enter_password("test11")
        
        # Step 4: Nhấn Enter để đăng nhập

        # Step 5: Kiểm tra thông báo lỗi nếu có
        # self.check_error_message("Đã có lỗi xảy ra.")
        
    def enter_input(self, name, value):
        agency_cd_input = self.driver.find_element(By.NAME, name)
        agency_cd_input.send_keys(value)

    def submit_login(self):
        password_input = self.driver.find_element(By.ID, "btnLogin")
        password_input.send_keys(Keys.RETURN)

    def get_error_input(self, name, expected_error, case):
        error_div = self.driver.find_element(By.ID, name)
        print(f" - Input: {case}")
        print(f"   - Ket qua mong muon: {expected_error}")
        try:
            self.assertEqual(error_div.text, expected_error)
            print("\033[94m    => Thành công! Thông báo lỗi khớp!\033[0m")
        except Exception as e:
            print(f"\033[31m    => Lỗi tra ve: {error_div.text} \033[0m")

    def check_error_message(self, expected_error_message):
        # Đợi một chút để hệ thống xử lý
        time.sleep(2)  # Thời gian đợi để lỗi hiển thị
        
        try:
            # Tìm thông báo lỗi
            error_message_div = self.driver.find_element(By.ID, "system-message")
            error_message = error_message_div.text
            # Kiểm tra thông báo lỗi có khớp không
            self.assertEqual(error_message, expected_error_message)
            print("Thông báo lỗi khớp!")
        except Exception as e:
            print(f"Lỗi: {e}")
        
    def tearDown(self):
        # Đóng trình duyệt sau khi kiểm thử
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
