import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

url = 'https://parsinger.ru/selenium/5.5/2/1.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    result = [element.clear() for element in browser.find_elements(By.CLASS_NAME, 'text-field')
              if element.is_enabled()]
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
    time.sleep(5)
