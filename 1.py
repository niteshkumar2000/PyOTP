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

# Get data from fields
E_OTP = form.getvalue('otp')
f = open("OTP.txt","r")
A_OTP = f.read()

if A_OTP == E_OTP:
	print('<p>OTP Verified</p>')
	print('<a href = "login.html"> <button>Home</button> </a>')

	f1 = open("user.txt","r")
	data = (f1.read()).split(' ')

	if data[2].isdigit():
		c.execute("INSERT INTO user(Name,Passowrd,Phone) values(%s,%s,%s)",(data[0],data[1],data[2]))
	else:
		c.execute("INSERT INTO user(Name,Password,Mail) values(%s,%s,%s)",(data[0],data[1],data[2]))
	db_connection.commit()
	print("<p> DATA ENTRY DONE</p>")
else:
	print('<p>Wrong OTP </p>')
	print('<a href = "verify.html"> <button>Go Back</button> </a>')

db_connection.close()