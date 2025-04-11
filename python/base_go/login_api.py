import requests

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
        # self.payloadErrorEmailFormatExpected = {
        #     'email': 'thanhnv'
        # }
       
    
    def handler_test(self):
        print("--- Không chuyền đầu vào ---")
        self.login(self.payloadError, 422, 'Tài khoản hoặc mật khẩu không được trống!', self.payloadErrorExpected)

        print("\n--- Email error ---")
        self.login(self.payloadErrorEmailFormat, 422, 'Tài khoản hoặc mật khẩu không được trống!', self.payloadErrorEmailFormatExpected)
        
        print("\n--- Password error empty---")
        self.login(self.payloadEmailFormat, 422, 'Tài khoản hoặc mật khẩu không được trống!', self.payloadEmailFormatExpected)
        

        # self.test_status(200, result, False, 'errorMsg', 'ログインに失敗した場合に表示')
        # self.check_json_structure(result.json())
    def login(self, payload, status,  message, expected):
        result = self.test_api_login(payload)
        self.test_status(status, result, True , 'message', message)
        self.check_json_structure(expected, result.json())

    def test_api_login(self, payload):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        return requests.post(self.url, data=payload, headers=headers)
    
    def test_status(self, status, response, compareMessage, errorName = 'message', errorText = ''):
        if response.status_code == status:
            print(f"---- Status: {status}")
            if compareMessage:
                self.test_text(errorName, errorText, response)
        else:
            print(f"--- Status: {response.status_code} mong muon: {status}")
            print(f"--- Response JSON: {response.json()}")

    def test_text(self, messageName, messageText, response):
        if response.json()[messageName] == messageText:
            print(f"--- Thong tin {messageName} tra ve: {messageText}")
        else:
            print(f"--- Thong tin {messageName} error  Content: {response.json()}")
    
    def check_json_structure(self, expected, actual):
        if expected == actual:
            print("\033[94m---- Thông tin chính xác \033[0m")
        else:
            print("\033[31m---- Thông tin KHÔNG chính xác \033[0m")
            print("------ Expected:", expected)
            print("------ Actual:  ", actual)

test_login = TestLoginApi()
test_login.handler_test()