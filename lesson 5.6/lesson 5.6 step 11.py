from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

with webdriver.Chrome(options=opt) as browser:
    browser.get("https://parsinger.ru/infiniti_scroll_1/")
    browser.implicitly_wait(5)
    total = 0
    list_input = []
    flag = True
    while flag:
        flag = False
        for span in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span'):
            if span.get_attribute('id') not in list_input:
                span.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
                total += int(span.text)
                list_input.append(span.get_attribute('id'))
                flag = True

            print(total)