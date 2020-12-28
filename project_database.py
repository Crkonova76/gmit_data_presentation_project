import mysql.connector
import dbConfig as cfg


class KidsDAO:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def create(self, kid):
        cursor = self.db.cursor()
        sql = "insert into kids (name, surname,belt,status,phoneNumber) values (%s,%s,%s,%s,%s)"
        values = [
            kid["name"],
            kid["surname"],
            kid["belt"],
            kid["status"],
            kid["phoneNumber"]
        ]

        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from kids"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict= self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    def findByID(self, registration):
        cursor = self.db.cursor()
        sql = "select * from kids where registration = %s"
        values = [registration]

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, kid):       
        cursor = self.db.cursor()
        sql = "update kids set name=%s,surname=%s,belt=%s,status=%s,phoneNumber=%s where registration = %s"
        values = [            
            kid["name"],
            kid["surname"],
            kid["belt"],
            kid["status"],
            kid["phoneNumber"],
            kid["registration"]
        ]
        cursor.execute(sql,values)
        self.db.commit()
        return kid

    def delete(self, registration):
        cursor = self.db.cursor()
        sql = "delete from kids where registration = %s"
        values = [registration]
        cursor.execute(sql, values)
        return{}

    def convertToDict(self,result):
        colnames=['registration','name','surname','belt','status','phoneNumber']
        kid = {}

        if result:
            for i,colName in enumerate(colnames):
                value=result[i]
                kid[colName]=value

        return kid

kidsDAO = KidsDAO()

class AdminsDAO:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def createAdmin(self, admin):
        cursor = self.db.cursor()
        sql = "insert into admins (UserName, Password) values (%s,%s)"
        values = [
            admin["UserName"],
            admin["Password"]
        ]

        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def deleteAdmin(self, id):
        cursor = self.db.cursor()
        if id == False:
            return {}
        else:
            sql = "delete from admins where id = %s"
            values = [id]
            cursor.execute(sql, values)
            return{}
        
        
    def deleteAll(self):
        cursor = self.db.cursor()
        sql = "delete from admins where id != 1"       
        cursor.execute(sql)
        return{}


    def getAllAdmins(self):
        cursor = self.db.cursor()
        sql = "select * from admins"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict= self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    def convertToDict(self,result):
        colnames=['id','UserName','Password']
        admin = {}

        if result:
            for i,colName in enumerate(colnames):
                value=result[i]
                admin[colName]=value
        return admin
        
        
adminsDAO = AdminsDAO()