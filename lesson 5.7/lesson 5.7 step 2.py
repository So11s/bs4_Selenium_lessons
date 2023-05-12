from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as browser:
    browser.get("http://parsinger.ru/blank/modal/2/index.html")
    browser.implicitly_wait(5)
    res = ''
    for btn in browser.find_elements(By.CLASS_NAME, "buttons"):
        btn.click()
        alert = browser.switch_to.alert
        alert.accept()
        answer = browser.find_element(By.ID, "result")
        if answer.text:
            res = answer.text

    print(res)