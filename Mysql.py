import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Uday@moksh@108", database="Mokshit")

mycursor = mydb.cursor()
mycursor.execute("select * from student")

result = mycursor.fetchall()

for i in result:
    print(i)

