import random

from fake_useragent import UserAgent
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service


# обрабатываемая страница
# url = "https://www.vk.com/"

user_agents_list = [
    "terminator",
    "mad max",
    "rus"
]

useragent = UserAgent()

# опции
options = webdriver.ChromeOptions()              # создать объект опций
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 "
#                      "(KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")    #  случайно из списка выхватывать
options.add_argument(f"user-agent={useragent.opera}")    # подставляем любой браузер,   можно  .opera или .random

# options.set_preference("general.useragent.override", useragent.random)   # строчка для firefox



# путь к файлу драйвера
s = Service("D:\\pythonProject\\selenium_learning\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)             # создаём экземпляр класса Webdriver
                                                                 # переменная driver - условный браузер, который мы будем настраивать и
                                                                 # передавать команды
try:                        # в try будем писать запросы
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    time.sleep(5)
    # driver.refresh()       # Обновляет окно браузера.
    # driver.get(url=url)
    # time.sleep(5)
    # driver.get_screenshot_as_file("1.png")    # сделать скриншот окна браузера
    # driver.save_screenshot("2.png")

except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


