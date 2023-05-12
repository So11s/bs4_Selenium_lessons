import os
from telethon import TelegramClient, events, sync, connection
from telethon.tl.types import InputMessagesFilterPhotos, PhotoStrippedSize
from token_telegram import api_id, api_hash


with TelegramClient("session_name2", api_id, api_hash) as client:
    total = 0
    for index, message in enumerate(client.iter_messages("https://t.me/Parsinger_Telethon_Test", filter=InputMessagesFilterPhotos)):
        file_name = f"./img_step_7/{index}.jpg"
        client.download_media(message.photo, file_name)

    dir = rf'{os.path.abspath(os.curdir)}\img_step_7'
    for img in os.listdir(dir):
        total += os.path.getsize(f'{dir}\{img}')
    print(total)