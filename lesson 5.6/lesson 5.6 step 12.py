import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates.crx')


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')

    for _ in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()

    print(sum(int(span.text) for span in browser.find_elements(By.CSS_SELECTOR, '#scroll-container p')))
    time.sleep(5)