from selenium import webdriver
import time

from selenium.webdriver.firefox.service import Service

# options
options = webdriver.FirefoxOptions()

# user-agent
options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

s = Service('geckodriver.exe')
driver = webdriver.Firefox(service=s, options=options)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()