from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash


client = TelegramClient('session_name2', api_id, api_hash)
client.start()
print(client.get_me())
client.disconnect()