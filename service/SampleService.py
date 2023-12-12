import sys

sys.path.append("D:\\test flask cors")
from model.Sample import Sample
from repository.SampleRepository import SampleRepository


class SampleService:

    # def getModelById(modelId):
    #     resultSet = ModelRepository.getModelById(modelId)
    #     model = Model(resultSet)
    #     return model

    def getSampleByCondition(search_name):
        resultSets = SampleRepository.getSampleByCondition(search_name)
        samples = []
        for sample in resultSets:
            sample = Sample(sample)
            sample.label.append(SampleRepository.getLabelBySampleId(sample.id))
            samples.append(sample)
        return samples

    # def getAllDataset():
    #     resultSets = DatasetRepository.getAllDataset()
    #     datasets = []
    #     for dataset in resultSets:
    #         datasets.append(Dataset(dataset))
    #     return datasets

    def getSampleById(sampleId):
        resultSet = SampleRepository.getSampleById(sampleId)
        sample = Sample(resultSet)
        print(sample)
        return sample

    def getAllSample():
        resultSets = SampleRepository.getAllSample()
        samples = []
        for sample in resultSets:
            sample = Sample(sample)
            sample.label.append(SampleRepository.getLabelBySampleId(sample.id))
            samples.append(sample)
        return samples

# print(SampleService.getSampleById(13))