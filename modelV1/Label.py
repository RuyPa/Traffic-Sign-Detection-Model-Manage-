class Label:
    def __init__(self, id, height, width, x_center, y_center):
        self.id = id
        self.height = height
        self.width = width
        self.x_center = x_center
        self.y_center = y_center

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            height=data['height'],
            width=data['width'],
            x_center=data['x_center'],
            y_center=data['y_center']
        )