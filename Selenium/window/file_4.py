from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://parsinger.ru/selenium/5.8/3/index.html'
with webdriver.Chrome() as browser:
    actions = ActionChains(browser)
    browser.get(url)
    check = browser.find_element(By.ID, 'check')
    result = browser.find_element(By.ID, 'result')

    for element in browser.find_elements(By.CLASS_NAME, 'pin'):
        sendkeys = element.text
        check.click()
        browser.switch_to.alert.send_keys(sendkeys)
        browser.switch_to.alert.accept()
        if result.text.isdigit():
            print(result.text)
            break
