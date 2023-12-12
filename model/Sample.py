

import sys
sys.path.append("D:\\test flask cors")
from repository.SampleRepository import SampleRepository
from model.Label import Label


class Sample:
    def __init__(self, rowInResult):
        self.id = int(rowInResult[0])
        self.code = rowInResult[1]
        self.name = rowInResult[2]
        self.path = rowInResult[3]
        self.label = []

