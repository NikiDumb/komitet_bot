import mysql.connector
from config import host,user,password, db_name,port
from datetime import datetime


async def add_msg(filling, division, e_date, joined, image):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("INSERT INTO messages(filling, division, e_date, joined, image) VALUES (%s, %s, %s, %s, %s, )", [filling, division, e_date, joined, image]) 
		connection.commit()
		return 1
	finally:
		connection.close()

async def delete_msg(log):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT id FROM messages WHERE id = (%s)", [log])
		if cursor.fetchone() is not None:
			cursor.execute("DELETE FROM messages WHERE id = (%s)", [log])
			connection.commit()
			return 1
		else:
			return 404
		finally:
			connection.close()


async def extract_msg(log):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT * FROM messages WHERE id = (%s)", [log])
		result = cursor.fetchone()
		if result is None:
		return 404
		else:
			await delete_msg(log)
			return result

