import sys
sys.path.append("D:\\test flask cors")



from service.ModelService import ModelService
from service.DatasetService import DatasetService

# print(DatasetService.getModelByCondition("data"))

ModelService.retrainModelV2(7, 3)