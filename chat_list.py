import asyncio
from telethon import TelegramClient
from telethon.errors import rpcerrorlist
from datetime import date, datetime
import re
import sqlite3


api_id = 988074
api_hash = "a5ec8b7b6dbeedc2514ca7e4ba200c13"



def proxis(id_akk):
    connection = sqlite3.connect('spam_baza.sqlite')
    q = connection.cursor()
    proxi = q.execute(f'SELECT proxi FROM akk where id =  "{id_akk}"').fetchone()[0]
    return proxi


async def get_chats(phone,users):
	try:
		proxi = proxis(phone)
		login_prox = proxi.split('@')[0].split(':')[0]
		pass_prox = proxi.split('@')[0].split(':')[1]
		ip_prox = proxi.split('@')[1].split(':')[0]
		port_prox = proxi.split('@')[1].split(':')[1]
		proxy = {'proxy_type':'socks5','addr': str(ip_prox),'port': int(port_prox),'username':str(login_prox),'password': str(pass_prox),'rdns': True}
		connection = sqlite3.connect('database.sqlite')
		q = connection.cursor()
		client = TelegramClient(str(phone), api_id, api_hash, device_model="Ids bot", system_version="6.12.0", app_version="10 P (28)", proxy=proxy)
		await client.connect()
		me = await client.get_me()
		dialogs = await client.get_dialogs()
		for chat in dialogs:
			id_chat = str(chat.id)
			if id_chat[:4] == '-100':
				print(chat.id)
				q = q.execute(f"SELECT * FROM list_chat WHERE akk = '{phone}' and id = '{chat.id}'")
				row = q.fetchone()
				if row is None:
					q.execute("INSERT INTO list_chat (id,name,akk,id_user) VALUES ('%s','%s','%s','%s')"%(chat.id,chat.name,phone,users))
					connection.commit()
		try:
			await client.disconnect()
		except OSError:
			return 'ddddd'
			print('Error on disconnect')
		return 'ok'
	except Exception as e:
		try:
			await client.disconnect()
		except OSError:
			return 'ddddd'



def mainssssss(phone,users):
	try:
		www = loop.run_until_complete(get_chats(phone,users))
		return www
	except Exception as e:
		return 'ddddd'

loop = asyncio.get_event_loop()