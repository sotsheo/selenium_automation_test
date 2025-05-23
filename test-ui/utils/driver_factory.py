"""
Khởi tạo WebDriver linh hoạt theo config.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .config import Config
import os

def get_driver():
    browser = Config.BROWSER.lower()
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception(f"Unsupported browser: {browser}")
    driver.implicitly_wait(Config.TIMEOUT)
    return driver
