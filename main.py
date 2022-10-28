# -*- coding: utf-8 -*-
from decimal import *
import telebot
import datetime
from telebot import types, apihelper
import sqlite3
import random
import time
import os,random,shutil,subprocess
import json
import keyboards
import requests
from datetime import datetime, timedelta
import chat_list
from datetime import date
from dateutil.relativedelta import relativedelta
from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime

TOKEN = '2055296300:AAEaLrWlowY6290Q0-k6mawS2ps-yzuXTn8'
bot = telebot.TeleBot(TOKEN)
admin = 2089909413


connection = sqlite3.connect('spam_baza.sqlite')
q = connection.cursor()
qiwi_p2p_token = q.execute(f'SELECT qiwi_token FROM config where id =  "1"').fetchone()[0]
p2p = QiwiP2P(auth_key=qiwi_p2p_token)

@bot.message_handler(commands=['start'])
def start_message(message):
	if message.chat.type == 'private':
		userid = str(message.chat.id)
		username = str(message.from_user.username)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		q = q.execute('SELECT * FROM ugc_users WHERE id IS '+str(userid))
		row = q.fetchone()
		if row is None:
			q.execute("INSERT INTO ugc_users (id) VALUES ('%s')"%(userid))
			connection.commit()
		try:
			func.first_join(user_id=chat_id, username=username)
		except:
			pass
		bot.send_message(message.chat.id,f'👑 Добро пожаловать в бот для автопостинга !',parse_mode='HTML',reply_markup=keyboards.main)

		
@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.chat.type == 'private':
		if message.text.lower() == '/admin':
			if message.chat.id == admin:
				connection = sqlite3.connect('spam_baza.sqlite')
				q = connection.cursor()
				all_user_count = q.execute(f'SELECT COUNT(id) FROM ugc_users').fetchone()[0]
				all_user_podpiska = q.execute(f'SELECT COUNT(id) FROM ugc_users WHERE data != "Нет"').fetchone()[0]
				keyboard = types.InlineKeyboardMarkup()
				keyboard.add(types.InlineKeyboardButton(text=f'''Пользователи''',callback_data=f'admin_search_user'))
				keyboard.add(types.InlineKeyboardButton(text='Рассылка',callback_data='send_sms_bot'))
				keyboard.add(types.InlineKeyboardButton(text='Обновить время',callback_data='timeupdate'))
				keyboard.add(types.InlineKeyboardButton(text='Рассылка',callback_data='spamspam'))
				keyboard.add(types.InlineKeyboardButton(text='Перезапустить боты',callback_data='restartsssss'))
				keyboard.add(types.InlineKeyboardButton(text='Сменить P2P QIWI',callback_data='qiwi_smena'))
				bot.send_message(message.chat.id, f'''Всего пользователей: {all_user_count}
Подписок {all_user_podpiska}''',parse_mode='HTML', reply_markup=keyboard)



		elif message.text.lower() == '🎛 меню':
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⏳ Автопостинг''',callback_data=f'akks'),types.InlineKeyboardButton(text=f'''💬 Автоответчик''',callback_data=f'Автоответчик'))
			keyboard.add(types.InlineKeyboardButton(text=f'''🖥 Профиль''',callback_data=f'profale'),types.InlineKeyboardButton(text=f'''📖 Информация''',callback_data=f'info'))
			bot.send_message(message.chat.id, f'''◾️ Выберите нужный пункт меню:''',parse_mode='HTML', reply_markup=keyboard)
			return

		

def new_data(message):
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
	if message.text != '🎛 Меню':
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		chat_chat = q.execute(f'SELECT chat FROM ugc_users where id =  "{message.chat.id}"').fetchone()[0]
		connection = sqlite3.connect('database.sqlite')
		q = connection.cursor()
		if int(tipsend) == 4:
			q.execute(f"update list_chat set photo = '{message.text}' where id_str = '{chat_chat}'")
			connection.commit()
		if int(tipsend) == 1:
			q.execute(f"update list_chat set username = '{message.text}' where id_str = '{chat_chat}'")
			connection.commit()
		if int(tipsend) == 6:
			q.execute(f"update list_chat set dop_text = '{message.text}' where id_str = '{chat_chat}'")
			connection.commit()
		if int(tipsend) == 2:
			if int(message.text) >= 1:
				q.execute(f"update list_chat set time = '{message.text}' where id_str = '{chat_chat}'")
				connection.commit()
				clock_in_half_hour = datetime.now() + timedelta(minutes=(int(message.text)))
				q.execute(f"update list_chat set time_step = '{clock_in_half_hour.hour}:{clock_in_half_hour.minute}' where id_str = '{chat_chat}'")
				connection.commit()
		bot.send_message(message.chat.id, '✔️ Готово',parse_mode='HTML', reply_markup=keyboard)
	else:
		bot.send_message(message.chat.id, 'Отменили',parse_mode='HTML', reply_markup=keyboard)

def new_data_m(message):
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
	if message.text != '🎛 Меню':
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		chat_chat = q.execute(f'SELECT akk FROM ugc_users where id =  "{message.chat.id}"').fetchone()[0]
		connection = sqlite3.connect('database.sqlite')
		q = connection.cursor()
		if int(tipsend11) == 4:
			q.execute(f"update list_chat set photo = '{message.text}' where akk = '{chat_chat}'")
			connection.commit()
		if int(tipsend11) == 1:
			q.execute(f"update list_chat set username = '{message.text}' where akk = '{chat_chat}'")
			connection.commit()
		bot.send_message(message.chat.id, '✔️ Готово',parse_mode='HTML', reply_markup=keyboard)
	else:
		bot.send_message(message.chat.id, 'Отменили',parse_mode='HTML', reply_markup=keyboard)

def btc_oplata_1(message):
	keyboard = types.InlineKeyboardMarkup()
	if message.text != '🎛 Меню':
		new_bill = p2p.bill(amount=int(message.text), lifetime=45)
		keyboard.add(types.InlineKeyboardButton(text='💳 Перейти к оплате',url=new_bill.pay_url))
		keyboard.add(types.InlineKeyboardButton(text='✅ Проверить',callback_data=f'Check_Depozit_qiwi_{new_bill.bill_id}'))
		bot.send_message(message.chat.id, '''▪️ Для совершения оплаты перейдите по ссылки из кнопки и совершите оплату счета !
			
