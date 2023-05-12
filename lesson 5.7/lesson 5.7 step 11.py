from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sqrt


opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

with webdriver.Chrome(options=opt) as browser:
    sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
             'http://parsinger.ru/blank/1/3.html',
             'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
             'http://parsinger.ru/blank/1/6.html', ]
    total = 0
    for site in sites:
        browser.get(site)
        browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        total += sqrt(int(browser.find_element(By.ID, "result").text))
    print(round(total, 9))