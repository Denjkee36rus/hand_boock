import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

url = 'https://parsinger.ru/methods/3/index.html'

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    lst = []
    for x in cookies:
        if int(x.get('name')[14:]) % 2 == 0:
            lst.append(int(x.get('value')))
    print(sum(lst))










    time.sleep(5)

    #rint(sum([int(cookie['value']) for cookie in cookies if str(cookie['name']).split('_')]))