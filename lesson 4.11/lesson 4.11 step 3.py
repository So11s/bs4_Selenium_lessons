import requests

response = requests.get(url='https://parsinger.ru/downloads/get_json/res.json').json()

d = {}

for item in response:
    d[item['categories']] = d.setdefault(item['categories'], 0) + int(item['count'])

print(d)
print(sum(map(int, d.values())))