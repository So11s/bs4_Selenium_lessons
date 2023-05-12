from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get("http://parsinger.ru/selenium/4/4.html")
    browser.implicitly_wait(5)
    checks_box = browser.find_elements(By.CLASS_NAME, "check")
    [btn.click() for btn in checks_box]
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, "result").text)