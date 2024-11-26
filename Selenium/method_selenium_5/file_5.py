import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

url = 'https://parsinger.ru/methods/5/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    urls = browser.find_elements(By.XPATH, '//div[@class="urls"]')

    # Dictionary to store the cookie expiration times
    cookie_lifetimes = {}

    for element in urls:
        element.click()
        time.sleep(1)

        # Get the expiration time of the cookie
        cookie_expiration = browser.get_cookie()["expiry"]

        # Calculate the remaining lifetime of the cookie
        remaining_lifetime = cookie_expiration - time.time()

        # Store the cookie lifetime in the dictionary
        cookie_lifetimes[element.text] = remaining_lifetime

    # Find the cookie with the longest lifetime
    longest_lifetime = max(cookie_lifetimes.values())
    longest_lifetime_cookie = [key for key, value in cookie_lifetimes.items() if value == longest_lifetime][0]

    # Get the number from the page with the longest lifetime cookie
    browser.get(longest_lifetime_cookie)
    number = browser.find_element(By.XPATH, '//p[@id="result"]').text

    # Print the number
    print(number)
