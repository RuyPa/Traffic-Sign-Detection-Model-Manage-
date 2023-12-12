import sys
from flask import jsonify, make_response, send_file
sys.path.append("D:\\test flask cors")
from model.Model import Model
from service.ModelService import ModelService
from utils import HandelFileUtil
from ultralytics import YOLO
import threading
from service.DatasetService import DatasetService

class ModelController:
    def getModelByCondition(search_name):
        result = ModelService.getModelByCondition(search_name)
        jsonResults = []
        for model in result:
            jsonResults.append(model.__dict__)
        return jsonify(jsonResults)

    def getModelById(modelId):
        model = ModelService.getModelById(modelId)
        return jsonify(model.__dict__)
    
    def deleteModelById(modelId):
        ModelService.deleteModelById(modelId)
        return jsonify({'message': 'Model deleted successfully'})
    
    def getActiveModel():
        model = ModelService.getActiveModel()
        modelPath = model.path
        response = make_response(send_file(modelPath, as_attachment=True, download_name='best.pt'))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        return response
    
    def trainNewModel():
        train_thread = threading.Thread(target=ModelService.trainNewModel)
        train_thread.start()
        return jsonify({'message': 'hello world!'})
    
    def retrainModelById(model_id):
        numberOfOldSamples = HandelFileUtil.countFile("D:\\test flask cors\\data\\images\\train")
        numberOfRetrainSamples = HandelFileUtil.countFile("D:\\test flask cors\\retrain\\images\\train")

        if numberOfRetrainSamples / numberOfOldSamples > 0.5:
            retrain_thread = threading.Thread(target=ModelService.retrainModel(model_id))
            retrain_thread.start() 
            return jsonify({'message': 'retraining'}) 
        else:
            return jsonify({'message': 'number of samples is less than permission'})
        
    def retrainModelByIdv2(model_id, datasetId):
        print(ModelService.getModelById(model_id).path)
        print(DatasetService.getDatasetById(datasetId).path)
        oldDatasetId= ModelService.getModelById(model_id).datasetId
        print(oldDatasetId)
        numberOfOldSamples = HandelFileUtil.countFile(DatasetService.getDatasetById(oldDatasetId).path + "\\images\\train")
        numberOfRetrainSamples = HandelFileUtil.countFile(DatasetService.getDatasetById(datasetId).path + "\\images\\train")

        if numberOfRetrainSamples / numberOfOldSamples > 0.01:
            retrain_thread = threading.Thread(target=ModelService.retrainModelV2(model_id,datasetId))
            retrain_thread.start() 
            return jsonify({'message': 'retraining'}) 
        else:
            return jsonify({'message': 'number of samples is less than permission'})
        
    def trainNewModelv2(datasetId):
        train_threadv2 = threading.Thread(target=ModelService.trainNewModelv2(datasetId))
        train_threadv2.start()
        return jsonify({'message': 'hello world!'})
    
    def setActiveModel(modelId):
        ModelService.setActiveModel(modelId)
        return jsonify({'message': 'success'})
    
    def trainNewModelv3(listSampleId):
        train_threadv3 = threading.Thread(target=ModelService.trainNewModelv3(listSampleId))
        train_threadv3.start()
        return jsonify({'message': 'hello world!'})
    

    def retrainModelByIdv3(model_id, sampleListId):
        modelForRetrain = ModelService.getModelById(model_id)
        numberOfOldSamples = len(modelForRetrain.modelsampleList)

        numberOfRetrainSamples = len(sampleListId)


        if numberOfRetrainSamples / numberOfOldSamples > 0.1:
            retrain_thread = threading.Thread(target=ModelService.retrainModelV3(model_id, sampleListId))
            retrain_thread.start() 
            return jsonify({'message': 'retraining'}) 
        else:
            return jsonify({'message': 'number of samples is less than permission'})
        
    def checkStt():
        result = ModelService.getStt()
        return jsonify({'message': result})

# ModelController.retrainModelByIdv3(5, (15,16,17, 18))