#!C:\Python\python.exe
print ('Content-type:text/html; charset=utf-8\n\n')
import cgi, cgitb 
# Python code for Sending mail from  
# your Gmail account  
import smtplib 
import math, random

# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
OTP = 0

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
receiver = form.getvalue('username')
number = form.getvalue('mobile')  

print("</body>")
print("</html>")
print("<html>")
print("<head>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))

sender = 'pycoders2432@gmail.com';
password = 'pyotp2432'  
OTP = '1055'
# creating SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(sender, password) 
 
# message to be sent
OTP = generateOTP() 
message = 'Here is your OTP ' + OTP + '.';
  
# sending the mail 
s.sendmail(sender,receiver, message) 
  
# terminating the session 
s.quit()
print("<p>OTP has been sent to your mail</p>")
print('<a href = "verify.html"> <input type="Button" value = " Verify"></a>') 

f = open("OTP.txt","w")
f.write(OTP)
f.close()