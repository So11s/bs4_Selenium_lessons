from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    res = 0
    res_str = ''
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/methods/5/index.html")
    urls = browser.find_elements(By.CSS_SELECTOR, ".urls a")

    for url in urls:
        url.click()
        for item in browser.get_cookies():
            print(item['expiry'], browser.find_element(By.ID, "result").text)
            if int(item['expiry']) > res:
                res_str = browser.find_element(By.ID, "result").text
                res = int(item['expiry'])
        browser.back()
    print()
    print(res, res_str)

