import random

from fake_useragent import UserAgent
# from selenium import webdriver   привязка к логину
from seleniumwire import webdriver

import time

from selenium.webdriver.firefox.service import Service

from proxy_auth_data import login, password

# обрабатываемая страница
# url = "https://www.vk.com/"

options = webdriver.FirefoxOptions()

# изменить useragent
useragent = UserAgent()
options.set_preference("general.useragent.override", useragent.random)   # строчка для firefox

# # установить proxy
# proxy = "190.61.88.147:8080"
#
# # получаем доступ к возможностям браузера
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# # устанавливаем флаг марионетки в True
# firefox_capabilities["marionette"] = True
# # передать словарь для proxy
# firefox_capabilities["proxy"] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }
proxy_options = {                                               # seleniumwire под логин и пароль
    "proxxy": {
        f"http://{login}:{password}@190.61.88.147:8080"
    }
}
# путь к файлу драйвера
s = Service("firefox_main.py.exe")
driver = webdriver.Firefox(service=s, seleniumwire_options=proxy_options)         # создаём экземпляр класса Webdriver
                                                # переменная driver - условный браузер, который мы будем настраивать и
                                                # передавать команды

try:                        # в try будем писать запросы
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    # time.sleep(5)
    # driver.refresh()       # Обновляет окно браузера.
    # driver.get(url=url)
    # time.sleep(5)
    # driver.get_screenshot_as_file("1.png")    # сделать скриншот окна браузера
    # driver.save_screenshot("2.png")
    driver.get("https://2ip.ru")
    time.sleep(5)

except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


