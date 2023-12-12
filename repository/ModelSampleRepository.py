# Import necessary modules
import sys

sys.path.append("D:\\test flask cors")
from model.ModelSample import ModelSample
from model.Sample import Sample

import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="managesample"
)

cursor = db.cursor()


# print(db)

class ModelSampleRepository:
    def getModelSampleByCondition(search_name):
        query = "SELECT * FROM managesample.modelsample WHERE model_id = %s"
        cursor.execute(query,  (search_name,))
        result = cursor.fetchall()
        print(search_name)
        return result

    def getModelSampleById(modelsampleId):
        query = "SELECT * FROM managesample.modelsample WHERE id = %s"
        cursor.execute(query, (modelsampleId,))
        result = cursor.fetchone()
        return result

    def insertModelSample(model):

        # Thực hiện câu lệnh SQL để lấy ID của hàng cuối cùng
        query = "SELECT id FROM managesample.modelsample ORDER BY id DESC LIMIT 1;"
        cursor.execute(query)

        # Lấy kết quả
        result = cursor.fetchone()[0]


        for modelsample in model.modelsampleList:
            # sample = Sample(modelsample.sample)
            # print(sample.id)
            # modelsample = ModelSample(modelsample)
            result = int(result) + 1
            insert_query = "INSERT INTO managesample.modelsample (id, model_id, sample_id) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (result, model.id, modelsample.sample.id))
            db.commit()
           

# print(ModelSampleRepository.getModelSampleByCondition(5))