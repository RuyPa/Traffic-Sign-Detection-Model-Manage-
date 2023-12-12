class Label:
    def __init__(self, rowInResult):
        self.id = int(rowInResult[0])
        self.height = rowInResult[1]
        self.width = rowInResult[3]
        self.x_center = rowInResult[4]
        self.y_center = rowInResult[5]

    @classmethod
    def constructorV1(cls, id, height, width, x_center, y_center):
        label = cls([id, height, None, width, x_center, y_center])
        return label