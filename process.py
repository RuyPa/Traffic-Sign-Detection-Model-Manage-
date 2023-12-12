from ultralytics import YOLO
import torch


model = YOLO("YOLOv8n.yaml")

# Load the trained model weights
results= model.load("C:\\Users\\Admin\\Desktop\\pythonProject\\runs\\detect\\train\\weights\\best.pt")

# Get the PyTorch mode

# Access the evaluation results
metrics = results.stats()
print(metrics)