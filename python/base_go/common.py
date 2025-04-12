# common.py
import requests

class CommonTestMethods:
    @staticmethod
    def test_status(status, response, compare_message, error_name='message', error_text=''):
        if response.status_code == status:
            print(f"---- Status: {status}")
            if compare_message:
                CommonTestMethods.test_text(error_name, error_text, response)
        else:
            print(f"--- Status: {response.status_code} mong muon: {status}")
            print(f"--- Response JSON: {response.json()}")

    @staticmethod
    def test_text(message_name, message_text, response):
        if response.json()[message_name] == message_text:
            print(f"--- Thong tin {message_name} tra ve: {message_text}")
        else:
            print(f"--- Thong tin {message_name} error  Content: {response.json()}")

    @staticmethod
    def check_data_json_structure(expected, actual):
        
        if expected == actual:
            print("\033[94m---- Thông tin chính xác \033[0m")
        else:
            print("\033[31m---- Thông tin KHÔNG chính xác \033[0m")
            print("------ Expected:", expected)
            print("------ Actual:  ", actual)
    def check_json_structure(expected_structure, actual_response):
        """
        Kiểm tra cấu trúc JSON response có khớp với expected structure không
        Không kiểm tra giá trị bên trong, chỉ kiểm tra sự tồn tại của các key
        """
        def get_structure(data):
            if isinstance(data, dict):
                return {key: get_structure(value) for key, value in data.items()}
            elif isinstance(data, list):
                return [get_structure(item) for item in data] if data else []
            else:
                return type(data).__name__
        
        expected_struct = get_structure(expected_structure)
        actual_struct = get_structure(actual_response)
        
        if expected_struct == actual_struct:
            print("\033[94m---- Cấu trúc JSON chính xác \033[0m")
            return True
        else:
            print("\033[31m---- Cấu trúc JSON KHÔNG chính xác \033[0m")
            print("------ Expected structure:", expected_struct)
            print("------ Actual structure:", actual_struct)
            return False
    @staticmethod
    def make_api_request(url, payload, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        return requests.post(url, data=payload, headers=headers)