from bs4 import BeautifulSoup
import requests
import lxml

url = "https://parsinger.ru/table/4/index.html"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'lxml')
digits = soup.find_all('td', class_='green')
res = (float(i.text) for i in digits)
print(sum(res))