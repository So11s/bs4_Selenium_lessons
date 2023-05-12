from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

with webdriver.Chrome(options=opt) as browser:
    browser.get("http://parsinger.ru/expectations/6/index.html")
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    res = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "Y1DM2GR")))
    print(res.text)