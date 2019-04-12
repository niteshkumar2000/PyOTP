import MySQLdb
db_connection = MySQLdb.connect(host='localhost',
								db='python',
								user='root',
								passwd='')
 
c = db_connection.cursor()
name = 'Niteshkumar'
password = "Nitesh15"
query = "SELECT Password FROM user WHERE Name = '%s'" % (name)
c.execute(query)

results = c.fetchall()
A_Password = ''
for row in results:
	A_Password = row[0]

if A_Password == password:
	print("<p>Login Success!!!</p>")
else:
	print("<p>Wrong Password!!!</p>")