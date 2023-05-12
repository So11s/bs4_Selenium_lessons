from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

with webdriver.Chrome(options=opt) as browser:
    browser.get("http://parsinger.ru/scroll/4/index.html")
    browser.implicitly_wait(5)
    res = 0
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn")
    for btn in buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true)", btn)
        btn.click()
        res += int(browser.find_element(By.ID, "result").text)

    print(res)