from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service


# обрабатываемая страница
url = "https://www.vk.com/"

# путь к файлу драйвера
s = Service("D:\\pythonProject\\selenium_learning\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)             # создаём экземпляр класса Webdriver
                                                 # переменная driver - условный браузер, который мы будем настраивать и
                                                 # передавать команды
try:                        # в try будем писать запросы
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


