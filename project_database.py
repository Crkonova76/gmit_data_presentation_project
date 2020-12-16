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
        sql = "insert into kids (name, surname,team,emergencyContactName,phoneNumber) values (%s,%s,%s,%s,%s)"
        values = [
            kid["name"],
            kid["surname"],
            kid["team"],
            kid["emergencyContactName"],
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
        #print(results)
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
        sql = "update kids set name=%s, surname=%s,team=%s,emergencyContactName=%s,phoneNumber=%s"
        values = [
            kid["name"],
            kid["surname"],
            kid["team"],
            kid["emergencyContactName"],
            kid["phoneNumber"]
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
        #self.db.commit()
        #print("delete completed")

    def convertToDict(self,result):
        colnames=['registration','name','surname','team','emergencyContactName','phoneNumber']
        kid = {}

        if result:
            for i,colName in enumerate(colnames):
                value=result[i]
                kid[colName]=value
        return kid

kidsDAO = KidsDAO()
