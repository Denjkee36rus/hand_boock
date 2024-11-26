import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

url = 'https://parsinger.ru/scroll/4/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    sum_result = 0
    for i in browser.find_elements(By.CLASS_NAME, 'btn'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", i)
        i.click()
        result = int(browser.find_element(By.ID, 'result').text)
        sum_result += result
    print(sum_result)



    time.sleep(3)


