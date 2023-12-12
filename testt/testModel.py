import sys
sys.path.append("D:\\test flask cors")
from flask import Flask, jsonify, request
from flask_cors import CORS
from model.Model import Model


model = Model.modelConstructor(0,0,0)

print(model.acc)