⏰ Ссылка актуальна: 45 минут''',parse_mode='HTML', reply_markup=keyboard)
	else:
		bot.send_message(message.chat.id, 'Отменили',parse_mode='HTML', reply_markup=keyboard)

def new_tig(message):
	if message.text != '🎛 Меню':
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		q.execute(f"update config set qiwi_token = '{message.text}' where id = '1'")
		connection.commit()
		bot.send_message(message.chat.id, '''✔️ Gotovo ! | /admin''',parse_mode='HTML')
	else:
		bot.send_message(message.chat.id, 'Отменили',parse_mode='HTML')


def send_photoorno(message):
	if message.text != 'Отмена':
		global text_send_all
		text_send_all = message.text
		msg = bot.send_message(message.chat.id, 'Отправьте ссылку на медиа',parse_mode='HTML',disable_web_page_preview = True)
		bot.register_next_step_handler(msg, admin_send_message_all_text_rus)


def admin_send_message_all_text_rus(message):
	if message.text != 'Отмена':
		global media
		media = message.text
		if int(tipsendSSSSS) == 1:
			msg = bot.send_photo(message.chat.id,str(media), "Отправить всем пользователям уведомление:\n" + text_send_all +'\n\nЕсли вы согласны, напишите Да',parse_mode='HTML')
			bot.register_next_step_handler(msg, admin_send_message_all_text_da_rus)
				
		if int(tipsendSSSSS) == 2:

			msg = bot.send_animation(chat_id=message.chat.id, animation=media, caption="Отправить всем пользователям уведомление:\n" + text_send_all +'\n\nЕсли вы согласны, напишите Да',parse_mode='HTML')
			bot.register_next_step_handler(msg, admin_send_message_all_text_da_rus)

		if int(tipsendSSSSS) == 3:

			media = f'<a href="{media}">.</a>'
			msg = bot.send_message(message.chat.id, f'''Отправить всем пользователям уведомление:
{text_send_all}
{media}
Если вы согласны, напишите Да''',parse_mode='HTML')
			bot.register_next_step_handler(msg, admin_send_message_all_text_da_rus)

def admin_send_message_all_text_da_rus(message):
	otvet = message.text
	colvo_send_message_users = 0
	colvo_dont_send_message_users = 0
	if message.text != 'Отмена':	
		if message.text.lower() == 'Да'.lower():
			connection = sqlite3.connect('spam_baza.sqlite')
			with connection:	
				q = connection.cursor()
				bot.send_message(message.chat.id, 'Начинаем отправлять!')
				if int(tipsendSSSSS) == 1: # картинка
					q.execute("SELECT * FROM ugc_users")
					row = q.fetchall()
					for i in row:
						jobid = i[0]

						time.sleep(0.1)
						reply = json.dumps({'inline_keyboard': [[{'text': '✖️ Закрыть', 'callback_data': f'Главное'}]]})
						response = requests.post(
							url='https://api.telegram.org/bot{0}/{1}'.format(TOKEN, "sendPhoto"),
							data={'chat_id': jobid,'photo': str(media), 'caption': str(text_send_all),'reply_markup': str(reply),'parse_mode': 'HTML'}
						).json()
						if response['ok'] == False:
							colvo_dont_send_message_users = colvo_dont_send_message_users + 1
						else:
							colvo_send_message_users = colvo_send_message_users + 1;
					bot.send_message(message.chat.id, 'Отправлено сообщений: '+ str(colvo_send_message_users)+'\nНе отправлено: '+ str(colvo_dont_send_message_users))	

				elif int(tipsendSSSSS) == 2: # гиф
					q.execute("SELECT * FROM spam_baza")
					row = q.fetchall()
					for i in row:
						jobid = i[0]

						time.sleep(0.1)
						reply = json.dumps({'inline_keyboard': [[{'text': '✖️ Закрыть', 'callback_data': f'Главное'}]]})
						response = requests.post(
							url='https://api.telegram.org/bot{0}/{1}'.format(TOKEN, "sendAnimation"),
							data={'chat_id': jobid,'animation': str(media), 'caption': str(text_send_all),'reply_markup': str(reply),'parse_mode': 'HTML'}
						).json()
						if response['ok'] == False:
							colvo_dont_send_message_users = colvo_dont_send_message_users + 1
						else:
							colvo_send_message_users = colvo_send_message_users + 1;
					bot.send_message(message.chat.id, 'Отправлено сообщений: '+ str(colvo_send_message_users)+'\nНе отправлено: '+ str(colvo_dont_send_message_users))	


				elif int(tipsendSSSSS) == 3: # видео
					q.execute("SELECT * FROM ugc_users")
					row = q.fetchall()
					for i in row:
						jobid = i[0]
						time.sleep(0.2)
						response = requests.post(
							url='https://api.telegram.org/bot{0}/{1}'.format(TOKEN, "sendMessage"),
							data={'chat_id': jobid, 'text': str(text_send_all) + str(media),'parse_mode': 'HTML'}
						).json()
						if response['ok'] == False:
							colvo_dont_send_message_users = colvo_dont_send_message_users + 1
						else:
							colvo_send_message_users = colvo_send_message_users + 1;
					bot.send_message(message.chat.id, 'Отправлено сообщений: '+ str(colvo_send_message_users)+'\nНе отправлено: '+ str(colvo_dont_send_message_users))					

def add_money2(message):
   if message.text != 'Отмена':
      connection = sqlite3.connect('spam_baza.sqlite')
      q = connection.cursor()
      q.execute(f"update ugc_users set balance = '{message.text}' where id = '{id_user_edit_bal1}'")
      connection.commit()
      bot.send_message(message.chat.id, 'Успешно!  | /admin',parse_mode='HTML')
   else:
      bot.send_message(message.chat.id, 'Вернулись в админку | /admin',parse_mode='HTML')

def searchuser(message):
	if message.text.lower() != 'отмена':
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		q.execute(f"SELECT * FROM ugc_users where id = '{message.text}'")
		row = q.fetchone()
		bot.send_message(message.chat.id, '<b>🔍 Ищем...</b>',parse_mode='HTML', reply_markup=keyboards.main)
		if row != None:
			saasssss = q.execute(f"SELECT COUNT(id) FROM akk where user = '{row[0]}'").fetchone()[0]
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text='➕ Обновить баланс',callback_data=f'добавитьбаланс_{row[0]}'))
			msg = bot.send_message(message.chat.id, f'''<b>Подробнее:</b>
