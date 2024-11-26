import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
from selenium.webdriver.support.ui import Select

# url = 'https://suninjuly.github.io/selects1.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     num_1 = int(browser.find_element(By.ID, 'num1').text)
#     num_2 = int(browser.find_element(By.ID, 'num2').text)
#     sum_num = num_1 + num_2
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(str(sum_num))
#     browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()
#     result = browser.switch_to.alert.text
#     print(result)
#     time.sleep(3)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

# Константы для селекторов
NUM_1_SELECTOR = (By.ID, 'num1')
NUM_2_SELECTOR = (By.ID, 'num2')
SELECT_SELECTOR = (By.TAG_NAME, "select")
SUBMIT_BUTTON_SELECTOR = (By.CSS_SELECTOR, '[class="btn btn-default"]')

def get_element_text(driver, value):
    """Получает текст элемента по селектору."""
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(value))
    return element.text

def select_option_by_value(driver, selector, value):
    """Выбирает опцию в выпадающем списке по значению."""
    select = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(selector)))
    select.select_by_value(str(value))

def click_submit_button(driver, selector):
    """Кликает на кнопку отправки формы."""
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(selector))
    button.click()

def main():
    url = 'https://suninjuly.github.io/selects1.html'
    with webdriver.Chrome() as browser:
        try:
            browser.get(url)

            # Получаем числа
            num_1 = int(get_element_text(browser, NUM_1_SELECTOR))
            num_2 = int(get_element_text(browser, NUM_2_SELECTOR))
            sum_num = num_1 + num_2

            # Выбираем опцию в выпадающем списке
            select_option_by_value(browser, SELECT_SELECTOR, sum_num)

            # Кликаем на кнопку отправки
            click_submit_button(browser, SUBMIT_BUTTON_SELECTOR)

            # Получаем текст из алерта
            alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
            result = alert.text
            print(result)

        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            browser.quit()

if __name__ == "__main__":
    main()








