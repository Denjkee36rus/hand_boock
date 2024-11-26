import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



with webdriver.Chrome() as browser:
    actions = ActionChains(browser)
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    result = []
    for x in browser.find_elements(By.CLASS_NAME, 'scroll-container'):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(x.find_element(By.TAG_NAME, 'p').text)








