import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math


with webdriver.Chrome() as browser:
    def calc():
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser.get('https://suninjuly.github.io/math.html')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'input_value')))

    # Получаем текст из элемента с ID 'input_value'
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CLASS_NAME, 'form-check-input').click()
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"').click()
    browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()
    result = browser.switch_to.alert.text
    print(result)

    time.sleep(3)



