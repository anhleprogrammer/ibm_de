# Import libraries required for connecting to mysql and redshift
import psycopg2
from mysqlconnect import connectMysql
from redshiftconnect import connectRedshift
from dotenv import load_dotenv
import os
load_dotenv()

# Connect to MySQL
mysqlConnect = connectMysql()
mysqlCur = mysqlConnect.cursor()

# Connect to Redshift
redshiftConnect = connectRedshift()
redshiftCur = redshiftConnect.cursor()
# Find out the last rowid from redshift data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the redshift database.


def get_last_rowid():
    SQL = """Select max(rowid) from sales_data"""
    redshiftCur.execute(SQL)
    result = redshiftCur.fetchone()
    last_rowid = result[0]
    print("Last row id on production datawarehouse = ", last_rowid)
    return last_rowid


# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.
last_rowid = get_last_rowid()


def get_latest_records(rowid):
    SQL = """Select rowid from sales_data s where rowid > %s"""
    mysqlCur.execute(SQL, (rowid,))
    latestrecords = mysqlCur.fetchall()
    return latestrecords


new_records = get_latest_records(last_rowid)
print("New rows to be inserted on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into redshift data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in redshift database.


def insert_records(records):
    new_records = []
    for record in records:
        SQL = """SELECT * from sales_data where rowid = %s"""
        mysqlCur.execute(SQL, (record[0],))
        result = mysqlCur.fetchone()
        INSERT = """INSERT INTO sales_data (rowid, product_id, category_id, quantity) VALUES (%s,%s,%s,%s)"""
        redshiftCur.execute(INSERT, result)
        new_records.append(result)
    redshiftConnect.commit()
    return new_records


insertedRecords = insert_records(new_records)
print(insertedRecords)
print("New rows inserted into production datawarehouse = ", len(insertedRecords))
mysqlConnect.close()
mysqlCur.close()
redshiftConnect.close()
redshiftCur.close()
