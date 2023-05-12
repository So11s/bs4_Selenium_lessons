from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash
from telethon.tl.functions.users import GetFullUserRequest


with TelegramClient("session_name2", api_id, api_hash) as client:
    lst = [332703068, 5914813738, 5710963988, 5799970696, 5843185336,
           5899028303, 5799846345, 5988909155, 5765618528, 5744269105,
           5811870581, 5749394385, 5821321049, 5831778721, 5908359516,
           5807015533, 5877375636, 5748959968, 5852187682, 5642780248,
           5633717169, 5989940172]
    total = 0
    for user in client.iter_participants('Parsinger_Telethon_Test'):
        if user.id in lst:
            total += int(client(GetFullUserRequest(user)).full_user.about)
    print(total)