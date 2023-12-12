class Model:
    def __init__(self, rowInResult):
        self.id = rowInResult[0]
        self.name = rowInResult[1]
        self.path = rowInResult[2]
        self.acc = rowInResult[3]
        self.pre = rowInResult[4]
        self.recall = rowInResult[5]
        self.f1 = rowInResult[6]
        self.status = rowInResult[7]
        self.datasetId = rowInResult[8]
        self.modelsampleList = []

    def modelConstructor(precision, recall, f1):
        model = Model
        model.acc = 0
        model.pre = precision
        model.recall = recall
        model.f1 = f1
        return model
    
    def modelConstructor1(id, name, path, acc, pre, recall, f1):
        model = Model
        model.id = id
        model.name = name
        model.path = path
        model.acc = 0
        model.pre = pre
        model.recall = recall
        model.f1 = recall
        model.status = ""
        return model
    
    def modelConstructor2(id, name, path, acc, pre, recall, f1, datasetId):
        model = Model
        model.id = id
        model.name = name
        model.path = path
        model.acc = 0
        model.pre = pre
        model.recall = recall
        model.f1 = recall
        model.status = ""
        model.datasetId = datasetId
        return model
    
    def modelConstructor3(id, name, path, acc, pre, recall, f1, modelsamples):
        model = Model
        model.id = id
        model.name = name
        model.path = path
        model.acc = 0
        model.pre = pre
        model.recall = recall
        model.f1 = recall
        model.status = ""
        model.modelsampleList = modelsamples
        return model