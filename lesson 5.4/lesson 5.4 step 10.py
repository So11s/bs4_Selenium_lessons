from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get("http://parsinger.ru/selenium/3/3.html")
    res = [int(item.text) for item in browser.find_elements(By.CSS_SELECTOR, "p:nth-child(2)")]
    print(sum(res))