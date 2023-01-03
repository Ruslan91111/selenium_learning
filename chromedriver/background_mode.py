"""
Код для работы браузера в фоновом режиме, то есть без открытия окна браузера
"""
import pickle

import win32api
import win32con
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from vk_auth_data import vk_login, vk_password


# создать объект опций запуска через Chrome
options = webdriver.ChromeOptions()
# request headers
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")
# отключение режима WebDriver
options.add_argument("--disable-blink-features=AutomationControlled")
# работа в фоновом режиме
options.add_argument("--headless")
# второй вариант работы в фоновом режиме
# options.headless = True

# создаём экземпляр класса Webdriver - переменная driver - условный браузер.
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get("https://vk.com/")
    print("Opened page")
    time.sleep(5)
    driver.refresh()
    print("refreshed the page")
    time.sleep(5)

except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


