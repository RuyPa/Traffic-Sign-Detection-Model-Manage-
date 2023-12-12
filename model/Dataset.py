class Dataset:
    def __init__(self, rowInResult):
        self.id = rowInResult[0]
        self.name = rowInResult[1]
        self.path = rowInResult[2]
