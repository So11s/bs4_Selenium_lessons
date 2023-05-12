from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash


with TelegramClient("session_name2", api_id, api_hash) as client:
    total = 0
    for message in client.iter_messages("https://t.me/Parsinger_Telethon_Test"):
        if message.text:
            total += int(message.text)
    print(total)