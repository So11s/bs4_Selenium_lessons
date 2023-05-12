from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import product


opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as browser:
    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    for x, y in product(window_size_x, window_size_y):
        browser.get("http://parsinger.ru/window_size/2/index.html")
        browser.set_window_size(x, y)
        result = browser.find_element(By.ID, "result").text
        if result:
            print(result)
            break
