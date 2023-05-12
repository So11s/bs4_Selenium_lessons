from bs4 import BeautifulSoup
import requests
import lxml

url = "http://parsinger.ru/html/index1_page_1.html"

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
prices = soup.select("p.price")
# print(list_prices)
list_prices = sum([int(item.text.split(" ")[0]) for item in prices])

print(list_prices)