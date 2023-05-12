from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash
import os


with TelegramClient("session_name2", api_id, api_hash) as client:
    size = 0
    for user in client.get_participants('t.me/Parsinger_Telethon_Test'):
        for index, photo in enumerate(client.iter_profile_photos(user)):
            file_name = f'./img_step_8/{user.id}_{index}.jpg'
            client.download_media(photo, file_name)
            size += os.path.getsize(file_name)
    print(size)