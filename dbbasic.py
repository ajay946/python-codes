import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="ajay@1234",database="telusko")


mycursor=mydb.cursor()



mycursor.execute("select * from student")
for i in mycursor:
    print(i)