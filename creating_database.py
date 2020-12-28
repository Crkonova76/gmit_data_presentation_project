import mysql.connector
import dbConfig as cfg

db=""

db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
     )

#create new database called competition
cursor=db.cursor()
cursor.execute("CREATE DATABASE competition")

#create table called kids
cursor=db.cursor()
sql="CREATE TABLE kids (registration INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR (30),surname VARCHAR(30),belt VARCHAR(30),status ENUM('Active','Inactive')DEFAULT 'ACTIVE',phoneNumber INT)"
cursor.execute(sql)

#create table called admins
cursor=db.cursor()
sql="CREATE TABLE admins (id INT AUTO_INCREMENT PRIMARY KEY,UserName VARCHAR (30),Password VARCHAR(30))"
cursor.execute(sql)

# #Create records in kids table
cursor=db.cursor()
sql="insert into kids (name, surname,belt,status,phoneNumber) values (%s,%s,%s,%s,%s)"
values=("Oliver","Crkon","blue","Active", "0872736491")
cursor.execute(sql,values)
db.commit()
print(cursor.lastrowid)

# #update phone number in the record
cursor=db.cursor()
sql="update kids set phoneNumber=%s where registration=%s "
values=("0872736491",1)
cursor.execute(sql,values)

# #delete member
cursor=db.cursor()
sql="delete from kids  where registration=%s "
values=(2,)
cursor.execute(sql,values)
db.commit()