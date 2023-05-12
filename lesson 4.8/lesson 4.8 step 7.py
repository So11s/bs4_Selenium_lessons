from bs4 import BeautifulSoup
import requests
import lxml

url = "https://parsinger.ru/table/5/index.html"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'lxml')
columns = soup.find_all('th')
d = {}
for i in range(1, len(columns) + 1):
    name = soup.select(f'th:nth-child({i})')
    digits = (float(i.text) for i in soup.select(f"tr td:nth-child({i})"))
    d[name[0].text] = round(sum(digits), 3)
print(d)