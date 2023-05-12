from bs4 import BeautifulSoup
import requests
import lxml
import json

url = "https://parsinger.ru/html/index3_page_1.html"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find(class_='pagen').find_all('a')[-1].text

urls_list = []

# находим все ссылки и добавляем в список urls_list
for page in range(1, int(pagen) + 1):
    response = requests.get(url=f'https://parsinger.ru/html/index3_page_{page}.html')
    soup = BeautifulSoup(response.text, 'lxml')
    u = [f"https://parsinger.ru/html/{btn.find('a').get('href')}" for btn in soup.find_all(class_='sale_button')]
    urls_list.extend(u)

res_json = []

for url_mouse in urls_list:
    response = requests.get(url=url_mouse)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    category = "mouse"
    name = soup.find(id='p_header').text
    article = soup.find(class_='article').text.split(': ')[-1]
    description = [(desc['id'], desc.text.split(': ', 1)[-1]) for desc in soup.find(id='description').find_all('li')]
    span = soup.find(id='in_stock').text.split()[-1]
    price = soup.find(id='price').text
    old_price = soup.find(id='old_price').text

    d = {
        'category': category,
        'name': name,
        'article': article,
        'description': {},
        'count': span,
        'price': price,
        'old_price': old_price,
        'link': url_mouse,
    }

    for key, value in description:
        d['description'].setdefault(key, value)

    res_json.append(d)

with open('../result_lesson4.10_step6.json', 'w', encoding='utf-8') as file:
    json.dump(res_json, file, indent=4, ensure_ascii=False)