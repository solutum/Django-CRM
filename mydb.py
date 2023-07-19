import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '123qwe45Ms'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE del_me")
print("done")