import sys
from flask import jsonify, make_response, send_file
sys.path.append("D:\\test flask cors")
from model.Model import Model
from service.ModelService import ModelService
from utils import HandelFileUtil
from ultralytics import YOLO
import threading
from service.DatasetService import DatasetService

class DatasetController:
    def getDatasetByCondition(search_name):
        result = DatasetService.getDatasetByCondition(search_name)
        jsonResults = []
        for dataset in result:
            jsonResults.append(dataset.__dict__)
        # print(jsonResults)
        return jsonify(jsonResults)
    
    def getAllDataset():
        result = DatasetService.getAllDataset()
        jsonResults = []
        for dataset in result:
            jsonResults.append(dataset.__dict__)
        return jsonify(jsonResults)
    
    def getDatasetById(datasetId):
        dataset = DatasetService.getDatasetById(datasetId)
        return jsonify(dataset.__dict__)