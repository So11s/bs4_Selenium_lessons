from bs4 import BeautifulSoup
import requests
import lxml

index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
total = 0

for i in range(5):
    for j in range(32):
        url = f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html"
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        price = int(soup.find('span', id='price').text.split()[0])
        count = int(soup.find('span', id='in_stock').text.split()[-1])
        sum_price = price * count
        total += sum_price

print(total)