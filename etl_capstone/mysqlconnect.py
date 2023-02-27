import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()


def connectMysql():
    connection = mysql.connector.connect(
        user='root', password=os.getenv('MYSQL_PASS'), host='127.0.0.1', database='sales')

    if connection.is_connected():
        print('Connected')
    else:
        print('Failed to connect')
    return connection


# create cursor
connection = connectMysql()
cursor = connection.cursor()


def drop_table():
    SQL = """Drop table if exists products"""
    cursor.execute(SQL)
    print("Table dropped")


# create table
drop_table()


def create_table():
    SQL = """CREATE TABLE IF NOT EXISTS products(

	rowid int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	product varchar(255) NOT NULL,
	category varchar(255) NOT NULL

	)"""

    cursor.execute(SQL)

    print("Table created")

# insert data


def insert_data():
    SQL = """INSERT INTO products(product,category)
		VALUES
		("Television","Electronics"),
		("Laptop","Electronics"),
		("Mobile","Electronics")
		"""

    cursor.execute(SQL)
    # save changes
    connection.commit()


# query data
def getAllData():
    SQL = "SELECT * FROM products"

    cursor.execute(SQL)

    for row in cursor.fetchall():
        print(row)


# close connection
connection.close()
