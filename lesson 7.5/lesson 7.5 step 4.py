from telethon import TelegramClient, events, sync, connection
from telethon.tl.types import InputMessagesFilterPinned
from token_telegram import api_id, api_hash


with TelegramClient("session_name2", api_id, api_hash) as client:
    message = client.get_messages("https://t.me/Parsinger_Telethon_Test", filter=InputMessagesFilterPinned)
    print(message[0].from_id.user_id)
