from ultralytics import YOLO

model = YOLO("/app/runs/detect-train/weights/best.pt")  

model.train(
    data="/app/data/data.yaml",  
    epochs=10,  # Number of epochs to train
    batch=8, # Batch size
    imgsz=640, # Image size for training
    resume=True,  # Resume training from the last checkpoint
    name="resume_training",  # Name of the training run
    exist_ok=True,  # Allow overwriting existing runs
    project="/app/runs/detect",  # Directory to save the training results
    save_period=1,  # Save model every epoch
    cache=True,  # Cache images for faster training
    workers=2,  # Number of workers for data loading
    rect=True,  # Rectangular training
)