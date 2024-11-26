from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://parsinger.ru/selenium/5.8/2/index.html'
with webdriver.Chrome() as browser:
    actions = ActionChains(browser)
    browser.get(url)
    result = browser.find_element(By.ID, 'result')
    for element in browser.find_elements(By.CLASS_NAME, 'buttons'):
        element.click()
        number = browser.switch_to.alert.text
        browser.switch_to.alert.dismiss()
        browser.find_element(By.ID, 'input').send_keys(number)
        browser.find_element(By.ID, 'check').click()
        if result.text.isdigit():
            print(result.text)
            break

    time.sleep(3)





