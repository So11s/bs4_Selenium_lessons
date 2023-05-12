from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/draganddrop/2/index.html")
    red_square = browser.find_element(By.ID, "draggable")
    actions = ActionChains(browser)
    for box in browser.find_elements(By.CLASS_NAME, "box"):
        actions.drag_and_drop(red_square, box).perform()

    print(browser.find_element(By.ID, "message").text)