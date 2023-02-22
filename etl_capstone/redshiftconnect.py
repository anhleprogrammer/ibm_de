import psycopg2

# Set the connection parameters
dbname = 'dev'
host = ''
port = 5439
user = ''
password = ''

# Connect to the cluster
conn = psycopg2.connect(
    dbname=dbname,
    host=host,
    port=port,
    user=user,
    password=password
)
