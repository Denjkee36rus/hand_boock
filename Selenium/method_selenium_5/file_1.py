import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/methods/1/index.html"
with webdriver.Chrome() as browser:
    browser.get(url)
    flag = False
    while not flag:
        browser.refresh()
        element = browser.find_element(By.ID, 'result')
        if element.text.isdigit():
            flag = True
    result = element.text
    time.sleep(4)
    print(result)

