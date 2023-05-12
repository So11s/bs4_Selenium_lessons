from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

with webdriver.Chrome(options=opt) as browser:
    browser.get("https://parsinger.ru/methods/3/index.html")
    print(sum(int(cooki['value']) for cooki in browser.get_cookies()))