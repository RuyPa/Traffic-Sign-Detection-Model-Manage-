import random
import sys

sys.path.append("D:\\test flask cors")
from flask import Flask, jsonify, request, send_from_directory,send_file
from flask_cors import CORS
from model.Model import Model
from modelV1.Sample import Sample
import os

from controller.ModelController import ModelController
from controller.DatasetController import DatasetController
from controller.SampleController import SampleController

from repository.SampleRepository import SampleRepository

app = Flask(__name__)

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
CORS(app, resources={r"/api/*": {"origins": "http://localhost:63343"}})

@app.route('/images/<path:image_name>')
def get_image(image_name):
    image_path = f'D:/test flask cors/data/images/train/{image_name}'
    return send_file(image_path, mimetype='image/png')


@app.route('/api/v2/model/<int:model_id>', methods=['GET'])
def getModelById(model_id):
    return ModelController.getModelById(model_id)


@app.route('/api/v2/model/get-current', methods=['GET'])
def downloadActiveModel():
    return ModelController.getActiveModel()


@app.route('/api/v2/model/search', methods=['GET'])
def searchModelByName():
    search_name = request.args.get('name')
    return ModelController.getModelByCondition(search_name)


@app.route('/api/v2/model/retrain/<int:model_id>', methods=['GET'])
def retrainModel(model_id):
    return ModelController.retrainModelById(model_id)


@app.route('/api/v2/train-new-model', methods=['GET'])
def traiNewModel():
    return ModelController.trainNewModel()


@app.route('/api/v2/model/<int:model_id>', methods=['DELETE'])
def deleteModel(model_id):
    return ModelController.deleteModelById(model_id)


@app.route('/api/v2/dataset/search', methods=['GET'])
def searchDatasetByName():
    search_name = request.args.get('name')
    return DatasetController.getDatasetByCondition(search_name)


@app.route('/api/v2/dataset', methods=['GET'])
def getAllDataset():
    return DatasetController.getAllDataset()


@app.route('/api/v2/dataset/<int:datasetId>', methods=['GET'])
def getDatasetById(datasetId):
    return DatasetController.getDatasetById(datasetId)


@app.route('/api/v2/model/retrainv2/<int:model_id>/<int:datasetId>', methods=['GET'])
def retrainModelv2(model_id, datasetId):
    return ModelController.retrainModelByIdv2(model_id, datasetId)


@app.route('/api/v2/train-new-modelv2/<int:datasetId>', methods=['GET'])
def traiNewModelv2(datasetId):
    return ModelController.trainNewModelv2(datasetId)


@app.route('/api/v2/set-active-model/<int:modelId>', methods=['GET'])
def setActiveModel(modelId):
    return ModelController.setActiveModel(modelId)


@app.route('/api/v3/sample/search', methods=['GET'])
def searchSampleByName():
    search_name = request.args.get('name')
    return SampleController.getSampleByCondition(search_name)

@app.route('/api/v3/model/train-new-model', methods=['POST'])
def traiNewModelv3():

    data = request.get_json()

    listSampleIds = [int(id) for id in data['ids'].split(',')]
    
    return ModelController.trainNewModelv3(listSampleIds)

@app.route('/api/v3/model/retrainv3/<int:model_id>', methods=['POST'])
def retrainModelv3(model_id):
    data = request.get_json()
    listSampleIds = [int(id) for id in data['ids'].split(',')]
    return ModelController.retrainModelByIdv3(model_id, listSampleIds)

@app.route('/api/v3/sample/all', methods=['GET'])
def getAllSample():
    return SampleController.getAllSample()

@app.route('/api/v3/stt', methods=['GET'])
def getStt():
    return ModelController.checkStt()



@app.route('/api/sample', methods=['POST'])
def process_sample():
    try:
        data_from_fe = request.get_json()
        sample_object = Sample(
            id=data_from_fe['id'],
            code=data_from_fe['code'],
            name=data_from_fe['name'],
            path=data_from_fe['path'],
            labels=data_from_fe['labels']
        )

        SampleRepository.insertSample(sample_object)

        for label in sample_object.labels:
            SampleRepository.insertLabel(label, sample_object.id)

        return jsonify({"message": "Sample processed successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
