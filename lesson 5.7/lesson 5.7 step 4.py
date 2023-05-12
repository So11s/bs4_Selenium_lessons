from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as browser:
    browser.get("http://parsinger.ru/blank/modal/4/index.html")
    btn = browser.find_element(By.ID, "check")
    for pin in browser.find_elements(By.CLASS_NAME, "pin"):
        str = pin.text
        btn.click()
        alert = browser.switch_to.alert
        alert.send_keys(str)
        alert.accept()
        answer = browser.find_element(By.ID, "result").text
        if answer != "Неверный пин-код":
            print(answer)
            break