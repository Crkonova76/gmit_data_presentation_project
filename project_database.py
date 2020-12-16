import mysql.connector

class KidsDAO:
    db=""
    def __init__(self):
        self.db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="competition"
        )

    def create(self,values):
        cursor=self.db.cursor()
        sql="insert into kids (name, surname,team,emergencyContactName,phoneNumber) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql,values)

        self.db.commit()
        return cursor .lastrowid

    def getAll(self):
        cursor=self.db.cursor()
        sql="select * from kids"
        cursor.execute(sql)
        result=cursor.fetchall()
        return result

    def findByID(self,id):
        cursor=self.db.cursor()
        sql="select * from kids where registration = %s"
        values=(id,)

        cursor.execute(sql,values)
        result=cursor.fetchone()
        return result

    def update(self,values):
        cursor=self.db.cursor()
        sql="update kids set name=%s, surname=%s,team=%s,emergencyContactName=%s,phoneNumber=%s"
        cursor.execute(sql,values)
        self.db.commit()

    def delete(self,id):
        cursor=self.db.cursor()
        sql="delete from kids where registration = %s"
        values=(id,)
        cursor.execute(sql,values)

        self.db.commit()
        print("delete completed")

kidsDAo=KidsDAO

#cursor=db.cursor()
#cursor.execute("CREATE DATABASE competition")

#cursor=db.cursor()
#sql="CREATE TABLE kids (registration INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR (30),surname VARCHAR(30),team VARCHAR(30),emergencyContactName VARCHAR (30),phoneNumber INT)"
#cursor.execute(sql)

#Create
#cursor=db.cursor()
#sql="insert into kids (name, surname,team,emergencyContactName,phoneNumber) values (%s,%s,%s,%s,%s)"
#values=("Oliver","Crkon","Limerick","Michal", "0872736491")
#cursor.execute(sql,values)
##db.commit()
#print(cursor.lastrowid)

#update phone number
#cursor=db.cursor()
#sql="update kids set phoneNumber=%s where registration=%s "
#values=("0872736491",1)
#cursor.execute(sql,values)

#delete competitor
#cursor=db.cursor()
#sql="delete from kids  where registration=%s "
#values=(2,)
#cursor.execute(sql,values)
#db.commit()
