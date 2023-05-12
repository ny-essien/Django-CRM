import mysql.connector

database = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = "density4488"
)

#prepare a cursor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE cryptchain")

print("All Done !!!")