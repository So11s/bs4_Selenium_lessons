from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/draganddrop/1/index.html")
    red_square = browser.find_element(By.ID, "draggable")
    grey_square = browser.find_element(By.ID, "field2")
    actions = ActionChains(browser)
    actions.drag_and_drop(red_square, grey_square).perform()
    print(browser.find_element(By.ID, "result").text)