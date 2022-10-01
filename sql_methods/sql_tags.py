import mysql.connector
#from config import host,user,password, db_name,port

global slovar
slovar = {
    'log'  :  'BIGINT',
    'name' : 'TEXT',
    'description' : 'TEXT',
    'photo' : 'TEXT',
    'BirthDate' : 'TEXT',
    'faculty' : 'TEXT',
    'group_' : 'TEXT',
    'course' : 'INT'
}

host = 'localhost'
user = 'root'
password = 'root'
db_name = 'komitet'
port = 3306



def create_sub_list(list_name, columns):
    connection = mysql.connector.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='root',
            database='komitet'
        )
    cursor = connection.cursor()
    try:
        table_name = 'sublist' + str(list_name)
        create_querry = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ('
        arr = columns.split('/')
        for i in range (0, len(arr)):
            if i == len(arr) - 1:
                create_querry += arr[i] + ' ' + slovar[arr[i]] + ')'
                break
            create_querry += arr[i] + ' ' + slovar[arr[i]] + ','
        cursor.execute(create_querry)
        connection.commit()
    finally:
        connection.close()


create_sub_list(100, 'log/photo/name/course')
