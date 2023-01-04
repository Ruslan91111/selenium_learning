"""
Код для перекллючения между вкладками на сайте авито.
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
    driver.get("https://www.avito.ru/moskva?q=гантели")
    # вывести текущий url адрес
    # print(f"Currently URL is: {driver.current_url}")
    time.sleep(4)

    # найти на странице картинку для клика и последующего перехода
    items = driver.find_elements(By.XPATH, '//div[@data-marker="item"]')
    items[0].click()
    time.sleep(3)
    print(f"Currently URL is: {driver.current_url}")

    # переключиться на следующую (первую) вкладку
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    # на новой открывшейся вкладке (второй) находим продавцв
    seller_name = driver.find_element(By.XPATH, '//div[@data-marker="seller-info/label"]')
    print(f"Seller name {seller_name.text}")
    print("#" * 20)
    time.sleep(5)

    # закрываем вкладку
    driver.close()

    # переключиться на первую вкладку
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(4)

    # переключение  с первой страницы на вторую вкладку
    items[1].click()
    time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    # собрать локацию продавца
    seller_geo = driver.find_element(By.CLASS_NAME, "style-item-address__string-wt61A")
    print(f'Локация продавца: {seller_geo.text}')

    # print(driver.window_handles)
    # переключиться на следующую вкладку
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


