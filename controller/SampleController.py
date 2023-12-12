import sys
from flask import jsonify, make_response, send_file
sys.path.append("D:\\test flask cors")
from model.Model import Model
from service.ModelService import ModelService
from utils import HandelFileUtil
from ultralytics import YOLO
import threading
from service.DatasetService import DatasetService
from service.SampleService import SampleService

class SampleController:
    def getSampleByCondition(search_name):
        result = SampleService.getSampleByCondition(search_name)
        jsonResults = []
        for sample in result:
            jsonResults.append(sample.__dict__)
        print(jsonResults)
        return jsonify(jsonResults)
    
    def getAllSample():
        result = SampleService.getAllSample()
        jsonResults = []
        for sample in result:
            jsonResults.append(sample.__dict__)
        # print(jsonResults)
        return jsonify(jsonResults)
    
    # def getAllDataset():
    #     result = DatasetService.getAllDataset()
    #     jsonResults = []
    #     for dataset in result:
    #         jsonResults.append(dataset.__dict__)
    #     return jsonify(jsonResults)
    
    # def getDatasetById(datasetId):
    #     dataset = DatasetService.getDatasetById(datasetId)
    #     return jsonify(dataset.__dict__)

# SampleController.getAllSample()
