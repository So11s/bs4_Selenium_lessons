from bs4 import BeautifulSoup
import requests
import lxml

# url = "http://parsinger.ru/html/index3_page_4.html"
# response = requests.get(url=url)
# soup_f = BeautifulSoup(response.text, 'lxml')
# count_page = soup_f.find('div', class_='pagen').find_all('a')[-1].text

res = 0

for item in range(1, 33):
    new_url = f"https://parsinger.ru/html/mouse/3/3_{item}.html"
    response_s = requests.get(url=new_url)
    response_s.encoding = 'utf-8'
    soup_s = BeautifulSoup(response_s.text, 'lxml')
    article = soup_s.find('p', class_='article').text
    res += int(article.split()[-1])

print(res)