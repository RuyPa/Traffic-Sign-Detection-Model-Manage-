

import sys
sys.path.append("D:\\test flask cors")
from modelV1.Label import Label


class Sample:
    def __init__(self, id, code, name, path, labels):
        self.id = id
        self.code = code
        self.name = name
        self.path = path
        self.labels = [Label.from_dict(label_data) for label_data in labels]

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            code=data['code'],
            name=data['name'],
            path=data['path'],
            labels=data['label']
        )