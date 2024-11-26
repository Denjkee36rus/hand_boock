import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/1/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    result = [item.clear() for item in browser.find_elements(By.TAG_NAME, 'input')]
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
    time.sleep(5)