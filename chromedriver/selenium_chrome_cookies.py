"""
В этом файле код для сохранения и подгрузки cookies при работе с сайтом VK,
Чтобы не проходить аутентификацию каждый раз, когда автоматизируем работу браузера
"""
import win32api
import win32con
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

from vk_auth_data import vk_login, vk_password
import pickle


options = webdriver.ChromeOptions()     # создать объект опций запуска через Chrome

# request headers
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")

s = Service("chromedriver.exe")                                  # путь к файлу-драйверу
driver = webdriver.Chrome(service=s, options=options)            # создаём экземпляр класса Webdriver
                                                                 # переменная driver - условный браузер, который мы будем настраивать и
                                                                 # передавать команды
# в try будем писать запросы
try:
    # driver.get("https://vk.com/")
    # time.sleep(5)
    #
    # # ввод логина
    # login_input = driver.find_element(By.ID, 'index_email')
    # login_input.clear()
    # login_input.send_keys(vk_login)
    # time.sleep(1)
    # button_input = driver.find_element(By.CSS_SELECTOR, '[class="FlatButton FlatButton--primary FlatButton--size-l FlatButton--wide VkIdForm__button VkIdForm__signInButton"]')
    # button_input.click()
    # time.sleep(10)

    # ввод пароля

    # имитация клика мыши
    # def click(x, y):
    #     win32api.SetCursorPos((x, y))
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    # click(716, 677)
    # time.sleep(70)

    # password_input = driver.find_element(By.NAME, 'password')
    # password_input.clear()
    # password_input.send_keys(vk_password)
    # time.sleep(2)
    #
    # button_password = driver.find_element(By.CSS_SELECTOR, '[class="vkuiButton vkuiButton--sz-l vkuiButton--lvl-primary vkuiButton--clr-accent vkuiButton--aln-center vkuiButton--sizeY-compact vkuiButton--stretched vkuiTappable vkuiTappable--sizeX-regular vkuiTappable--hasHover vkuiTappable--hasActive vkuiTappable--mouse"]')
    # button_password.click()
    # time.sleep(5)
    #
    # news_link = driver.find_element(By.ID, "l_nwsf").click()
    # time.sleep(5)

    # cookies сохранение куки в отдельный файл
    # pickle.dump(driver.get_cookies(), open(f"{vk_login}cookies", "wb"))


    # далее закомментировать весь код загрузки cookies от try и вниз.
    driver.get("https://vk.com/")
    time.sleep(5)

    # подгружаем cookies
    for cookie in pickle.load(open(f"{vk_login}cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

    time.sleep(5)

except Exception as ex:    # перехватывать исключения
    print(ex)
finally:
    driver.close()         # обязательно закрыть, чтобы процессы не оставались открытми фоном
    driver.quit()


