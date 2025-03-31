from ultralytics import YOLO
from google.colab import drive

drive.mount('/content/drive')

model = YOLO("/content/CyfrowePrzetwarzanieObrazow/runs/detect-train/weights/best.pt")  

model.train(
    data="/content/CyfrowePrzetwarzanieObrazow/data/dataset/data.yaml",  
    epochs=10,  # Number of epochs to train
    batch=4, # Batch size
    imgsz=640, # Image size for training
    resume=True,  # Resume training from the last checkpoint
    name="resume_training",  # Name of the training run
    exist_ok=True,  # Allow overwriting existing runs
    project="/content/drive/MyDrive/CyfrowePrzetwarzanieObrazow/runs/detect",  # Directory to save the training results
    cache=False,  # Cache images for faster training
    workers=2,  # Number of workers for data loading
    rect=False,  # Rectangular training
)