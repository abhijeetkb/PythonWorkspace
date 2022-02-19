import cx_Oracle
import csv

def get_header(columns):
    header = []
    for column in data.description:
       # print(column[0])
        header.append(column[0])
    print("Column Header: ")
    print("******************************************************************************************************************************")
    print(header)
    print("******************************************************************************************************************************")
    return header

connection = cx_Oracle.connect('localdb/localdb@127.0.0.1:1521/xe')

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# Create a tablE
sql="""SELECT USERNAME,FULLNAME,password,ROLENAME,ACCOUNTENABLED ,CREATIONDATE ,STATUSCODE ,SENSITIVITY FROM users order by FULLNAME ASC"""
data=cursor.execute(sql)

# open the file in the write mode
with open('users.csv', 'w', newline='',encoding='UTF8') as csvfile:
    writer = csv.writer(csvfile)
    header=get_header(data.description)
    writer.writerow(header)
    i=1
    for rec in cursor:
        print("Row: " + str(i) + str(rec))
        writer.writerow(rec)
        i+=1
   
# close the file
csvfile.close()

