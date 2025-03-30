# scripts/train_yolo.py

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="/app/data/dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    project="runs",
    name="detect-train",
    exist_ok=True
)
