from bs4 import BeautifulSoup
import requests
import lxml

url = "http://parsinger.ru/html/hdd/4/4_1.html"

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
old_price = soup.find('span', id='old_price').text.split()[0]
new_price = soup.find('span', id='price').text.split()[0]
res = (int(old_price) - int(new_price)) / int(old_price) * 100
print(res)
# print(old_price)