import mysql.connector
import config

connection = mysql.connector.connect(
    user='root', password=config.auth_string, host='127.0.0.1', database='sales')

if connection.is_connected():
    print('Connected')
else:
    print('Failed to connect')

print(2)
