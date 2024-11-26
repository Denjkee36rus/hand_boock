import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

url = 'https://parsinger.ru/selenium/5.5/3/1.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    total_element = browser.find_elements(By.CLASS_NAME, 'parent')
    result = sum([int(element.text) for element in total_element
                  if element.find_element(By.XPATH, '//input[@type="checkbox"]').is_selected()])
    print(result)
    time.sleep(5)