import os
import requests
import lxml
import aiofiles
import aiohttp
import asyncio

from bs4 import BeautifulSoup


# url = "https://parsinger.ru/asyncio/aiofile/2/index.html"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
#
# urls = [f"{domain}{url['href']}" for url in soup.find(class_="item_card").find_all("a")]
#
# dir = os.path.abspath(os.curdir)
# catalog_img = os.listdir(rf"{dir}/images_step_5")
#
# for url in urls:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     for picture in soup.find_all(class_='picture'):
#         picture_name = picture['src'].split('/')[-1]
#         if picture_name not in catalog_img:
#             response2 = requests.get(picture['src'], stream=True).content
#             with open(f'images_step_5/{picture_name}', 'wb') as file:
#                 file.write(response2)

dir = os.path.abspath(os.curdir)
catalog_img = os.listdir(rf"{dir}/images_step_5")


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


async def write_file(session, url, name_img):
    if name_img not in catalog_img:
        async with aiofiles.open(f'images_step_5/{name_img}', mode='wb') as f:
            async with session.get(url) as response:
                async for file in response.content.iter_chunked(2048):
                    await f.write(file)


async def main():
    url = "https://parsinger.ru/asyncio/aiofile/2/index.html"
    domain = "https://parsinger.ru/asyncio/aiofile/2/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            urls = [f"{domain}{url['href']}" for url in soup.find(class_="item_card").find_all("a")]
            for link in urls:
                async with session.get(link) as response2:
                    soup2 = BeautifulSoup(await response2.text(), 'lxml')
                    links = [picture['src'] for picture in soup2.find_all(class_='picture')]
                tasks = [asyncio.create_task(write_file(session, link, link.split('/')[-1])) for link in links]

            await asyncio.gather(*tasks)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())


print(get_folder_size(f"{dir}/images_step_5/"))
