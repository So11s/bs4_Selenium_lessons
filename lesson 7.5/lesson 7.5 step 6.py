from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash


with TelegramClient("session_name2", api_id, api_hash) as client:
    print([client.get_entity(message.from_id.user_id).username for message in client.get_messages("https://t.me/Parsinger_Telethon_Test")])