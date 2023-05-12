from bs4 import BeautifulSoup
import csv
import requests
import lxml

url = "https://parsinger.ru/html/index1_page_1.html"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')

pages = soup.find(class_='pagen').find_all('a')[-1].text

header = ['Наименование', 'Бренд', 'Форм-фактор', 'Емкость', 'Объем буф. памяти', 'Цена']

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(header)

for i in range(1, int(pages) + 1):
    url = f"https://parsinger.ru/html/index4_page_{i}.html"

    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    names = [name.text.strip() for name in soup.find_all(class_='name_item')]
    infos = [info.text.split('\n') for info in soup.find_all(class_='description')]
    prices = [price.text.split()[0] for price in soup.find_all(class_='price')]

    for name, descr, price in zip(names, infos, prices):
        flatten = name, *[x.split(':')[1].strip() for x in descr if x], price

        file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(flatten)

    file.close()