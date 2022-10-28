import re
import time
import requests
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.functions.messages import GetHistoryRequest, ReadHistoryRequest
from telethon import TelegramClient, events, sync
import telethon.sync
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import sqlite3
import telebot
from telebot import types, apihelper
import os,random,shutil,subprocess

TOKEN = '1940224257:AAEJgHU-uTyT0JRyNOE0RZ1WboFDJUJMtgo'
bot = telebot.TeleBot(TOKEN)
API_ID = 988074
API_HASH = 'a5ec8b7b6dbeedc2514ca7e4ba200c13'


def proxis(id_akk):
    try:
        connection = sqlite3.connect('spam_baza.sqlite')
        q = connection.cursor()
        proxi = q.execute(f'SELECT proxi FROM akk where id =  "{id_akk}"').fetchone()[0]
        return proxi
    except Exception as e:
        return 'no'

def main():
    connection = sqlite3.connect('database.sqlite')
    q = connection.cursor()
    q.execute(f"SELECT * FROM list_chat where status = 'Send'")
    row = q.fetchall()
    for i in row:
        q.execute(f"update list_chat set status = 'NoSend' where id_str = '{i[0]}'")
        connection.commit()
        q.execute(f"update list_chat set colvo_send = colvo_send + '1' where id_str = '{i[0]}'")
        connection.commit()  
        try:
            proxi = proxis(i[7])   
            login_prox = proxi.split('@')[0].split(':')[0]
            pass_prox = proxi.split('@')[0].split(':')[1]
            ip_prox = proxi.split('@')[1].split(':')[0]
            port_prox = proxi.split('@')[1].split(':')[1]
            proxy = {'proxy_type':'socks5','addr': str(ip_prox),'port': int(port_prox),'username':str(login_prox),'password': str(pass_prox),'rdns': True}
            client = TelegramClient(str(i[7]), API_ID, API_HASH, device_model="Quik bot", system_version="6.12.0", app_version="10 P (28)", proxy=proxy)
            client.connect()    
            status_akk = client.is_user_authorized()
            if status_akk == True:
                akk = i[7]
                link = i[1]
                text = i[2]
                photo = i[6]
                try:
                    if photo != None:
                        try:
                            client.send_message(link, text, file=photo)
                            try:
                                bot.send_message(i[8], f'✔️ Успешная отправка | {i[3]} | {i[7]}')
                            except Exception as e:
                                bot.send_message(-1001584706559, e)
                        except Exception as e:
                            client.send_message(link, text)
                            try:
                                bot.send_message(i[8], f'✔️ Успешная отправка | {i[3]} | {i[7]}')
                            except Exception as e:
                                bot.send_message(-1001584706559, e)
                    else:
                        client.send_message(link, text)
                        try:
                            bot.send_message(i[8], f'✔️ Успешная отправка | {i[3]} | {i[7]}')
                        except Exception as e:
                            bot.send_message(-1001584706559, e)
                except Exception as e:
                    bot.send_message(-1001584706559, e)
                    try:
                        bot.send_message(i[8], f'✖️ Ошибка отправки | {i[3]} | {i[7]} | {e}')
                    except Exception as e:
                        bot.send_message(-1001584706559, e)
            else:
                try:
                    bot.send_message(i[8], f'✖️ Ошибка аккаунта | {i[7]}')
                except Exception as e:
                    bot.send_message(-1001584706559, e)
                

            client.disconnect()
        except Exception as e:
            try:
                bot.send_message(i[8], f'✖️ Ошибка: {e} | {i[7]}')
                client.disconnect()
            except Exception as e:
                bot.send_message(-1001584706559, e)



while True:
    main()
