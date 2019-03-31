#!C:\Python\python.exe
print ('Content-type:text/html; charset=utf-8\n\n')
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
E_OTP = form.getvalue('otp')
f = open("OTP.txt","r")
A_OTP = f.read()

if A_OTP == E_OTP:
	print('<p>OTP Verified</p>')
	print('<a href = "index.html"> <button>Home</button> </a>')
else:
	print('<p>Wrong OTP </p>')
	print('<a href = "verify.html"> <button>Go Back</button> </a>')