<b>Ид:</b> <code>{row[0]}</code>
<b>Баланс:</b> <code>{row[1]}</code>
<b>Аккаунтов:</b> <code>{saasssss}</code>
<b>Подписка:</b> <code>{row[5]}</code>

''',parse_mode='HTML',reply_markup=keyboard)
		else:
			bot.send_message(message.chat.id, '<b>Нет такого пользователя</b> | /admin',parse_mode='HTML')
	else:
		bot.send_message(message.chat.id, '<b>Отменили</b> | /admin',parse_mode='HTML')

def add_proxi(message):
	if message.text != '🎛 Меню':
		try:
			proxi = message.text
			login_prox = proxi.split('@')[0].split(':')[0]
			pass_prox = proxi.split('@')[0].split(':')[1]
			ip_prox = proxi.split('@')[1].split(':')[0]
			port_prox = proxi.split('@')[1].split(':')[1]
			connection = sqlite3.connect('spam_baza.sqlite')
			q = connection.cursor()
			akkkkkkk = q.execute(f'SELECT akk FROM ugc_users where id =  "{message.chat.id}"').fetchone()[0]
			q.execute(f"update akk set proxi = '{proxi}' where id = '{akkkkkkk}'")
			connection.commit()
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
			bot.send_message(message.chat.id,F'''✔️ Успешно сменили прокси''',parse_mode='HTML', reply_markup=keyboard)
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
			bot.send_message(message.chat.id,f'✖️ Ошибка формата',parse_mode='HTML', reply_markup=keyboard)
	else:
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
		bot.send_message(message.chat.id, '✔️ Вернулись на главную',reply_markup=keyboard)


def add_autotext(message):
	if message.text != '🎛 Меню':
		try:
			connection = sqlite3.connect('spam_baza.sqlite')
			q = connection.cursor()
			akkkkkkk = q.execute(f'SELECT akk FROM ugc_users where id =  "{message.chat.id}"').fetchone()[0]
			q.execute(f"update akk set text = '{message.text}' where id = '{akkkkkkk}'")
			connection.commit()
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Автоответчик'))
			bot.send_message(message.chat.id,F'''✔️ Успешно сменили''',parse_mode='HTML', reply_markup=keyboard)
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Автоответчик'))
			bot.send_message(message.chat.id,f'✖️ Ошибка формата',parse_mode='HTML', reply_markup=keyboard)
	else:
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Автоответчик'))
		bot.send_message(message.chat.id, '✔️ Вернулись на главную',reply_markup=keyboard)


def proxis(id_akk):
    connection = sqlite3.connect('spam_baza.sqlite')
    q = connection.cursor()
    proxi = q.execute(f'SELECT proxi FROM akk where id =  "{id_akk}"').fetchone()[0]
    return proxi

@bot.callback_query_handler(func=lambda call:True)
def podcategors(call):

	if call.data[:19] == 'Check_Depozit_qiwi_':
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		if p2p.check(bill_id=call.data[19:]).status == "PAID":
			bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
			q.execute(f"update ugc_users set balance = balance + '{p2p.check(bill_id=call.data[19:]).amount}' where id = '{call.message.chat.id}'")
			connection.commit()
			bot.send_message(call.message.chat.id, f"✔️ Баланс успешно пополнен !",parse_mode='HTML', reply_markup=keyboards.main)
			bot.send_message(admin, f'#Новая оплата |  {p2p.check(bill_id=call.data[19:]).amount} RUB | <a href="tg://user?id={call.message.chat.id}">{call.message.chat.first_name}</a>',parse_mode='HTML')
		
		else:
			bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="⚠ Оплата не найдена!")

	if call.data == 'akks':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')	
		q = connection.cursor()
		keyboard = types.InlineKeyboardMarkup()
		row = q.execute(f"SELECT * FROM akk where user = '{call.message.chat.id}'").fetchall()
		keyboard = types.InlineKeyboardMarkup()
		for i in row:
			keyboard.add(types.InlineKeyboardButton(text=i[2],callback_data=f'список{i[0]}'))
		keyboard.add(types.InlineKeyboardButton(text='➕ Добавить аккаунт',callback_data=f'добавитьаккаунт'))
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Главное'))
		bot.send_message(call.from_user.id,  f'''◾️ Выберите нужный аккаунт или добавьте новый:''',parse_mode='HTML', reply_markup=keyboard)
		
	if call.data == 'Автоответчик':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')	
		q = connection.cursor()
		keyboard = types.InlineKeyboardMarkup()
		row = q.execute(f"SELECT * FROM akk where user = '{call.message.chat.id}'").fetchall()
		keyboard = types.InlineKeyboardMarkup()
		for i in row:
			keyboard.add(types.InlineKeyboardButton(text=i[2],callback_data=f'автоответ{i[0]}'))
		keyboard.add(types.InlineKeyboardButton(text='➕ Добавить аккаунт',callback_data=f'добавитьаккаунт'))
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Главное'))
		bot.send_message(call.from_user.id,  f'''◾️ Выберите нужный аккаунт или добавьте новый:''',parse_mode='HTML', reply_markup=keyboard)

	if call.data[:9] == 'автоответ':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		datas = q.execute(f"SELECT data FROM ugc_users where id = '{call.message.chat.id}'").fetchone()[0]
		if str(datas) != str('Нет'):
			q.execute(f"update ugc_users set akk = '{call.data[9:]}' where id = '{call.message.chat.id}'")
			connection.commit()
			akk_akk = q.execute(f'SELECT akk FROM ugc_users where id =  "{call.message.chat.id}"').fetchone()[0]
			proxi = q.execute(f'SELECT proxi FROM akk where id =  "{akk_akk}"').fetchone()[0]
			status_auto = q.execute(f'SELECT auto FROM akk where id =  "{akk_akk}"').fetchone()[0]
			text_auto = q.execute(f'SELECT text FROM akk where id =  "{akk_akk}"').fetchone()[0]
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''💬 Смена текста''',callback_data=f'текста'),types.InlineKeyboardButton(text=f'''💡Вкл/Выкл автоответчик''',callback_data=f'вклавтооответчик'))
			keyboard.add(types.InlineKeyboardButton(text=f'''🌏 Смена прокси''',callback_data=f'сменапрокси'),types.InlineKeyboardButton(text=f'''🗑 Удалить аккаунт''',callback_data=f'del_akk'))
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
			bot.send_message(call.message.chat.id, f'''▪️ Прокси: {proxi}
	▪️ Текст автооответчика: {text_auto}
	▪️ Статус: {status_auto}''',parse_mode='HTML', reply_markup=keyboard)
		else:
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'),)
			bot.send_message(call.message.chat.id, f'''✖️ Подписка отсутствует''',parse_mode='HTML', reply_markup=keyboard)


	if call.data == 'текста':
		msg = bot.send_message(call.message.chat.id,'ℹ️ Введите текст автоответчика:',parse_mode='HTML', reply_markup=keyboards.main)
		bot.register_next_step_handler(msg, add_autotext)
	if call.data=='spamspam':
		chat_id=call.message.chat.id
		msg = bot.send_message(chat_id=chat_id,
                               text='Введите текст для рассылки. \n\nДля отмены напишите "-" без кавычек!')
		bot.register_next_step_handler(msg, message1)

	if call.data == 'вклавтооответчик':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		akk_akk = q.execute(f'SELECT akk FROM ugc_users where id =  "{call.message.chat.id}"').fetchone()[0]
		status_auto = q.execute(f'SELECT auto FROM akk where id =  "{akk_akk}"').fetchone()[0]
		if str(status_auto) == str('Выключен'):
			q.execute(f"update akk set auto = 'Работает' where id = '{akk_akk}'")
			connection.commit()
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Автоответчик'))
			bot.send_message(call.message.chat.id,F'''✔️ Успешно включили''',parse_mode='HTML', reply_markup=keyboard)
		else:
			q.execute(f"update akk set auto = 'Выключен' where id = '{akk_akk}'")
			connection.commit()
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Автоответчик'))
			bot.send_message(call.message.chat.id,F'''✔️ Успешно выключили''',parse_mode='HTML', reply_markup=keyboard)





	if call.data == 'timeupdate':
		bot.send_message(call.from_user.id, 'Load' ,parse_mode='HTML')
		connection = sqlite3.connect('database.sqlite')
		q = connection.cursor()
		clock_in_half_hour = datetime.now()
		q.execute(f"SELECT * FROM list_chat where status = 'NoSend' and time >= '1'")
		row = q.fetchall()
		for i in row:
			try:
				ttt = datetime.now() + timedelta(minutes=(int(i[4])))
				q.execute(f"update list_chat set time_step = '{ttt.hour}:{ttt.minute}' where id_str = '{i[0]}'")
				connection.commit()
			except Exception as e:
				q.execute(f"DELETE FROM list_chat where id_str = '{i[0]}'")
				connection.commit()
	
		bot.send_message(call.from_user.id, f'''✔️ Time update /admin''',parse_mode='HTML')

	if call.data == 'restartsssss':
		bot.send_message(call.message.chat.id, '<b>Reboot...</b>',parse_mode='HTML')
		cmd = 'systemctl restart avp'
		cmd1 = 'systemctl restart avp_autos'
		cmd2 = 'systemctl restart avp_bot_auch'
		cmd3 = 'systemctl restart avp_ids_spam'
		cmd4 = 'systemctl restart avp_send_1'
		subprocess.Popen(cmd3, shell=True)
		subprocess.Popen(cmd1, shell=True)
		subprocess.Popen(cmd2, shell=True)
		subprocess.Popen(cmd4, shell=True)
		subprocess.Popen(cmd, shell=True)


	
	if call.data[:6] == 'список':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		datas = q.execute(f"SELECT data FROM ugc_users where id = '{call.message.chat.id}'").fetchone()[0]
		if str(datas) != str('Нет'):
			q.execute(f"update ugc_users set akk = '{call.data[6:]}' where id = '{call.message.chat.id}'")
			connection.commit()
			akk_akk = q.execute(f'SELECT akk FROM ugc_users where id =  "{call.message.chat.id}"').fetchone()[0]
			proxi = q.execute(f'SELECT proxi FROM akk where id =  "{akk_akk}"').fetchone()[0]
			keyboard = types.InlineKeyboardMarkup()
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			rows = q.execute(f"SELECT * FROM list_chat  where akk = '{akk_akk}'").fetchall()
			btns = []
			for i in range(len(rows)):
				btns.append(types.InlineKeyboardButton(text=rows[i][3], callback_data=f'servis_{rows[i][0]}'))
			while btns != []:
				try:
					keyboard.add(
						btns[0],
						btns[1]
						)
					del btns[1], btns[0]
				except:
					keyboard.add(btns[0])
					del btns[0]

			keyboard.add(types.InlineKeyboardButton(text=f'''🔄  Загрузить чаты с аккаунта''',callback_data=f'loading_akk'))
			keyboard.add(types.InlineKeyboardButton(text=f'''🌏 Смена прокси''',callback_data=f'сменапрокси'),types.InlineKeyboardButton(text=f'''🗑 Удалить аккаунт''',callback_data=f'del_akk'))
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'),types.InlineKeyboardButton(text=f'''📚 Multi settings''',callback_data=f'Multi'))
			bot.send_message(call.message.chat.id, f'''🌐 Прокси: {proxi}''',parse_mode='HTML', reply_markup=keyboard)
		else:
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'),)
			bot.send_message(call.message.chat.id, f'''✖️ Подписка отсутствует''',parse_mode='HTML', reply_markup=keyboard)


	if call.data == 'loading_akk':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		bot.send_message(call.message.chat.id, f'🔄 Загружаем, пожалуйста ожидайте.',reply_markup=keyboards.main)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		akk_akk = q.execute(f'SELECT akk FROM ugc_users where id =  "{call.message.chat.id}"').fetchone()[0]
		www = chat_list.mainssssss(akk_akk, call.message.chat.id)
		if str(www) == str('ok'):
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
			bot.send_message(call.message.chat.id, f'''✔️ Чаты успешно добавлены.

