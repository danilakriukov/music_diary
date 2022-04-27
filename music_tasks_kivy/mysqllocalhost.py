import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "SymphoniaHeroica1803!",
    #auth_plugin='mysql_native_password'
    database = "hometaskdb",
    )

my_cursor = mydb.cursor()
#print(mydb)
#my_cursor.execute("CREATE DATABASE testdb")
#my_cursor.execute("SHOW DATABASES")
#print(my_cursor)
for db in my_cursor:
    print(db)
#for db in my_cursor:
#    print(db[0])
# [0] - nice look
#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#my_cursor.execute("SHOW TABLES")
#for db in my_cursor:
#    print(db[0])
#tuple - кортеж
#sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
#record1 = ("Danila", "fsdfl@fgdf.ru", 34)

#my_cursor.execute(sqlStuff, record1)
#mydb.commit()
#show = my_cursor.execute("SHOW TABLES")
#print(show)
input()
