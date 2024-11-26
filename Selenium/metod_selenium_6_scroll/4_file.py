from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://parsinger.ru/selenium/5.7/5/index.html'
with webdriver.Chrome() as browser:
    actions = ActionChains(browser)
    browser.get(url)

    for element in browser.find_elements(By.CLASS_NAME, 'timer_button'):
        pauses = element.find_element(By.XPATH, '//button[@class="timer_button"]')
        actions.click_and_hold(element).pause(float(element.get_attribute('value'))).release(element).perform()
    alert_text = browser.switch_to.alert.text
    print("Текст alert:", alert_text)
