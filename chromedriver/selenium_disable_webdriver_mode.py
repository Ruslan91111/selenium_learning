"""
В этом файле код для отключения режима WebDriver.
Для того, чтобы стать более похожим на обычного пользователя
"""

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()     # создать объект опций запуска через Chrome

# request headers
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# Список опций chromium
# https://peter.sh/experiments/chromium-command-line-switches/


s = Service("chromedriver.exe")                                  # путь к файлу-драйверу
driver = webdriver.Chrome(service=s, options=options)            # создаём экземпляр класса Webdriver
                                                                 # переменная driver - условный браузер, который мы будем настраивать и
                                                                 # передавать команды
# в try будем писать запросы
try:
    # страница детекто-режима webdriver
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(25)


except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


