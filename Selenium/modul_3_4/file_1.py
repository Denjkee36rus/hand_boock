import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    for field in browser.find_elements(By.CLASS_NAME, 'form'):
        field.send_keys('Text')
    browser.find_element(By.ID, 'btn').click()
    result = browser.find_element(By.ID, 'result').text
    time.sleep(3)
    print(result)
