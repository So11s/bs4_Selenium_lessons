import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    total = 0
    for i in range(1, 6):
        div = browser.find_element(By.XPATH, f'//*[@id="scroll-container_{i}"]/div')

        for _ in range(10):
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 100).perform()

        total += sum([int(span.text) for span in browser.find_elements(By.CSS_SELECTOR, f'#scroll-container_{i} span')])

    print(total)