⚠️ Для получения логов у вас должен быть запущен бот: @Quik_Log_Bot''',reply_markup=keyboard)
		else:
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
			bot.send_message(call.message.chat.id, f'✖️ Ошибка аккаунта.',reply_markup=keyboard)


	if call.data == 'сменапрокси':
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text=f'''📜 Инструкция''',url='https://telegra.ph/Dobavlyaem-proksi-06-28'),types.InlineKeyboardButton(text=f'''➕ Купить прокси''',url='https://www.proxy.house/?r=65634'))
		msg = bot.send_message(call.message.chat.id,'ℹ️ Введите прокси в формате: login:password@ip:port (SOCKS)',parse_mode='HTML', reply_markup=keyboard)
		bot.register_next_step_handler(msg, add_proxi)

		
	if call.data == 'del_akk':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		akk_akkass = q.execute(f'SELECT akk FROM ugc_users where id =  "{call.message.chat.id}"').fetchone()[0]
		connection = sqlite3.connect('database.sqlite')
		q = connection.cursor()
		q.execute(f"DELETE FROM list_chat where akk = '{akk_akkass}'")
		connection.commit()
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		q.execute(f"DELETE FROM akk where id = '{akk_akkass}'")
		connection.commit()
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
		bot.send_message(call.from_user.id,  f'''✔️ Аккаунт успешно удален''',parse_mode='HTML', reply_markup=keyboard)


	if call.data == 'добавитьаккаунт':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')	
		q = connection.cursor()
		datas = q.execute(f"SELECT data FROM ugc_users where id = '{call.message.chat.id}'").fetchone()[0]
		if str(datas) != str('Нет'):
			code = call.message.chat.id
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''🌐 Перейти''',url=f'https://t.me/t34oijt34bot?start={code}'))
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
			bot.send_message(call.message.chat.id, f'''ℹ️ Перейдите в бот  <a href="https://t.me/t34oijt34bot?start={code}">ссылке</a> и пройдите авторизацию следуйте дальнейшим инструкциям.''',parse_mode='HTML', reply_markup=keyboard)
		else:
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
			bot.send_message(call.from_user.id,  f'''✖️ У вас нет подписки''',parse_mode='HTML', reply_markup=keyboard)





	if call.data[:7] == 'servis_':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')	
		q = connection.cursor()
		q.execute(f"update ugc_users set chat = '{call.data[7:]}' where id = '{call.message.chat.id}'")
		connection.commit()
		chat_chat = q.execute(f'SELECT chat FROM ugc_users where id =  "{call.message.chat.id}"').fetchone()[0]
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text='Сменить текст',callback_data=f'настройка{1}'),types.InlineKeyboardButton(text='Сменить доп текст',callback_data=f'настройка{6}'))
		keyboard.add(types.InlineKeyboardButton(text='Сменить фото',callback_data=f'настройка{4}'),types.InlineKeyboardButton(text='Сменить задержку',callback_data=f'настройка{2}'))
		keyboard.add(types.InlineKeyboardButton(text='Назад',callback_data=f'akks'),types.InlineKeyboardButton(text='Удалить',callback_data=f'настройка{3}'))
		connection = sqlite3.connect('database.sqlite')
		q = connection.cursor()
		row = q.execute(f"SELECT * FROM list_chat where id_str = '{chat_chat}'").fetchone()
		bot.send_message(call.from_user.id,  f'''▪️ Id: <code>{row[1]}</code>
▪️ Текст: <code>{row[2]}</code>
▪️ Доп текст: <code>{row[11]}</code>
▪️ Картинка: <code>{row[6]}</code> (ссылка)
▪️ Задержка: <code>{row[4]}</code> минут
▪️ Отправка: <code>{row[5]}</code>''',parse_mode='HTML', reply_markup=keyboard)
		clock_in_half_hour = datetime.now()
		bot.send_message(call.from_user.id,  f'''
▪️ Текушие время сервера: <code>{clock_in_half_hour}</code>''',parse_mode='HTML', reply_markup=keyboards.main)


	if call.data == 'send_sms_bot':
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text='С картинокй',callback_data=f'Рассылка{1}'))
		keyboard.add(types.InlineKeyboardButton(text='С гиф',callback_data=f'Рассылка{2}'))
		keyboard.add(types.InlineKeyboardButton(text='С видео',callback_data=f'Рассылка{3}'))
		bot.send_message(call.from_user.id, f'''как будем рассылкать ?''',parse_mode='HTML', reply_markup=keyboard)

	if call.data[:8] == 'Рассылка':
		global tipsendSSSSS
		tipsendSSSSS = call.data[8:]
		msg= bot.send_message(call.message.chat.id, "<b>Введи текст для рассылки</b>",parse_mode='HTML')
		bot.register_next_step_handler(msg, send_photoorno)	


	if call.data == 'Multi':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text='Сменить текст',callback_data=f'мульти{1}'))
		keyboard.add(types.InlineKeyboardButton(text='Сменить фото',callback_data=f'мульти{4}'))
		keyboard.add(types.InlineKeyboardButton(text='Назад',callback_data=f'akks'))
		bot.send_message(call.from_user.id,  f'''▪️Смена информации по всем чатам аккаунта:''',parse_mode='HTML', reply_markup=keyboard)

	

	
	if call.data[:6] == 'мульти':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		global tipsend11
		tipsend11 = call.data[6:]
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		if int(tipsend11) == 1:
			msg= bot.send_message(call.message.chat.id, "<b>Введи новое значение:</b>",parse_mode='HTML')
			bot.register_next_step_handler(msg, new_data_m)
		if int(tipsend11) == 4:
			msg= bot.send_message(call.message.chat.id, "<b>Введи новое значение:</b>",parse_mode='HTML')
			bot.register_next_step_handler(msg, new_data_m)


	elif call.data[:9] == 'настройка':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		global tipsend
		tipsend = call.data[9:]
		print(tipsend)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		if int(tipsend) == 1:
			msg= bot.send_message(call.message.chat.id, "<b>Введи новое значение:</b>",parse_mode='HTML')
			bot.register_next_step_handler(msg, new_data)
		if int(tipsend) == 2:
			msg= bot.send_message(call.message.chat.id, "<b>Введи новое значение:</b>",parse_mode='HTML')
			bot.register_next_step_handler(msg, new_data)
		if int(tipsend) == 3:
			chat_chat = q.execute(f'SELECT chat FROM ugc_users where id =  "{call.message.chat.id}"').fetchone()[0]
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			q.execute(f"DELETE FROM list_chat where id_str = '{chat_chat}'")
			connection.commit()
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'))
			bot.send_message(call.from_user.id,  '''✔️ Готово''',parse_mode='HTML', reply_markup=keyboard)
		if int(tipsend) == 4:
			msg= bot.send_message(call.message.chat.id, "<b>Введите ссылку на фото:</b>",parse_mode='HTML')
			bot.register_next_step_handler(msg, new_data)
		if int(tipsend) == 5:
			keyboard = types.InlineKeyboardMarkup()
			akk_akk = q.execute(f'SELECT akk FROM ugc_users where id =  "{call.message.chat.id}"').fetchone()[0]
			print(akk_akk)
			keyboard = types.InlineKeyboardMarkup()
			connection = sqlite3.connect('database.sqlite')
			q = connection.cursor()
			rows = q.execute(f"SELECT * FROM list_chat  where akk = '{akk_akk}'").fetchall()
			btns = []
			for i in range(len(rows)):
				btns.append(types.InlineKeyboardButton(text=rows[i][3], callback_data=f'servis_{rows[i][0]}'))

			while btns != []:
				try:
					keyboard.add(
						btns[0],
						btns[1]
						)

					del btns[1], btns[0]

				except:
					keyboard.add(btns[0])
					del btns[0]
			clock_in_half_hour = datetime.now()
			keyboard.add(types.InlineKeyboardButton(text=f'''🔄  Загрузить чаты с аккаунта''',callback_data=f'loading_akk'))
			keyboard.add(types.InlineKeyboardButton(text=f'''🌏 Смена прокси''',callback_data=f'сменапрокси'),types.InlineKeyboardButton(text=f'''🗑 Удалить аккаунт''',callback_data=f'del_akk'))
			keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'akks'),types.InlineKeyboardButton(text=f'''📚 Multi settings''',callback_data=f'Multi'))
		if int(tipsend) == 6:
			msg= bot.send_message(call.message.chat.id, "<b>Введи новое значение:</b>",parse_mode='HTML')
			bot.register_next_step_handler(msg, new_data)
				
	elif call.data == 'qiwi_smena':
		msg= bot.send_message(call.message.chat.id, "<b>Укажите токен p2p qiwi</b>",parse_mode='HTML')
		bot.register_next_step_handler(msg, new_tig)

	elif call.data == 'Главное':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		keyboard = types.InlineKeyboardMarkup()
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text=f'''⏳ Автопостинг''',callback_data=f'akks'),types.InlineKeyboardButton(text=f'''💬 Автоответчик''',callback_data=f'Автоответчик'))
		keyboard.add(types.InlineKeyboardButton(text=f'''🖥 Профиль''',callback_data=f'profale'),types.InlineKeyboardButton(text=f'''📖 Информация''',callback_data=f'info'))
		bot.send_message(call.message.chat.id, f'''◾️ Выберите нужный пункт меню:''',parse_mode='HTML', reply_markup=keyboard)


	elif call.data == 'profale':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		balans = q.execute(f"SELECT balance FROM ugc_users where id = '{call.message.chat.id}'").fetchone()[0]
		data = q.execute(f"SELECT data FROM ugc_users where id = '{call.message.chat.id}'").fetchone()[0]
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text=f'''💰 Пополнить баланс''',callback_data='Пополнить'))
		keyboard.add(types.InlineKeyboardButton(text=f'''🔓 Оформить подписку''',callback_data='Оформить'))
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Главное'))
		bot.send_message(call.message.chat.id, f'''
▪️ id: <code>{call.message.chat.id}</code>
▪️ Баланс: <code>{balans}</code>
▪️ Подписка до: <code>{data}</code>''',parse_mode='HTML', reply_markup=keyboard)

	elif call.data == 'Пополнить':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text=f'''▪️ QIWI / CARD''',callback_data='бткчек'))
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'profale'))
		bot.send_message(call.message.chat.id, f'''▪️ Выберите способ для депозита:''',parse_mode='HTML', reply_markup=keyboard)

	elif call.data == 'бткчек':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		msg = bot.send_message(call.message.chat.id,'''▪️ Укажите сумму пополнения:''', reply_markup=keyboards.main, parse_mode='HTML')
		bot.register_next_step_handler(msg, btc_oplata_1)

	elif call.data == 'Оформить':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text=f'''◾️ Тест / Сутки / 50р''',callback_data=f'подписка1'))
		keyboard.add(types.InlineKeyboardButton(text=f'''◾️ 1 месяц / 500р''',callback_data=f'подписка2'))
		keyboard.add(types.InlineKeyboardButton(text=f'''◾️ 3 месяц / 1200р''',callback_data=f'подписка3'))
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Главное'))
		bot.send_message(call.message.chat.id, '''◾️ Выберите подписку:''',parse_mode='HTML', reply_markup=keyboard)

	elif call.data[:8] == 'подписка':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		temp_id = call.data[8:]
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		bal_us = q.execute(f"SELECT balance FROM ugc_users where id = '{call.from_user.id}'").fetchone()[0]
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Главное'))
		if str(temp_id) == '1':
			if int(bal_us) >= int(50):
				q.execute("update ugc_users set balance = balance - " + str(50)+" where id = " +str(call.from_user.id))
				connection.commit()
				tomorrow = datetime.now() + timedelta(days=1)
				tomorrow_formatted = tomorrow.strftime('%d/%m/%Y')
				print(tomorrow_formatted)
				q.execute(f"update ugc_users set data = '{tomorrow_formatted}' where id = '{call.from_user.id}'")
				connection.commit()
				bot.send_message(call.message.chat.id, '''✔️ Подписка оформлена''',parse_mode='HTML', reply_markup=keyboard)
			else:
				bot.send_message(call.message.chat.id, '''✖️ Пополните баланс''',parse_mode='HTML', reply_markup=keyboard)

		if str(temp_id) == '2':
			if int(bal_us) >= int(500):
				q.execute("update ugc_users set balance = balance - " + str(500)+" where id = " +str(call.from_user.id))
				connection.commit()
				tomorrow = datetime.now() + timedelta(days=30)
				tomorrow_formatted = tomorrow.strftime('%d/%m/%Y')
				q.execute(f"update ugc_users set data = '{tomorrow_formatted}' where id = '{call.from_user.id}'")
				connection.commit()
				bot.send_message(call.message.chat.id, '''✔️ Подписка оформлена''',parse_mode='HTML', reply_markup=keyboard)
			else:
				bot.send_message(call.message.chat.id, '''✖️ Пополните баланс''',parse_mode='HTML', reply_markup=keyboard)

		if str(temp_id) == '3':
			if int(bal_us) >= int(1200):
				q.execute("update ugc_users set balance = balance - " + str(1200)+" where id = " +str(call.from_user.id))
				connection.commit()
				tomorrow = datetime.now() + timedelta(days=90)
				tomorrow_formatted = tomorrow.strftime('%d/%m/%Y')
				q.execute(f"update ugc_users set data = '{tomorrow_formatted}' where id = '{call.from_user.id}'")
				connection.commit()
				bot.send_message(call.message.chat.id, '''✔️ Подписка оформлена''',parse_mode='HTML', reply_markup=keyboard)
			else:
				bot.send_message(call.message.chat.id, '''✖️ Пополните баланс''',parse_mode='HTML', reply_markup=keyboard)


	elif call.data == 'info':
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		connection = sqlite3.connect('spam_baza.sqlite')
		q = connection.cursor()
		akkakk = q.execute(f'SELECT COUNT(id) FROM akk').fetchone()[0]
		connection = sqlite3.connect('database.sqlite')
		q = connection.cursor()
		chat = q.execute(f'SELECT COUNT(id) FROM list_chat').fetchone()[0]
		colvo_send = q.execute(f'SELECT SUM(colvo_send) FROM list_chat').fetchone()[0]
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton(text=f'''🧑‍🔧 Поддержка''',url=f'https://t.me/MoreScr1pts'))
		keyboard.add(types.InlineKeyboardButton(text=f'''⬅️ Назад''',callback_data=f'Главное'))
		bot.send_message(call.message.chat.id, f'''📖 Подробная информация по боту:
▪️ https://telegra.ph/Info-07-12-56

📊 Статистика бота:
▪️Аккаунтов: {akkakk}
▪️Чатов: {chat}
▪️Отправлено: {colvo_send}''',parse_mode='HTML', reply_markup=keyboard)

	elif call.data[:17] == 'admin_search_user':
		msg = bot.send_message(call.message.chat.id, f'<b>Введи id пользователя</b>',parse_mode='HTML', reply_markup=keyboards.otmena)
		bot.register_next_step_handler(msg,searchuser)

	elif call.data[:15] == 'добавитьбаланс_':
		global id_user_edit_bal1
		id_user_edit_bal1 = call.data[15:]
		msg = bot.send_message(call.message.chat.id, 'Введи сумму: ',parse_mode='HTML')
		bot.register_next_step_handler(msg, add_money2)



bot.polling(True)
