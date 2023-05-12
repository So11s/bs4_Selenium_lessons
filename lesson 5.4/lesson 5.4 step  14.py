from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get("http://parsinger.ru/selenium/6/6.html")
    browser.implicitly_wait(5)
    res = eval(browser.find_element(By.ID, 'text_box').text)
    for val in browser.find_elements(By.TAG_NAME, "option"):
        if int(val.text) == res:
            val.click()
        break
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, "result").text)