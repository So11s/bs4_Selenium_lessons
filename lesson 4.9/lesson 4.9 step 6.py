from bs4 import BeautifulSoup
import csv
import requests
import lxml


header = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
          'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
          'Ссылка на карточку с товаром']

with open('../result_step6.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(header)

res = []

for i in range(1, 33):

    url = f"https://parsinger.ru/html/watch/1/1_{i}.html"

    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    name = soup.find('p', id='p_header').text
    article = soup.find('p', class_='article').text.split()[1]
    info = [i.text.split(':', 1)[-1].strip() for i in soup.find(id='description') if i.text.strip()]
    stock = soup.find(id='in_stock').text.split(':')[1].strip()
    price = soup.find(id='price').text
    old_price = soup.find(id='old_price').text

    res_i = [name, article, *info, stock, price, old_price, url]
    res.append(res_i)


with open('../result_step6.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for row in res:
        writer.writerow(row)