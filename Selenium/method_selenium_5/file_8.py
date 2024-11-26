import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
with chrome_driver as browser:
    browser.get("https://parsinger.ru/selenium/5.5/4/1.html")
    time.sleep(0.3)

    for div in browser.find_elements(By.CLASS_NAME, "parent"):
        gray = div.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]')
        blue = div.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]')
        btn = div.find_element(By.TAG_NAME, 'button')
        blue.send_keys(gray.text)
        gray.clear()
        btn.click()

    browser.find_element(By.ID, "checkAll").click()

    print(browser.find_element(By.ID, "congrats").text)






