from selenium import webdriver
from selenium.webdriver.common.by import By
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as browser:
    browser.get("http://parsinger.ru/window_size/1/")
    browser.set_window_size(571, 692)
    print(browser.find_element(By.ID, "result").text)
    time.sleep(10)