from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_argument('--headless')

with webdriver.Chrome(options=opt) as browser:
    browser.get("https://parsinger.ru/methods/3/index.html")
    cookies = browser.get_cookies()
    res = []
    for cooki in cookies:
        if '_' in cooki['name'] and int(cooki['name'].split('_')[-1]) % 2 == 0:
            res.append(int(cooki['value']))

print(sum(res))