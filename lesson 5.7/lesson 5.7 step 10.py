from selenium import webdriver
from selenium.webdriver.common.by import By


opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

with webdriver.Chrome(options=opt) as browser:
    total = 0
    browser.get("http://parsinger.ru/blank/3/index.html")
    for index, btn in enumerate(browser.find_elements(By.CLASS_NAME, "buttons")):
        btn.click()

    for window_handle in browser.window_handles[1:]:
        browser.switch_to.window(window_handle)
        total += int(browser.execute_script("return document.title;"))
    print(total)
