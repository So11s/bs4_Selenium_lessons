from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get("http://parsinger.ru/selenium/7/7.html")
    browser.implicitly_wait(5)
    res = sum([int(val.text) for val in browser.find_elements(By.TAG_NAME, "option")])
    browser.find_element(By.ID, "input_result").send_keys(res)
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, "result").text)