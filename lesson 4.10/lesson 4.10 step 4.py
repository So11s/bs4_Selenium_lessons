from bs4 import BeautifulSoup
import requests
import lxml
import json

url = "http://parsinger.ru/html/index1_page_1.html"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find(class_='pagen').find_all('a')[-1].text

result_json = []

for page in range(1, int(pagen) + 1):

    url = f"http://parsinger.ru/html/index3_page_{page}.html"
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    names = [name.text.strip() for name in soup.find_all(class_='name_item')]
    infos = [i.text.strip().split("\n") for i in soup.find_all(class_='description')]
    prices = [price.text.strip() for price in soup.find_all(class_='price')]

    for name, description, price in zip(names, infos, prices):
        brand, type_, type_connect, gaming = [info.split(":")[-1].strip() for info in description]
        result_json.append({
            'name': name,
            'brand': brand,
            'type': type_,
            'type_connect': type_connect,
            'gaming': gaming,
            'price': price,
        })

with open('../result_lesson4.10_step4.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_json, json_file, indent=4, ensure_ascii=False)