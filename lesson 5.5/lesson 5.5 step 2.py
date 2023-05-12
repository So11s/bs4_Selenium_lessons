from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/methods/1/index.html")
    browser.implicitly_wait(5)

    while not  browser.find_element(By.ID, "result").text.isdigit():
        browser.refresh()
    print(browser.find_element(By.ID, "result").text)