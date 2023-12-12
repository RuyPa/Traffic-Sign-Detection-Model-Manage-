import os
from ultralytics import YOLO
import cv2
from model import Model
import pymysql



db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="managesample"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM managesample.model")
result = cursor.fetchall()
models = []
for row in result:
    model = Model.Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    models.append(model.__dict__)

last_item = models[-1]['path']

base_path = "\\".join(last_item.split("\\")[:-2])

lastNumber = int (base_path[-1]) + 1

newPath = base_path[:-1] + str(lastNumber)

print(newPath)

# Ghép chuỗi "results.csv" vào phần đường dẫn cắt được
final_path = os.path.join(newPath, "results.csv")

# In ra đường dẫn kết quả
print(final_path)

# model = YOLO("D:\\test flask cors\\runs\\detect\\train3\\weights\\best.pt")
# results = model.train(data="configretrain.yaml", epochs=1 )

# # test phat hien vung anh cua 1 anh

# model = YOLO("D:\\test flask cors\\runs\\detect\\train6\\weights\\best.pt")
# results = model("D:\\test flask cors\\retrain\\images\\train\\00281.png")


# # Load ảnh
# frame = cv2.imread("D:\\test flask cors\\data\\images\\train\\t10b.jpg")



# # Load model
# model = YOLO("D:\\test flask cors\\runs\\detect\\train\weights\\best.pt")  # load a custom model

# threshold = 0.5
# print(1)
# # Xử lý ảnh
# results = model(frame)[0]
# print(1)
# for result in results.boxes.data.tolist():
#     print(2)
#     x1, y1, x2, y2, score, class_id = result

#     # if score > threshold:
#     print()

# cv2.destroyAllWindows()
