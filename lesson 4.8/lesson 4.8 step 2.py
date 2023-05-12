from bs4 import BeautifulSoup
import requests
import lxml

url = "https://parsinger.ru/table/1/index.html"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')

data = soup.find_all('td')
res = sum(set(float(i.text) for i in data))
print(res)
