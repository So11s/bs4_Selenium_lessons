from bs4 import BeautifulSoup
import requests
import lxml

url = "https://parsinger.ru/table/2/index.html"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
rows = soup.find_all('tr')
sp = (float(i.find('td').text) for i in rows[1:])
print(sum(sp))