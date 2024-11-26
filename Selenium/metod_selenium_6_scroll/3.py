from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://parsinger.ru/selenium/5.7/1/index.html'
with webdriver.Chrome() as browser:
    actions = ActionChains(browser)
    browser.get(url)
    for element in browser.find_elements(By.CLASS_NAME, 'button-container'):
        button = element.find_element(By.CLASS_NAME,  'clickMe')
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        button.click()
    alert_text = browser.switch_to.alert.text
    print("Текст alert:", alert_text)

    time.sleep(5)






