from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/draganddrop/3/index.html")
    block = browser.find_element(By.ID, "block1")
    end_point = browser.find_element(By.ID, "point5")
    actions = ActionChains(browser)
    actions.click_and_hold(block).move_by_offset(400, 0).perform()

    print(browser.find_element(By.ID, "message").text)
