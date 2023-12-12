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

class ModelRepository:
    def getModelById(modelId):
        query = "SELECT * FROM managesample.model WHERE id = %s"
        cursor.execute(query, (modelId,))
        result = cursor.fetchone()
        return result

    def getModelByCondition(search_name):
        query = "SELECT * FROM managesample.model WHERE name LIKE %s"
        cursor.execute(query, (f'%{search_name}%'))
        result = cursor.fetchall()
        print(search_name)
        return result

    def insertModel(model):
        insert_query = "INSERT INTO managesample.model (id, name, path, acc, pre, recall, f1, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (model.id, model.name, model.path, model.acc, model.pre, model.recall, model.f1, model.status))
        db.commit()

    def deleteModelById(modelId):
        query = "DELETE FROM managesample.model WHERE id = %s"
        cursor.execute(query, (modelId,))
        db.commit()

    def getActiveModel():
        query = "SELECT * FROM managesample.model WHERE status LIKE %s"
        cursor.execute(query, ('%active%',))
        result = cursor.fetchone()
        return result
    
    def insertModelv2(model):
        insert_query = "INSERT INTO managesample.model (id, name, path, acc, pre, recall, f1, status, datasetId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (model.id, model.name, model.path, model.acc, model.pre, model.recall, model.f1, model.status, model.datasetId))
        db.commit()

    def setActiveModel(modelId):
        update_query = "UPDATE managesample.model SET status = %s WHERE status LIKE %s"
        cursor.execute(update_query, ("", "%active%"))
        db.commit()  

        set_active_query = "UPDATE managesample.model SET status = %s WHERE id = %s"
        cursor.execute(set_active_query, ("active", modelId))
        db.commit() 

    def checkstt():
        check_query =  "SELECT * FROM managesample.stt"
        cursor.execute(check_query,)
        result = cursor.fetchone()
        return result[0]
    
    def setStt(stt):
        upd_query = "UPDATE managesample.stt SET stt = %s"
        cursor.execute(upd_query, (stt))
        db.commit()

# print(ModelRepository.checkstt())
# ModelRepository.setStt(0)
# print(ModelRepository.checkstt())
