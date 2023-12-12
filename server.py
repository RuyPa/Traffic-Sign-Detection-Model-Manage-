# # http://localhost:5000/api/v1/hello

from flask import jsonify, Flask, request, send_file, make_response
from model import Model
from flask_cors import CORS
import pymysql
from ultralytics import YOLO
import threading
import CountImg
import read
from repository.ModelRepository import ModelRepository

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="managesample"
)

cursor = db.cursor()


@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'hello world!'})


@app.route('/api/v1/model', methods=['GET'])
def getModel():
    result = ModelRepository.getAllModel()
    models = []
    for row in result:
        model = Model.Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        models.append(model.__dict__)
    return jsonify(models)

@app.route('/api/v1/train-new-model', methods = ['GET'])
def trainNewModel():
    def train_model():
        path, lastid = read.getPathResult()
        # code cu
        model = YOLO("YOLOv8n.yaml")
        results = model.train(data="config.yaml", epochs=1 )
        #code cu
        acc, precision, recall, f1 = read.algorithmEvaluation(path)
        newModelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"

        # print(newModelPath)

        idd = lastid + 1
        name = 'best.pt'
        accuracy = acc
        precision = precision
        recall = recall
        f1_score = f1
        path = newModelPath

        insert_query = "INSERT INTO managesample.model (id, name, path, acc, pre, recall, f1, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (idd, name, path, accuracy, precision, recall, f1_score, " "))
        db.commit()



    train_thread = threading.Thread(target=train_model)
    train_thread.start()   
    return jsonify({'message': 'hello world!'})


@app.route('/api/v1/model/<int:model_id>', methods=['GET'])
def getModelById(model_id):
    query = "SELECT * FROM managesample.model WHERE id = %s"
    cursor.execute(query, (model_id,))
    result = cursor.fetchone()
    model = Model.Model(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
    return jsonify(model.__dict__)


@app.route('/api/v1/model/<int:model_id>', methods=['DELETE'])
def deleteModel(model_id):
    ModelRepository.deleteModelById(model_id)
    return jsonify({'message': 'Model deleted successfully'})


@app.route('/api/v1/model/search', methods=['GET'])
def searchModelByName():
    search_name = request.args.get('name')
    query = "SELECT * FROM managesample.model WHERE name LIKE %s"
    cursor.execute(query, (f'%{search_name}%'))
    result = cursor.fetchall()
    models = []
    for row in result:
        model = Model.Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        models.append(model.__dict__)
    return jsonify(models)

@app.route('/api/v1/model/retrain/<int:model_id>', methods =['GET'])
def retrainModel(model_id):

    # get by id sau do lay path la duoc
    query = "SELECT path FROM managesample.model WHERE id = %s"
    cursor.execute(query, (model_id,))
    # khi lay ra path la mot tubel ko phai string --> lay path[0]
    path = cursor.fetchone()
    def retrain():
        path, lastid = read.getPathResult()

        # code cu
        model = YOLO(path[0])
        results = model.train(data="configretrain.yaml", epochs=1 )

        # #code cu

        acc, precision, recall, f1 = read.algorithmEvaluation(path)
        newModelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"

        idd = lastid + 1
        name = 'best.pt'
        accuracy = acc
        precision = precision
        recall = recall
        f1_score = f1
        path = newModelPath

        insert_query = "INSERT INTO managesample.model (id, name, path, acc, pre, recall, f1, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (idd, name, path, accuracy, precision, recall, f1_score, " "))
        db.commit()

    numberOfOldSamples = CountImg.countFile("D:\\test flask cors\\data\\images\\train")
    numberOfRetrainSamples = CountImg.countFile("D:\\test flask cors\\retrain\\images\\train")
    # numberOfRetrainSamples = 1

    if numberOfRetrainSamples / numberOfOldSamples > 0.025:
        retrain_thread = threading.Thread(target=retrain)
        retrain_thread.start() 
        response = {'message': 'retraining'}
    else:
        response = {'message': 'number of samples is less than permission'}
    return jsonify(response)

@app.route('/api/v1/model/get-current', methods=['GET'])
def download_best_pt():
    query = "SELECT path FROM managesample.model WHERE status LIKE %s"
    cursor.execute(query, ('%active%',))
    result = cursor.fetchone()
    file_path = result[0]
    print(file_path)
    response = make_response(send_file(file_path, as_attachment=True, download_name='best.pt'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response
    

if __name__ == '__main__':
    app.run(debug=True)
