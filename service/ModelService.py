import sys



sys.path.append("D:\\test flask cors")
from repository.SampleRepository import SampleRepository
from repository.ModelRepository import ModelRepository
from repository.ModelSampleRepository import ModelSampleRepository
from model.Model import Model
from  model.Sample import Sample
from model.ModelSample import ModelSample
import csv
from utils import HandelFileUtil
from ultralytics import YOLO
import threading
from service.DatasetService import DatasetService
import testCreateFile


class ModelService:

    def getModelById(modelId):
        resultSet = ModelRepository.getModelById(modelId)
        model = Model(resultSet)
        modelsampleList =  ModelSampleRepository.getModelSampleByCondition(modelId)
        
        model.modelsampleList = modelsampleList
        return model

    def getModelByCondition(search_name):
        resultSets = ModelRepository.getModelByCondition(search_name)
        models = []
        for resultSet in resultSets:
            models.append(Model(resultSet))
        return models

    def trainNewModel():
        # tao path moi cho model, lay id cuoi cua model cuoi cung
        path, lastid = HandelFileUtil.getPathResult()

        # tao mot model moi 
        model = YOLO("YOLOv8n.yaml")
        results = model.train(data="config.yaml", epochs=1)

        # lay thong so sau khi tao ra model
        valueEvaluationModel = ModelService.modelEvaluation(path)

        # tao cac thong tin ve model moi
        id = lastid + 1
        name = 'best.pt'
        accuracy = valueEvaluationModel.acc
        precision = valueEvaluationModel.pre
        recall = valueEvaluationModel.recall
        f1 = valueEvaluationModel.f1
        modelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"

        model = Model.modelConstructor1(id, name, modelPath, accuracy, precision, recall, f1)
        ModelRepository.insertModel(model)

    def trainNewModelv2(datasetId):

        datasetPath = DatasetService.getDatasetById(datasetId).path
        # tao path moi cho model, lay id cuoi cua model cuoi cung
        path, lastid = HandelFileUtil.getPathResult()

        # tao mot model moi 
        model = YOLO("YOLOv8n.yaml")
        results = model.train(data=datasetPath + "\\config.yaml", epochs=1)

        # lay thong so sau khi tao ra model
        valueEvaluationModel = ModelService.modelEvaluation(path)

        # tao cac thong tin ve model moi
        id = lastid + 1
        name = 'best.pt'
        accuracy = valueEvaluationModel.acc
        precision = valueEvaluationModel.pre
        recall = valueEvaluationModel.recall
        f1 = valueEvaluationModel.f1
        modelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"

        model = Model.modelConstructor2(id, name, modelPath, accuracy, precision, recall, f1, datasetId)
        ModelRepository.insertModelv2(model)

    def trainNewModelv3(sampleIds):
        ModelRepository.setStt(1)
        samples = []
        for id in sampleIds:
            sample = SampleRepository.getSampleById(id)
            samples.append(sample)

        modelsampleList = []
        for sample in samples:
            modelsample = ModelSample.modelsampleConstructor1(Sample(sample))
            modelsampleList.append( modelsample)

        

        filePath = testCreateFile.createFile(samples)
        # tao path moi cho model, lay id cuoi cua model cuoi cung
        path, lastid = HandelFileUtil.getPathResult()

        # tao mot model moi
        model = YOLO("YOLOv8n.yaml")
        results = model.train(data=filePath + "\\config.yaml", epochs=1)

        # lay thong so sau khi tao ra model
        valueEvaluationModel = ModelService.modelEvaluation(path)

        # tao cac thong tin ve model moi
        id = lastid + 1
        name = 'best.pt'
        accuracy = valueEvaluationModel.acc
        precision = valueEvaluationModel.pre
        recall = valueEvaluationModel.recall
        f1 = valueEvaluationModel.f1
        modelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"


        model = Model.modelConstructor3(id, name, modelPath, accuracy, precision, recall, f1, modelsampleList)


        ModelRepository.insertModel(model)
        ModelSampleRepository.insertModelSample(model)
        ModelRepository.setStt(0)
        # testCreateFile.deleteFile(filePath)

    def retrainModel(model_id):
        # get path of model want to retrain
        modelForRetrain = ModelService.getModelById(model_id)
        modelPathForRetrain = modelForRetrain.path
        print("duy")
        print(modelPathForRetrain)

        path, lastid = HandelFileUtil.getPathResult()

        model = YOLO(modelPathForRetrain)
        results = model.train(data="configretrain.yaml", epochs=1)

        valueEvaluationModel = ModelService.modelEvaluation(path)

        # tao cac thong tin ve model moi
        id = lastid + 1
        name = 'best.pt'
        accuracy = valueEvaluationModel.acc
        precision = valueEvaluationModel.pre
        recall = valueEvaluationModel.recall
        f1 = valueEvaluationModel.f1
        modelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"

        model = Model.modelConstructor1(id, name, modelPath, accuracy, precision, recall, f1)
        ModelRepository.insertModel(model)

    def deleteModelById(modelId):
        # model = ModelService.getModelById(modelId)
        # modelPath = model.path
        # HandelFileUtil.deleteFile(modelPath)
        return ModelRepository.deleteModelById(modelId)

    def retrainModelV2(modelid, datasetId):
        datasetpath = DatasetService.getDatasetById(datasetId).path
        # get path of model want to retrain
        modelForRetrain = ModelService.getModelById(modelid)
        modelPathForRetrain = modelForRetrain.path
        print("duy")
        print(modelPathForRetrain)

        path, lastid = HandelFileUtil.getPathResult()

        model = YOLO(modelPathForRetrain)
        results = model.train(data=datasetpath + "\\config.yaml", epochs=1)

        valueEvaluationModel = ModelService.modelEvaluation(path)

        # tao cac thong tin ve model moi
        id = lastid + 1
        name = 'best.pt'
        accuracy = valueEvaluationModel.acc
        precision = valueEvaluationModel.pre
        recall = valueEvaluationModel.recall
        f1 = valueEvaluationModel.f1
        modelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"

        model = Model.modelConstructor2(id, name, modelPath, accuracy, precision, recall, f1, datasetId)
        ModelRepository.insertModelv2(model)

    def getActiveModel():
        resultSet = ModelRepository.getActiveModel()
        model = Model(resultSet)
        return model

    def modelEvaluation(path):
        with open(path, "r") as f:
            reader = csv.reader(f)
            next(reader)
            precision = 0
            recall = 0
            count = 0
            f1 = 0
            for row in reader:
                count = count + 1
                precision += float(row[4])
                recall += float(row[5])
                f1 += float((2 * precision * recall) / (precision + recall))
            model = Model.modelConstructor(precision / count, recall / count, f1 / count)
            return model

    def setActiveModel(modelId):
        ModelRepository.setActiveModel(modelId)

    def retrainModelV3(modelid, sampleIds):
        ModelRepository.setStt(1)
        samples = []
        for id in sampleIds:
            sample = SampleRepository.getSampleById(id)
            samples.append(sample)

        

        modelsampleList = []
        for sample in samples:
            modelsample = ModelSample.modelsampleConstructor1(Sample(sample))
            modelsampleList.append( modelsample)

        
        modelForRetrain = ModelService.getModelById(modelid)
        modelsampleListOld =  ModelSampleRepository.getModelSampleByCondition(modelid)
        modelForRetrain.modelsampleList = modelsampleListOld

        modelPathForRetrain = modelForRetrain.path


        filePath = testCreateFile.createFile(samples)
        # tao path moi cho model, lay id cuoi cua model cuoi cung
        path, lastid = HandelFileUtil.getPathResult()

        # tao mot model moi
        model = YOLO(modelPathForRetrain)
        results = model.train(data=filePath + "\\config.yaml", epochs=1)

        # lay thong so sau khi tao ra model
        valueEvaluationModel = ModelService.modelEvaluation(path)

        # tao cac thong tin ve model moi
        id = lastid + 1
        name = 'best.pt'
        accuracy = valueEvaluationModel.acc
        precision = valueEvaluationModel.pre
        recall = valueEvaluationModel.recall
        f1 = valueEvaluationModel.f1
        modelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"


        model = Model.modelConstructor3(id, name, modelPath, accuracy, precision, recall, f1, modelsampleList)


        ModelRepository.insertModel(model)
        ModelSampleRepository.insertModelSample(model)
        ModelRepository.setStt(0)

    def getStt():
        return ModelRepository.checkstt()
    
    def setStt(stt):
        ModelRepository.setStt(stt)

# listId = (16,17,18)
# ModelService.retrainModelV3(5, listId)

# ModelRepository.setStt(1)
# print(ModelService.getStt())
