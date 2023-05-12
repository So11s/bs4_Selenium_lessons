from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.implicitly_wait(10)
    browser.get("https://parsinger.ru/selenium/1/1.html")
    for word in browser.find_elements(By.CSS_SELECTOR, "input[type='text']"):
        word.send_keys('aaa')
    browser.find_element(By.CSS_SELECTOR, "input[type='button']").click()
    print(browser.find_element(By.ID, 'result').text)