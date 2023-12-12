import sys
sys.path.append("D:\\test flask cors")
from repository.SampleRepository import SampleRepository
from model.Sample import Sample


class ModelSample:
    def __init__(self, rowInResult):
        self.id = rowInResult[0]
        self.sample = Sample(SampleRepository.getSampleById(rowInResult[2]))
    
    @classmethod
    def modelsampleConstructor1(cls, sample):
        # Use the class constructor instead of __init__
        modelsample = cls([0, 0, sample.id])  # Assuming rowInResult is a list
        return modelsample