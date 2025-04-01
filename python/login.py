from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Khởi tạo ChromeDriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://mypage-new-dev.mvno.help/")  # Thay URL của bạn vào đây

    def test_login_success(self):
        # test hien thi
        # print("Test hien thi")
        time.sleep(2)
        # self.compare_title('ログイン')
        # self.is_displayed('box-login-logo', 'logo', By.CLASS_NAME) # logo
        # self.get_compare_text(By.CLASS_NAME, 'box-copyright', 'Copyright © 2025 LEQUIOS Co., Ltd. All Rights Reserved.', 'copyright') # coppy right
        # self.is_displayed('toggle-menu', 'icon menu', By.CLASS_NAME) # econ menu
        # self.is_displayed('login_id', 'input login', By.NAME)
        # self.is_displayed('password', 'input password', By.NAME)
        # self.is_displayed('btn-bg-blue', 'input submit', By.CLASS_NAME)
        # self.is_displayed('change-type-password', 'type password', By.ID)
        # # kiem tra action click
        # self.click_type_password(By.ID, "change-type-password")
        # case required 

        self.submit_login()
        time.sleep(2) 
        print("Case: Loi required all")
        self.get_compare_text(By.ID, "message-login_id", "ログインIDを入力してください。", "Loi required")
        self.get_compare_text(By.ID, "message-password", "パスワードを入力してください。", "Loi required")

        print("Case: Loi required login_id")
        self.enter_input("password", "password")
        self.submit_login()
        time.sleep(2) 
        self.get_compare_text(By.ID, "message-login_id", "ログインIDを入力してください。", "Loi required")
        self.get_compare_text(By.ID, "message-password", "", "Loi required")

        print("Case: Loi required password")
        self.enter_input("password", "")
        self.enter_input("login_id", "login_id")
        self.submit_login()
        time.sleep(2) 
        self.get_compare_text(By.ID, "message-login_id", "", "Loi required")
        self.get_compare_text(By.ID, "message-password", "パスワードを入力してください。", "Loi required")

        print("Case: Loi login no success")
        self.enter_input("password", "1231")
        self.enter_input("login_id", "login_id")
        self.submit_login()
        time.sleep(2) 
        self.get_compare_text(By.ID, "message-login_id", "", "Loi required")
        self.get_compare_text(By.ID, "message-password", "", "Loi required")
        self.get_compare_text(By.ID, "error-system-text", "ログインに失敗した場合に表示", "Loi he thong")

        # click url  password-reissue
        first_link = self.driver.find_element(By.CSS_SELECTOR, ".forgot-password a:first-child")
        first_link.click()
        self.compare_title('パスワード再発行')

        # click url  password-reissue
        self.driver.get("https://mypage-new-dev.mvno.help/")
        time.sleep(2) 
        first_link = self.driver.find_element(By.CSS_SELECTOR, ".forgot-password a:last-child")
        first_link.click()
        self.compare_title('ログインID再通知')
        # Step 4: Nhấn Enter để đăng nhập

        # Step 5: Kiểm tra thông báo lỗi nếu có
        # self.check_error_message("Đã có lỗi xảy ra.")
    
    def is_displayed(self, name, target, by): 
        try:
            logo = self.driver.find_element(by, name)  # Thay "logo" bằng ID thực tế của logo
            
            # Kiểm tra xem logo có hiển thị không
            if logo.is_displayed():
                print(f"✅ {target} hiển thị đúng.")
            else:
                print(f"❌ {target} không hiển thị.")
        except:
            print(f"❌ Không tìm thấy {target} trên trang.")

    def enter_input(self, name, value):
        input_element = self.driver.find_element(By.NAME, name)
        input_element.clear() 
        input_element.send_keys(value)

    def submit_login(self):
        password_input = self.driver.find_element(By.CLASS_NAME, "btn-bg-blue")
        password_input.send_keys(Keys.RETURN)

    def click_type_password(self, by, name):
        self.driver.find_element(by, name).click()
        typeInput = self.driver.find_element(By.ID, 'input-password').get_attribute("type")
        if typeInput == 'text':
            print("\033[94m    => Action type passsword thanh cong!\033[0m")
        else:
            print("\033[31m    => Action type passsword loi!\033[0m")
        
        self.driver.find_element(by, name).click()
        typeInput = self.driver.find_element(By.ID, 'input-password').get_attribute("type")
        if typeInput == 'password':
            print("\033[94m    => Action type passsword thanh cong!\033[0m")
        else:
            print("\033[31m    => Action type passsword loi!\033[0m")
    def compare_title(self, text):
        try:
            self.assertEqual(self.driver.title, text)
            print("\033[94m    => Thành công! Thông báo khớp title!\033[0m")
        except Exception as e:
            print(f"\033[31m    => Lỗi tra ve title: {self.driver.title} \033[0m")

    def get_compare_text(self, by, name, expected_error, case):
        error_div = self.driver.find_element(by, name)
        print(f" - Input: {case}")
        print(f"   - Ket qua mong muon: {expected_error}")
        try:
            self.assertEqual(error_div.text, expected_error)
            print("\033[94m    => Thành công! Thông báo khớp!\033[0m")
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
