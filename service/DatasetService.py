import sys
sys.path.append("D:\\test flask cors")
from repository.ModelRepository import ModelRepository
from model.Model import Model
from model.Dataset import Dataset
import csv
from utils import HandelFileUtil
from ultralytics import YOLO
import threading
from repository.DatasetRepository import DatasetRepository

class DatasetService:

    # def getModelById(modelId):
    #     resultSet = ModelRepository.getModelById(modelId)
    #     model = Model(resultSet)
    #     return model

    def getDatasetByCondition(search_name):
        resultSets = DatasetRepository.getDatasetByCondition(search_name)
        datasets = []
        for dataset in resultSets:
            datasets.append(Dataset(dataset))
        return datasets
    
    def getAllDataset():
        resultSets = DatasetRepository.getAllDataset()
        datasets = []
        for dataset in resultSets:
            datasets.append(Dataset(dataset))
        return datasets
    
    def getDatasetById(datasetId):
        resultSet = DatasetRepository.getDatasetById(datasetId)
        dataset = Dataset(resultSet)
        return dataset