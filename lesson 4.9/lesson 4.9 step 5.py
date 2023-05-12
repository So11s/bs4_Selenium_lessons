from bs4 import BeautifulSoup
import csv
import requests
import lxml

url = "https://parsinger.ru/html/index1_page_1.html"

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

pages = soup.find(class_='pagen').find_all('a')[-1].text


for i in range(1, 6):
    for j in range(1, 4):
        url = f"https://parsinger.ru/html/index{i}_page_{j}.html"

        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        names = [name.text.strip() for name in soup.find_all(class_='name_item')]
        infos = [info.text.split('\n') for info in soup.find_all(class_='description')]
        prices = [price.text.split()[0] for price in soup.find_all(class_='price')]

        for name, descr, price in zip(names, infos, prices):
            flatten = name, *[x.split(':')[1].strip() for x in descr if x], price

            file = open('../result_step5.csv', 'a', encoding='utf-8-sig', newline='')
            writer = csv.writer(file, delimiter=';')
            writer.writerow(flatten)

            file.close()