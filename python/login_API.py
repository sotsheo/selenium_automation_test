import requests

class TestLoginApi():

    def __init__(self):
        self.url = "https://crm-new-dev.mvno.help/api/mypage_login"

        self.payloadError = {
            'username': 'testuser',
            'password': 'password'
        }
        self.payloadSuccess = {
            'oem_cd': 'LEQ001',
            'loginId': 'thanh96',
            'password': 'Thanhnb09',
            'loginIp': '127.0.0.1'
        }
        self.payloadErrorOem = {
            'oem_cd': 'LEQ002',
            'loginId': 'thanh1',
            'password': 'Thanhnb09',
            'loginIp': '127.0.0.1'
        }
        self.payloadAcount = {
            'oem_cd': 'LEQ002',
            'loginId': 'thanh',
            'password': 'Thanhnb09',
            'loginIp': '127.0.0.1'
        }

        self.payloadErrorProgress = {
            'oem_cd': 'LEQ001',
            'loginId': 'thanh1',
            'password': 'Thanhnb09',
            'loginIp': '127.0.0.1'
        }
    
    def handler_test(self):
        print("--- Loi khong du thong tin---")
        result = self.test_api_login(self.payloadError)
        self.test_status(400, result, True , 'errorMsg', '予期せぬエラーが発生しました。お手数ですが、サポートセンター（$OEMのCSリンク）へご連絡ください。')

        print("\n--- Loi sai tai khoan---")
        result = self.test_api_login(self.payloadAcount)
        self.test_status(200, result, True, 'errorMsg', 'ログインに失敗した場合に表示')   

        print("\n--- Loi khong dung oem cd---")
        result = self.test_api_login(self.payloadErrorOem)
        self.test_status(200, result, True, 'errorMsg', '予期せぬエラーが発生しました。お手数ですが、サポートセンター（$OEMのCSリンク）へご連絡ください。') 

        print("\n--- Loi khong dung progress ---")
        result = self.test_api_login(self.payloadErrorProgress)
        self.test_status(200, result, True, 'errorMsg', 'マイページが利用可能になるまで、暫くお待ちください。')   

        print("\n--- Thanh cong ---")
        result = self.test_api_login(self.payloadSuccess)
        self.test_status(200, result, False)   
        # result = self.test_api_login(self.payloadSuccess)
        # self.test_status(200, result, False, 'errorMsg', 'ログインに失敗した場合に表示')
        # self.check_json_structure(result.json())

    def test_api_login(self, payload):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        return requests.post(self.url, data=payload, headers=headers)
    
    def test_status(self, status, response, compareMessage, errorName = 'message', errorText = ''):
        if response.status_code == status:
            print(f"Status: {status}")
            if compareMessage:
                self.test_text(errorName, errorText, response)
        else:
            print(f"Status: {response.status_code} mong muon: {status}")
            print(f"Response JSON: {response.json()}")

    def test_text(self, messageName, messageText, response):
        if response.json()[messageName] == messageText:
            print(f"Thong tin {messageName} tra ve: {messageText}")
        else:
            print(f"Thong tin {messageName} error  Content: {response.json()}")
    
    def check_json_structure(self, response_json):
        # Kiểm tra xem có trường 'status' và 'data' không
        if 'status' in response_json and 'data' in response_json:
            print("Trường 'status' và 'data' có trong phản hồi.")
            
            # Kiểm tra kiểu dữ liệu của các trường
            if isinstance(response_json['status'], str) and isinstance(response_json['data'], dict):
                print("Cấu trúc JSON hợp lệ!")
                
                # Kiểm tra thêm các trường trong 'data'
                if 'user_id' in response_json['data'] and 'username' in response_json['data']:
                    print("Các trường 'user_id' và 'username' có trong 'data'.")
                    
                    # Kiểm tra kiểu dữ liệu của 'user_id' và 'username'
                    if isinstance(response_json['data']['user_id'], int) and isinstance(response_json['data']['username'], str):
                        print("Dữ liệu của 'user_id' và 'username' hợp lệ!")
                    else:
                        print("Kiểu dữ liệu của 'user_id' hoặc 'username' không hợp lệ.")
                else:
                    print("Thiếu trường 'user_id' hoặc 'username' trong 'data'.")
            else:
                print("Kiểu dữ liệu của 'status' hoặc 'data' không hợp lệ.")
        else:
            print("Thiếu trường 'status' hoặc 'data' trong phản hồi.")

test_login = TestLoginApi()
test_login.handler_test()