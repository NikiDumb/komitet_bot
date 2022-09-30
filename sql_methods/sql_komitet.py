import mysql.connector
from config import host,user,password, db_name,port
from datetime import datetime

async def add_komitet_user(log):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT * FROM komitet_users WHERE id = %s",[log])
		if cursor.fetchone() is not None:
			return 606
		else:
			cursor.execute("INSERT INTO komitet_users(id) VALUES (%s)", [log])
			connection.commit()
			return 1
	finally:
		connection.close()




#################################################################################################################
#удалить администратора, id передается как число, пример : await delete_admin(Ваш id)
#################################################################################################################
async def delete_komitet_user(name):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT id FROM komitet_users WHERE name = %s", [name])
		if cursor.fetchone() is None:
			return 404
		else:
			cursor.execute("DELETE FROM komitet_users WHERE name = %s", [name])
			connection.commit()
			return 1
	finally:
		connection.close()

#################################################################################################################
#авторизация, логин передается как число, пример : await log_in(Ваш логин)
#################################################################################################################
async def log_in(log):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT id FROM komitet_users WHERE id = %s", [log])
		if cursor.fetchone() is None:
			return 404
		else:
			return 1
	finally:
		connection.close()


async def extract_komitet_users_name(division):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT name FROM komitet_users WHERE division = %s", [division])
		if cursor.fetchone() is not None:
			return cursor.fetchone()
		else:
			return 404
	finally:
		connection.close()

async def extract_komitet_users_id(division):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT id FROM komitet_users WHERE division = %s", [division])
		if len(cursor.fetchall()) > 0:
			return cursor.fetchall()
		else:
			return 404
	finally:
		connection.close()

async def extract_komitet_users(division):
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT * FROM komitet_users WHERE division = %s", [division])
		if len(cursor.fetchall()) > 0:
			return cursor.fetchall()
		else:
			return 404
	finally:
		connection.close()


async def extract_komitet_users_division():
	connection = mysql.connector.connect(
			host=host,
			port = port,
			user=user,
			passwd=password,
			database=db_name
        )
	cursor = connection.cursor()
	try:
		cursor.execute("SELECT division FROM komitet_users")
		if len(cursor.fetchall()) > 0:
			return cursor.fetchall()
		else:
			return 404
	finally:
		connection.close()
