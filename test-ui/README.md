# Selenium UI Automation Test Project

## Mục tiêu
Dự án kiểm thử tự động UI cho các màn hình Login và Register bằng Selenium, theo mô hình Page Object, sử dụng Pytest.

## Cấu trúc dự án

```
selenium_ui_test/
├── data/
│   ├── login_test_data.json
│   └── register_test_data.json
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── register_page.py
├── reports/
├── tests/
│   ├── test_login.py
│   └── test_register.py
├── utils/
│   ├── config.py
│   ├── driver_factory.py
│   └── logger.py
├── requirements.txt
└── README.md
```

## Hướng dẫn cài đặt

1. **Cài đặt Python >= 3.8**
2. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Chỉnh sửa file `utils/config.py` nếu muốn thay đổi cấu hình browser hoặc đường dẫn base_url.**

## Chạy test

- Chạy toàn bộ test và sinh báo cáo HTML:
  ```bash
  pytest --html=reports/report.html --self-contained-html
  ```
  ```bash
  pytest tests/test_register.py --html=reports/report.html --self-contained-html
  ```
- Xem log trong `reports/test.log`.

## Ghi chú
- Có thể thay đổi browser (Chrome/Firefox) trong file `utils/config.py`.
- Dữ liệu test nằm trong thư mục `data/`.
- Kết quả test và log sẽ lưu trong thư mục `reports/`.

## Liên hệ
- Tác giả: Thanhnv
- Email: thanhnv.k59cntt@gmail.com
