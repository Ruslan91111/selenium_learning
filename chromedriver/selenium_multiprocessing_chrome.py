"""
Запуск нескольких браузеров с тремя разными сайтами.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from multiprocessing import Pool

# создать объект опций запуска через Chrome
options = webdriver.ChromeOptions()

# request headers, user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")
# отключение режима WebDriver
options.add_argument("--disable-blink-features=AutomationControlled")

urls_list = ["https://stackoverflow.com", "https://vk.com", "https://youtube.com"]


def get_data(url):
    try:
        s = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=options)
        driver.get(url=url)
        time.sleep(4)
        driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    # одновременное открытие трех окон браузера с тремя сайтами
    p = Pool(processes=3)
    p.map(get_data, urls_list)



