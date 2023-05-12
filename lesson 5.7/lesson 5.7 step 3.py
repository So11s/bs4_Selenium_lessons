from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as browser:
    browser.get("http://parsinger.ru/blank/modal/3/index.html")
    for btn in browser.find_elements(By.CLASS_NAME, "buttons"):
        btn.click()
        alert = browser.switch_to.alert
        str = alert.text
        alert.accept()
        browser.find_element(By.ID, "input").send_keys(str)
        browser.find_element(By.ID, "check").click()
        res = browser.find_element(By.ID, "result").text
        if res != "Неверный пин-код":
            print(res)
            break
