from bs4 import BeautifulSoup
import requests
import lxml
import json


url = "http://parsinger.ru/html/index1_page_1.html"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find(class_='pagen').find_all('a')[-1].text
categories = soup.find(class_='nav_menu').find_all('a')

result_json = []

ogl = {
    1: ('type', 'material', 'tegnologies'),
    2: ('diagonal', 'material body', 'resolution'),
    3: ('type', 'connect', 'game'),
    4: ('form-factor', 'container', 'buffer'),
    5: ('type connect', 'color', 'type'),
}

for category in range(1, len(categories) + 1):
    for page in range(1, int(pagen) + 1):
        url = f"http://parsinger.ru/html/index{category}_page_{page}.html"
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        names = [name.text.strip() for name in soup.find_all(class_='name_item')]
        infos = [i.text.strip().split("\n") for i in soup.find_all(class_='description')]
        prices = [price.text.strip() for price in soup.find_all(class_='price')]

        for name, description, price in zip(names, infos, prices):
            brand, *items = [info.split(":")[-1].strip() for info in description]
            d = {
                'name': name,
                 'brand': brand,
            }
            for i in range(len(ogl[category])):
                d[ogl[category][i]] = items[i]
            d['price'] = price
            result_json.append(d)

with open('../result_lesson4.10_step5.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_json, json_file, indent=4, ensure_ascii=False)