# Import necessary modules
import random
import sys

sys.path.append("D:\\test flask cors")

import pymysql
from model.Label import Label

db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="managesample"
)

cursor = db.cursor()


# print(db)

class SampleRepository:
    def getSampleByCondition(search_name):
        query = "SELECT * FROM managesample.sample WHERE code LIKE %s"
        cursor.execute(query, (f'%{search_name}%'))
        result = cursor.fetchall()
        print(search_name)
        return result

    def getSampleById(sampleId):
        query = "SELECT * FROM managesample.sample WHERE id = %s"
        cursor.execute(query, (sampleId,))
        result = cursor.fetchone()
        return result
    
    def getAllSample():
        query = "SELECT * FROM managesample.sample"
        cursor.execute(query, )
        result = cursor.fetchall()
        return result


    def getLabelBySampleId(sampleId):
        query = "SELECT * FROM managesample.label WHERE sample_id = %s"
        cursor.execute(query, (sampleId,))
        result = cursor.fetchone()
        return result
    

    def insertLabel(label, sample_id):
        insert_query = "INSERT INTO managesample.label (id, height, sample_id, width, x_center, y_center) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (random.randint(0, 100000), label.height, sample_id, label.width, label.x_center, label.y_center))
        db.commit()

    def insertSample(sample):
        insert_query = "INSERT INTO managesample.sample (id, code, name, path) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (sample.id, sample.code, sample.name, sample.path))
        db.commit()

# print(SampleRepository.getLabelBySampleId(13))



# label = Label.constructorV1(1,2,3,4,5)

# SampleRepository.insertLabel(label, 1)