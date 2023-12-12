# Import necessary modules
import sys
sys.path.append("D:\\test flask cors")

import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="managesample"
)

cursor = db.cursor()

# print(db)

class DatasetRepository:
    def getDatasetByCondition(search_name):
        query = "SELECT * FROM managesample.dataset WHERE name LIKE %s"
        cursor.execute(query, (f'%{search_name}%'))
        result = cursor.fetchall()
        print(search_name)
        return result
    
    def getAllDataset():
        query = "SELECT * FROM managesample.dataset"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    def getDatasetById(datasetId):
        query = "SELECT * FROM managesample.dataset WHERE id = %s"
        cursor.execute(query, (datasetId,))
        result = cursor.fetchone()
        return result
    

