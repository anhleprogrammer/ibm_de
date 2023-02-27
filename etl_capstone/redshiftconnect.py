import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

# Set the connection parameters
dbname = os.getenv('DB_NAME')
host = os.getenv('HOST')
port = os.getenv('PORT')
user = os.getenv('RSUSER')
password = os.getenv('RSPASSWORD')


# Connect to the cluster
def connectRedshift():
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            host=host,
            port=port,
            user=user,
            password=password
        )
        print('Connected')
        return conn
    except psycopg2.Error as e:
        print('Unable to connect!')


conn = connectRedshift()
cur = conn.cursor()
# create table

SQL = """CREATE TABLE IF NOT EXISTS sales_data(rowid INTEGER PRIMARY KEY NOT NULL,product_id INTEGER NOT NULL,category_id INTEGER NOT NULL, quantity INTEGER NOT NULL)"""
cur.execute(SQL)
conn.commit()
print("Table created")


# query data
def getAllRecords():
    SQL = "SELECT * FROM sales_data"
    cur.execute(SQL)
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No records")
    else:
        for row in rows:
            print(row)


# close connection
cur.close()
conn.close()
