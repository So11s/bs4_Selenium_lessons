from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

with webdriver.Chrome(options=opt) as browser:
    browser.get("http://parsinger.ru/scroll/2/index.html")
    total = 0
    for row in browser.find_elements(By.TAG_NAME, "input"):
        row.click()
        num = row.get_attribute("id")
        if browser.find_element(By.ID, f"result{num}").text.isdigit():
            total += int(browser.find_element(By.ID, f"result{num}").text)
        # browser.execute_script("return arguments[0].scrollIntoView(true)", row)

    print(total)