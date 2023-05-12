from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash
import os


with TelegramClient("session_name2", api_id, api_hash) as client:
    total = 0
    participants = client.get_participants('t.me/Parsinger_Telethon_Test')
    for index, item in enumerate(participants):
        file_name = f'./img_step_6/{index}.jpg'
        client.download_profile_photo(item, file_name, download_big=True)
        total += os.path.getsize(file_name)
    print(total)