import sqlite3
import datetime
import time
from datetime import datetime, timedelta
import re



while True:
	connection = sqlite3.connect('database.sqlite')
	q = connection.cursor()
	clock_in_half_hour = datetime.now()
	q.execute(f"SELECT * FROM list_chat where time_step = '{clock_in_half_hour.hour}:{clock_in_half_hour.minute}' and status = 'NoSend'")
	row = q.fetchall()
	for i in row:
		try:
			clock_in_half_hour = datetime.now() + timedelta(minutes=(int(i[4])))
			q.execute(f"update list_chat set time_step = '{clock_in_half_hour.hour}:{clock_in_half_hour.minute}' where id_str = '{i[0]}'")
			connection.commit()
			q.execute(f"update list_chat set status = 'Send' where id_str = '{i[0]}'")
			connection.commit()
		except Exception as e:
			q.execute(f"DELETE FROM list_chat where id_str = '{i[0]}'")
			connection.commit()
			