from bs4 import BeautifulSoup
import requests
import lxml

url = "http://parsinger.ru/html/index3_page_1.html"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, "lxml")

pagen = soup.find('div', class_='pagen').find_all('a')[-1].text
itog = []
for page in range(1, int(pagen) + 1):
    resp = requests.get(url=f"https://parsinger.ru/html/index3_page_{page}.html")
    resp.encoding = 'utf-8'
    s_soup = BeautifulSoup(resp.text, 'lxml')
    product_names = [name.text for name in s_soup.find_all('a', class_='name_item')]
    itog.append(product_names)

print(itog)