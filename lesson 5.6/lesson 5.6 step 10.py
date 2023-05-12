from selenium import webdriver
from selenium.webdriver.common.by import By


opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

with webdriver.Chrome(options=opt) as browser:
    browser.get("http://parsinger.ru/scroll/3/")
    total = 0
    for row in browser.find_elements(By.TAG_NAME, "input"):
        row.click()
        num = row.get_attribute("id")
        if browser.find_element(By.ID, f"result{num}").text.isdigit():
            total += int(num)

    print(total)