import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

url = 'https://parsinger.ru/methods/3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    sum_cookie = 0
    for cookie in cookies:
        if 'secret_cookie_' in cookie['name']:
            sum_cookie += int(cookie['value'])
    print(sum_cookie)

