import os
import lxml
import aiofiles
import aiohttp
import asyncio
import time

from bs4 import BeautifulSoup

dir = os.path.abspath(os.curdir)
catalog_img = os.listdir(rf"{dir}/images_step_6")


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


async def write_file(session, url, name_img):
    if name_img not in catalog_img:
        async with aiofiles.open(f'images_step_6/{name_img}', mode='wb') as f:
            async with session.get(url) as response:
                async for file in response.content.iter_chunked(2048):
                    await f.write(file)


async def main():
    url = "https://parsinger.ru/asyncio/aiofile/3/index.html"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            domain = "https://parsinger.ru/asyncio/aiofile/3/"
            urls = [rf"{domain}/{url['href']}" for url in soup.find(class_="item_card").find_all("a")]
            for link in urls:
                async with session.get(link) as response2:
                    soup2 = BeautifulSoup(await response2.text(), 'lxml')
                    domain2 = "https://parsinger.ru/asyncio/aiofile/3/depth2/"
                    urls2 = [fr"{domain2}/{url['href']}" for url in soup2.find(class_="item_card").find_all("a")]
                    links = []
                    for link1 in urls2:
                        async with session.get(link1) as response3:

                            soup3 = BeautifulSoup(await response3.text(), 'lxml')
                            links.extend([picture['src'] for picture in soup3.find_all(class_='picture')])
                tasks = [asyncio.create_task(write_file(session, link, link.split('/')[-1])) for link in links]

                await asyncio.gather(*tasks)

start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())


print(get_folder_size(f"{dir}/images_step_6/"))
print(f'Cохранено за {round(time.perf_counter() - start, 3)} сек')

