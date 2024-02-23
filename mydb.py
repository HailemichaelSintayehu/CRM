import mysql.connector 

database = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = 'StrongPassword123!'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm_data")

print("All Done!")