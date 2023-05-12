from telethon import TelegramClient, events, sync, connection
from token_telegram import api_id, api_hash
from telethon.tl.functions.users import GetFullUserRequest


with TelegramClient("session_name2", api_id, api_hash) as client:
    lst = ['Anthony_Hills', 'Craig_Moody', 'Kathleen_Browns', 'Vicki_Baileys', 'Jorge_Garrett', 'Larry_Summers',
           'Tommy_Sullivan', 'Edward_Murrray', 'Nicholas_Gonzales', 'Virgina_Garcia', 'Denise_Barker', 'Jessie_Wright',
           'Mary_Baileyn', 'Claytons_Riley', 'Joshuan_Chandler', 'Jameson_Powell', 'Harry_Valdes', 'Chriss_Yong',
           'Sarah_Wilis', 'Frances_Ross', 'Joseph_Anderson']
    total = 0
    for user in client.iter_participants('Parsinger_Telethon_Test'):
        if user.username in lst:
            total += int(client(GetFullUserRequest(user)).full_user.about)
    print(total)