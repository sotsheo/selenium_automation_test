"""
Cấu hình dự án: browser, base_url, timeout...
"""
import os

class Config:
    # Browser: 'chrome' hoặc 'firefox'
    BROWSER = os.getenv('TEST_BROWSER', 'chrome')
    BASE_URL = os.getenv('BASE_URL', 'https://booking-app-kdrc.onrender.com/')
    TIMEOUT = 10
    REPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
