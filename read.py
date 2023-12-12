# import pandas as pd
# import csv
# import pymysql
# from model import Model
#
# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="1234567",
#     database="managesample"
# )
#
# cursor = db.cursor()
#
# def algorithmEvaluation(path):
#     with open(path, "r") as f:
#         reader = csv.reader(f)
#         next(reader)
#         precision = 0
#         recall = 0
#         count = 0
#         f1 = 0
#         for row in reader:
#             count= count + 1
#             precision += float (row[4])
#             recall += float (row[5])
#             f1 += (2*precision * recall) / (precision +recall)
#         return 0, precision/ count, recall /count, f1 / count
#
# def getPathResult():
#
#
#     cursor.execute("SELECT * FROM managesample.model")
#     result = cursor.fetchall()
#     models = []
#     for row in result:
#         model = Model.Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
#         models.append(model.__dict__)
#
#     last_item = models[-1]['path']
#
#     last_id = models[-1]['id']
#
#     base_path = "\\".join(last_item.split("\\")[:-2])
#
#     # test cho file gen ra tiep theo
#     lastNumber = int (base_path[-1]) + 1
#     # lastNumber = int (base_path[-1])
#
#     newPath = base_path[:-1] + str(lastNumber) + '\\results.csv'
#     return newPath, last_id
#
# # path, lastid = getPathResult()
# # acc, precision, recall, f1 = algorithmEvaluation("D:\\test flask cors\\runs\\detect\\train7\\results.csv")
# # print (acc, precision , recall , f1 )
#
# # newModelPath = "\\".join(path.split("\\")[:-1]) + "\\weights\\best.pt"
#
# # print(newModelPath)
#
# # idd = lastid + 1
# # name = 'best.pt'
# # accuracy = acc
# # precision = precision
# # recall = recall
# # f1_score = f1
# # path = newModelPath
#
# # insert_query = "INSERT INTO managesample.model (id, name, path, acc, pre, recall, f1, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# # cursor.execute(insert_query, (idd, name, path, accuracy, precision, recall, f1_score, " "))
# # db.commit()
#
# # print(newModelPath)
#
