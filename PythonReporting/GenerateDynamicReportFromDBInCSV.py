import cx_Oracle
import csv

connection = cx_Oracle.connect('localdb/localdb@127.0.0.1:1521/xe')

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# Create a tablE
sql="""SELECT USERNAME,FULLNAME,password,ROLENAME,ACCOUNTENABLED ,CREATIONDATE ,STATUSCODE ,SENSITIVITY FROM users"""
cursor.execute(sql)

# open the file in the write mode
with open('users.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    for rec in cursor:
        writer.writerow(rec)

# close the file
f.close()