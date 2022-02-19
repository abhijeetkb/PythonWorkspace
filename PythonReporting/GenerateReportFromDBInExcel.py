import cx_Oracle
import xlsxwriter

connection = cx_Oracle.connect('localdb/localdb@127.0.0.1:1521/xe')

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# Create a tablE
sql="""SELECT USERNAME,FULLNAME FROM users"""
cursor.execute(sql)
workbook=xlsxwriter.Workbook('Users.xlsx')
worksheet=workbook.add_worksheet()
row=1
col=1
worksheet.write(0,0,"Username")
worksheet.write(0,1,"Fullname")

for rec in cursor:
    worksheet.write(row,col-1,rec[0])
    worksheet.write(row,col,rec[1])
    row+=1
    
workbook.close()