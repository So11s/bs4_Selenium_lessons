from bs4 import BeautifulSoup
import requests
import lxml

url = "https://parsinger.ru/table/5/index.html"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'lxml')
blues = soup.select('td:last-child')
oranges = soup.find_all('td', class_='orange')
res = (float(a.text) * float(b.text) for a, b in zip(blues, oranges))
print(sum(res))