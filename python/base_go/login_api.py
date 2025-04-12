# test_login.py
from common import CommonTestMethods

class TestLoginApi():
    def __init__(self):
        self.url = "http://localhost:8001/api/v1/login"

        self.payloadError = {}
        self.payloadErrorExpected = {
            'errors': {
                'email': 'Email không được phép trống!',
                'password': 'Password không được phép trống!'
            },
            'message': 'Tài khoản hoặc mật khẩu không được trống!'
        }
        self.payloadErrorEmailFormat = {
            'email': 'thanhnv'
        }
        self.payloadErrorEmailFormatExpected = {
            'errors': {
                'email': 'Email không đúng định dạng!',
                'password': 'Password không được phép trống!'
            },
            'message': 'Tài khoản hoặc mật khẩu không được trống!'
        }
    
        self.payloadEmailFormat = {
            'email': 'thanhnv@gmail.com'
        }
        self.payloadEmailFormatExpected = {
            'errors': {
                'password': 'Password không được phép trống!'
            },
            'message': 'Tài khoản hoặc mật khẩu không được trống!'
        }
        self.payloadErrorAccount = {
            'email': 'thanhnv@gmail1.com',
            'password': 'thanhnv@gmail.com'
        }
        self.payloadErrorAccountExpected = {
            'errors': 'Tài khoản hoặc mật khẩu không chính xác!',
            'message': 'Tài khoản hoặc mật khẩu không chính xác!',
        }
        self.payloadErrorAccountStatus = {
            'email': 'thanhnv@gmail.com',
            'password': 'thanhnv@gmail.com'
        }
        self.payloadErrorAccountStatusExpected = {
            'errors': 'Tài khoản của bạn chưa được xác thực!',
            'message': 'Tài khoản của bạn chưa được xác thực!',
        }
        self.payloadSuccess = {
            'email': 'date@gmail.com',
            'password': 'thanhnv@gmail.com'
        }
        self.payloadSuccessExpected = {
            'data': "",
            'message': ""
        }
    
    def handler_test(self):
        print("--- Không chuyền đầu vào ---")
        self.login(self.payloadError, 422, 'Tài khoản hoặc mật khẩu không được trống!', self.payloadErrorExpected)

        print("\n--- Lôi email không đúng định dạng và password không chuyền ---")
        self.login(self.payloadErrorEmailFormat, 422, 'Tài khoản hoặc mật khẩu không được trống!', self.payloadErrorEmailFormatExpected)
        
        print("\n--- Lỗi mât khẩu không chuyền ---")
        self.login(self.payloadEmailFormat, 422, 'Tài khoản hoặc mật khẩu không được trống!', self.payloadEmailFormatExpected)
        
        print("\n--- Đăng nhập không đúng tài khoản ---")
        self.login(self.payloadErrorAccount, 402, 'Tài khoản hoặc mật khẩu không chính xác!', self.payloadErrorAccountExpected)
        
        print("\n--- Tài khoản của bạn chưa được xác thực! ---")
        self.login(self.payloadErrorAccountStatus, 402, 'Tài khoản của bạn chưa được xác thực!', self.payloadErrorAccountStatusExpected)
        
        print("\n--- Đăng nhập thành công! ---")
        self.login(self.payloadSuccess, 200, 'Đăng nhập thành công!', self.payloadSuccessExpected, False)
        
    def login(self, payload, status, message, expected, data = True):
        result = CommonTestMethods.make_api_request(self.url, payload)
        CommonTestMethods.test_status(status, result, True, 'message', message)
        if (data):
            CommonTestMethods.check_data_json_structure(expected, result.json())
        else:
            print(1)
            CommonTestMethods.check_json_structure(expected, result.json())
        

test_login = TestLoginApi()
test_login.handler_test()