from bs4 import BeautifulSoup
import csv
import requests
import lxml


header = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена',
          'Ссылка на карточку с товаром']

url = "https://parsinger.ru/html/index1_page_1.html"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, "lxml")

pages = soup.find(class_='pagen').find_all('a')[-1].text

categories = soup.find(class_='nav_menu').find_all('a')

all_urls_list = []

for category in range(1, len(categories) + 1):
    for page in range(1, int(pages) + 1):
        url = f"https://parsinger.ru/html/index{category}_page_{page}.html"
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')
        [all_urls_list.append(item.find('a').get('href')) for item in soup.find_all('div', class_='sale_button')]

items = []

for u in all_urls_list:
    url = f"https://parsinger.ru/html/{u}"
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "lxml")
    name = soup.find(id='p_header').text
    article = soup.find(class_='article').text.split()[-1]
    brand = soup.find(id='brand').text.split()[-1]
    model = soup.find(id='model').text.split()[-1]
    stock = soup.find(id='in_stock').text.split(':')[-1].strip()
    price = soup.find(id='price').text
    old_price = soup.find(id='old_price').text

    info = [name, article, brand, model, stock, price, old_price, url]
    items.append(info)

with open('../result_step7.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(header)
    writer.writerows(items)