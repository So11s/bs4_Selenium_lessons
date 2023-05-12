import requests

url = "http://parsinger.ru/downloads/get_json/res.json"

response = requests.get(url=url).json()

res = {}

for item in response:
    res[item['categories']] = res.setdefault(item['categories'], 0) + int(item['count']) * int(item['price'].split()[0])

print(res)