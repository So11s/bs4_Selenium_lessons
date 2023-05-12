from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash


client = TelegramClient("session_name2", api_id, api_hash)
client.start()
participants = client.get_participants('t.me/Parsinger_Telethon_Test')
print([f"{item.id} {item.first_name} {item.last_name} {item.phone}" for item in participants])