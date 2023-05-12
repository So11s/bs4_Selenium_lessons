from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash


with TelegramClient("session_name2", api_id, api_hash) as client:
    user_id = 5807015533
    res = 0
    messages = client.get_messages("https://t.me/Parsinger_Telethon_Test", from_user=user_id)
    for message in messages:
        res += int(message.text)
    print(res)