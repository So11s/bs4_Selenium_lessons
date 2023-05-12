from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://parsinger.ru/downloads/cooking_soup/index.zip'

with open('../index.html', 'rb') as file:
    soup = BeautifulSoup(file, 'lxml')
    print(soup)
