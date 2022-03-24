import sqlite3
class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connectDatabase()
        self.createTable()
    
    def connectDatabase(self):
        self.conn = sqlite3.connect("member.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = 1")

    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS member (id TEXT PRIMARY KEY, pw TEXT, name TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS playlist (no INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, name TEXT, FOREIGN KEY(id) REFERENCES member(id) ON DELETE CASCADE) ")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS video (no INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, playlist INTEGER, FOREIGN KEY(playlist) REFERENCES playlist (no) ON DELETE CASCADE) ")
        
    def createData(self, tableName, dataCondition, dataList):
        tmpData = "INSERT INTO " + tableName + " ("
        for index in range(0, len(dataCondition)):
            tmpData += dataCondition[index]
            if index < len(dataCondition) - 1:
                tmpData += ", "
        tmpData += ") VALUES ("
        for index in range(0, len(dataCondition)):
            tmpData  += "?"
            if index < len(dataCondition) - 1:
                tmpData += ", "
        tmpData += ")"
        self.cursor.execute(tmpData, dataList)
        self.conn.commit()

    def readData(self, dataTypeList, tableName, dataConditionType, dataCondition):
        tmpSelect = "SELECT "
        for index in range(0, len(dataTypeList)):
            tmpSelect += dataTypeList[index]
            if index < len(dataTypeList) - 1:
                tmpSelect += ", "
        tmpSelect += " FROM " + tableName + " "
        if len(dataConditionType) != 0:
            tmpSelect += "WHERE " + dataConditionType + " = ?"
            self.cursor.execute(tmpSelect, dataCondition)
            result = self.cursor.fetchall()
            return result
        else:
            self.cursor.execute(tmpSelect)
            result = self.cursor.fetchall()
            return result

    def deleteData(self, tableName, dataType, dataList):
        tmpDelete = "DELETE FROM " + tableName + " WHERE " + dataType + " = ?"
        self.cursor.execute(tmpDelete, dataList)
        self.conn.commit()

        
