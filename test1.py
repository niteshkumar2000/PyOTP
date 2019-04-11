#!C:\Python\python.exe
print ('Content-type:text/html; charset=utf-8\n\n')
import MySQLdb
 
print("Connecting to database using MySQLdb")
 
db_connection = MySQLdb.connect(host='localhost',
								db='test',
								user='root',
								passwd='')
 
print("Succesfully Connected to database using MySQLdb!")

c = db_connection.cursor()

c.execute("SELECT * FROM user")
result = c.fetchall()

for row in result:
	print("<p>Username : %s Password : %s</p>" % (row[0],row[1]))

db_connection.close()