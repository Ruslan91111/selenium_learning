from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

from vk_auth_data import vk_login, vk_password


options = webdriver.ChromeOptions()              # создать объект опций запуска через Chrome

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")


s = Service("chromedriver.exe")                                  # путь к файлу-драйверу
driver = webdriver.Chrome(service=s, options=options)            # создаём экземпляр класса Webdriver
                                                                 # переменная driver - условный браузер, который мы будем настраивать и
                                                                 # передавать команды
# в try будем писать запросы
try:
    driver.get("https://vk.com/")
    time.sleep(5)

    login_input = driver.find_element("id", "index_element")
    login_input.clear()
    login_input.send_keys(vk_login)
    time.sleep(3)
    login_input.send_keys(Keys.ENTER)



    # driver.refresh()       # Обновляет окно браузера.
    # driver.get(url=url)
    # time.sleep(5)
    # driver.get_screenshot_as_file("1.png")    # сделать скриншот окна браузера
    # driver.save_screenshot("2.png")

    time.sleep(5)
except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


