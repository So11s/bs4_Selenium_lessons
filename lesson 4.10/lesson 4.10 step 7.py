from bs4 import BeautifulSoup
import requests
import lxml
import json


# Функция принимает url и возвращает BeautifulSoup
def get_soup_from_url(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# Возвращает количество категорий
def get_categories():
    categories = get_soup_from_url("https://parsinger.ru/html/index1_page_1.html").find(class_='nav_menu').find_all('a')
    return len(categories)


# Возвращает максимальное числа pagen
def get_pagen():
    pagen = get_soup_from_url("https://parsinger.ru/html/index1_page_1.html").find(class_='pagen').find_all('a')[-1]
    return int(pagen.text)


urls_list = []

# находим все ссылки и добавляем в список urls_list
for category_i in range(1, get_categories() + 1):
    for page in range(1, get_pagen() + 1):
        soup = get_soup_from_url(f'https://parsinger.ru/html/index{category_i}_page_{page}.html')
        u = [(category_i, f"https://parsinger.ru/html/{btn.find('a').get('href')}") for btn in soup.find_all(class_='sale_button')]
        urls_list.extend(u)

res_json = []

name_category = {
    1: "watch",
    2: "phone",
    3: "mouse",
    4: "HDD",
    5: "headphones"
}

for category_i, url_n in urls_list:
    soup = get_soup_from_url(url_n)

    category = name_category[category_i]
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
        'link': url_n,
    }

    for key, value in description:
        d['description'].setdefault(key, value)

    res_json.append(d)

with open('../result_lesson4.10_step7.json', 'w', encoding='utf-8') as file:
    json.dump(res_json, file, indent=4, ensure_ascii=False)