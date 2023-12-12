import sys
sys.path.append("D:\\test flask cors")  # Add the directory containing 'repositoryy' to sys.path
from repository.ModelRepository import ModelRepository  # Import the specific module
from model.Model import Model
from repository.DatasetRepository import DatasetRepository

# model = ModelRepository()  # Create an instance of the ModelRepository class

# result = model.getModelById(1)

# print(result)


# model = Model(8, "duy", "asdfsaf", 1,1,1,1)

# ModelRepository.insertModel(model)


# model = Model.modelConstructor2(9, "1", "1", 1,1,1,1, 0)
# ModelRepository.insertModelv2(model)

# print(DatasetRepository.getDatasetByCondition("data"))

print(ModelRepository.setActiveModel(3))

