import mysql.connector
from config import host,user,password, db_name,port


def TagsProcess(SomeText, SomeWords):
	a = 'хэштеги :'
	for i in range(0, len(SomeWords)):
		if (SomeText.lower()).find(SomeWords[i])>0:
			a+=(' #'+SomeWords[i]) 
	print (f'{InputText}\n{a}')

async def extract_tags(text_):
    connection = mysql.connector.connect(
            host=host,
            port = port,
            user=user,
            passwd=password,
            database=db_name
        )
    cursor = connection.cursor()
    try:
        date_now = datetime.now()
        cursor.execute("DELETE FROM events WHERE e_date < (%s)", [date_now])
    finally:
        connection.close()