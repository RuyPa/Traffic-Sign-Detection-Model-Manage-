import sys
sys.path.append("D:\\test flask cors")
import pandas as pd
import csv
import pymysql
from model import Model
import os
import glob 
import os

db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="managesample"
)

cursor = db.cursor()


def getPathResult():


    cursor.execute("SELECT * FROM managesample.model")
    result = cursor.fetchall()
    models = []
    for row in result:
        model = Model.Model(row)
        models.append(model.__dict__)

    # print(models)

    last_item = models[-1]['path']

    last_id = models[-1]['id']

    base_path = "\\".join(last_item.split("\\")[:-2])

    # test cho file gen ra tiep theo
    lastNumber = int (base_path[-1]) + 1
    # lastNumber = int (base_path[-1])

    newPath = base_path[:-1] + str(lastNumber) + '\\results.csv'
    return newPath, last_id





def countFile(a):
    directory_path = a
    all_files = glob.glob(os.path.join(directory_path, '*'))
    image_extensions = ('.jpg', '.png')
    image_files = [file for file in all_files if file.lower().endswith(image_extensions)]

    num_images = len(image_files)

    print(f'The number of image files in the directory is: {num_images}')
    return num_images


def deleteFile(modelPath):
    filePath = "\\".join(modelPath.split("\\")[:-2])
    os.chmod(filePath, 0o777)
    os.remove(filePath)




# getPathResult()

# path, id = getPathResult()

# print(path)
# print(id)