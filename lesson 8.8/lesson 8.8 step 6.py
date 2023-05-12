import aiohttp
import requests
import asyncio
import lxml
from bs4 import BeautifulSoup

res = []
urls = []

domain = "https://parsinger.ru/asyncio/create_soup/1/"


def get_soup(url):
    response = requests.get(url=url)
    return BeautifulSoup(response.text, 'lxml')


def get_urls(soup):
    for url in soup.find(class_="item_card").find_all("a"):
        urls.append(f"{domain}{url['href']}")


async def get_data(session, url):
    async with session.get(url) as response:
        if response.ok:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')
            num = soup.find("p", class_="text").text
            res.append(int(num))


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(asyncio.create_task(get_data(session, link)) for link in urls))


url = "https://parsinger.ru/asyncio/create_soup/1/index.html"
soup = get_soup(url)
get_urls(soup)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print(sum(res))