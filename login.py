#!C:\Python\python.exe
print ('Content-type:text/html; charset=utf-8\n\n')
import cgi, cgitb 
import MySQLdb
 
db_connection = MySQLdb.connect(host='localhost',
								db='python',
								user='root',
								passwd='')
 
c = db_connection.cursor()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

name = form.getvalue('name')
password = form.getvalue('password')
query = "SELECT Password FROM user WHERE Name = '%s'" % (name)
c.execute(query)

results = c.fetchall()
A_Password = ''
for row in results:
	A_Password = row[0]

if A_Password == password:
	print("<p>Login Success!!!</p>")
	print('<a href = "index.html"> <button>Go Home</button> </a>')
else:
	print("<p>Wrong Password!!!</p>")
	print('<a href = "login.html"> <button>Go Back</button> </a>')