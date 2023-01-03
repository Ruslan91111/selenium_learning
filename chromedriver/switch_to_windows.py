"""
Код для перекллючения между вкладками
"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# создать объект опций запуска через Chrome
options = webdriver.ChromeOptions()
# request headers
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")
# отключение режима WebDriver
options.add_argument("--disable-blink-features=AutomationControlled")
# работа в фоновом режиме
# options.headless = True

# создаём экземпляр класса Webdriver - переменная driver - условный браузер.
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get("https://www.avito.ru/moskva?q=автомобили")
    time.sleep(5)
    items = driver.find_elements(By.XPATH, '//div[@data-marker="item"]')
    items[0].click()
    time.sleep(4)
except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


