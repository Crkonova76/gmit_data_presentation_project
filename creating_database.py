import mysql.connector

db=""

#create new database called competition
cursor=db.cursor()
cursor.execute("CREATE DATABASE competition")

#create table called kids
cursor=db.cursor()
sql="CREATE TABLE kids (registration INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR (30),surname VARCHAR(30),team VARCHAR(30),emergencyContactName VARCHAR (30),phoneNumber INT)"
cursor.execute(sql)

#Create records
cursor=db.cursor()
sql="insert into kids (name, surname,team,emergencyContactName,phoneNumber) values (%s,%s,%s,%s,%s)"
values=("Oliver","Crkon","Limerick","Michal", "0872736491")
cursor.execute(sql,values)
db.commit()
print(cursor.lastrowid)

#update phone number in the record
cursor=db.cursor()
sql="update kids set phoneNumber=%s where registration=%s "
values=("0872736491",1)
cursor.execute(sql,values)

#delete competitor
cursor=db.cursor()
sql="delete from kids  where registration=%s "
values=(2,)
cursor.execute(sql,values)
db.commit()