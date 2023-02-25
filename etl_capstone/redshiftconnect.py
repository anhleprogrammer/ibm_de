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
try:
    conn = psycopg2.connect(
        dbname=dbname,
        host=host,
        port=port,
        user=user,
        password=password
    )
    print('Connected')
except psycopg2.Error as e:
    print('Unable to connect!')
