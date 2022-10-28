import sqlite3
from SimpleQIWI import *

Product = []

# Переменные / функции
bot_token = ''		# 
admin_user_id = 838383838										#  
channel_id = -773838383									# 

token = 'a4313ec5642e3f0b7a6cee5f3d5db7fd' 							# qiwi token
phone = '79644928352'												# qiwi number

secret = ''   # CRYSTAL PAY SECRET 1
login = ''    # CRYSTAL PAY LOGIN


manager = "" # username мэнеджера без @
group = "@otziv_vaper" # канал с отзывами, готовый вариант, можно оставить

bot_name = "" #username бота без @

Product = []


def found_worker(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
			boolean = bool(len(result))
			if (boolean == True):
				for row in result:
					return row[4]
			else:
				return 0
	except:
		pass

def name_from_id(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
			boolean = bool(len(result))
			if (boolean == True):
				for row in result:
					return row[2]
			else:
				return 0
	except:
		pass

def user_delete_bill(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			cur.execute("DELETE FROM `bill_id` WHERE `user_id` = ?", (user_id,))
	except:
		pass

def user_bill_id(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `bill_id` WHERE `user_id` = ?', (user_id,)).fetchall()
			boolean = bool(len(result))
			if (boolean == True):
				for row in result:
					return row[1]
			else:
				return 0
	except:
		pass

def user_exists_bill(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `bill_id` WHERE `user_id` = ?', (user_id,)).fetchall()
			return bool(len(result))
	except:
		pass

def create_bill_id(user_id, bill_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO `bill_id` (`user_id`, `bill`) VALUES(?,?)", (user_id, bill_id))
	except:
		pass		

def user_referals(user_id):
	try:
		array = []
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `users` WHERE `referal` = ?', (user_id,)).fetchall()
			boolean = bool(len(result))
			if boolean == True:
				for row in result:
					array.append(str(row[1]))
				return array
			else:
				return "0"
	except:
		pass

def user_count_ref(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
			boolean = bool(len(result))
			if (boolean == True):
				for row in result:
					return row[5]
			else:
				return 0
	except:
		pass

def user_exists(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
			return bool(len(result))
	except:
		pass

def user_update_referal(user_id, worker):		
	try:
		balance = user_balance(user_id) + 50
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			cur.execute("UPDATE `users` SET `referal` = ? WHERE `user_id` = ?", (worker, user_id))
			cur.execute("UPDATE `users` SET `balance` = ? WHERE `user_id` = ?", (balance, user_id))
			cur.execute("UPDATE `users` SET `referal_count` = referal_count + ? WHERE `user_id` = ?", (1, worker))
	except:
		pass	

def user_add(user_id, user_name):
	try:
		if (user_name == None):
			user_name = 'none'

		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO `users` (`user_id`, `user_name`, `balance`, `referal`, `referal_count`) VALUES(?,?,?,?,?)", (user_id, user_name, 0, 0, 0))
	except:
		pass

def user_add_ref(user_id, user_name, referal):
	try:
		count = user_count_ref(referal) + 1
		if (user_name == None):
			user_name = 'none'

		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO `users` (`user_id`, `user_name`, `balance`, `referal`, `referal_count`) VALUES(?,?,?,?,?)", (user_id, user_name, 50, referal, 0))
			cur.execute("UPDATE `users` SET `referal_count` = ? WHERE `user_id` = ?", (count, referal))
	except:
		pass		

def user_balance(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
			for row in result:
				return row[3]
	except:
		return 0	

def get_price_from_name(name):
	if (name == "HQD Cuvie"):
		return 230
	elif (name == "HQD Stark"):
		return 230
	elif (name == "HQD V2"):
		return 230
	elif (name == "HQD Cuvie Plus"):
		return 450
	elif (name == "HQD Maxim"):
		return 230
	elif (name == "HQD Ultra Stick"):
		return 450
	elif (name == "Juul Promo Kit"):
		return 1499
	elif (name == "Juul Device Kit"):
		return 1750
	elif (name == "Juul Starter Kit"):
		return 1649
	elif ("x2 / x4" in name):
		return '395 / 695'
	elif ("2" in name):
		return 395
	elif ("4" in name):
		return 695

def user_update_balance(user_id, value):
	try:
		balance = user_balance(user_id) + value
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			cur.execute("UPDATE `users` SET `balance` = ? WHERE `user_id` = ?", (balance, user_id))
	except:
		pass		

def user_un_balance(user_id, value):
	balance = user_balance(user_id)
	try:
		if (balance < value):
			return False
		else:
			balance = balance - value
			with sqlite3.connect("evidence.db") as con:
				cur = con.cursor()
				cur.execute("UPDATE `users` SET `balance` = ? WHERE `user_id` = ?", (balance, user_id))
				return True
	except:
		return False

def referal(user_id):
	try:
		with sqlite3.connect("evidence.db") as con:
			cur = con.cursor()
			result = cur.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
			for row in result:
				return row[3]
	except:
		return 0	