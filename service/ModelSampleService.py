import sys

sys.path.append("D:\\test flask cors")
from model.ModelSample import ModelSample
from repository.ModelSampleRepository import ModelSampleRepository


class ModelSampleService:

    # def getModelById(modelId):
    #     resultSet = ModelRepository.getModelById(modelId)
    #     model = Model(resultSet)
    #     return model

    def getModelSampleByCondition(search_name):
        resultSets = ModelSampleRepository.getModelSampleByCondition(search_name)
        modelsamples = []
        for modelsample in resultSets:
            modelsamples.append(ModelSample(modelsample))
        return modelsamples

    # def getAllDataset():
    #     resultSets = DatasetRepository.getAllDataset()
    #     datasets = []
    #     for dataset in resultSets:
    #         datasets.append(Dataset(dataset))
    #     return datasets

    def getModelampleById(modelsampleId):
        resultSet = ModelSampleRepository.getModelSampleById(modelsampleId)
        sample = ModelSample(resultSet)
        return sample
    
    def getModelSampleByModelId(id):
        resultSets = ModelSampleRepository.getModelSampleByCondition(id)
        modelsamples = []
        for modelsample in resultSets:
            modelsamples.append(ModelSample(modelsample))
        return modelsamples


# print(ModelSampleService.getModelSampleByCondition(5))