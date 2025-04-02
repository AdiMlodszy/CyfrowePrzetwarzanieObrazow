from ultralytics import YOLO

model = YOLO("../runs/detect/Training/weights/best.pt")  # Load the trained model
results = model.predict(
    source="../data/dataset/images/360p.mp4",
    name="predict_run",  # Name of the prediction run
    project="../runs_predict",  # Directory to save the prediction results 
    conf=0.25,  # Confidence threshold
    batch=4,  # Batch size
    show=True,
    save=True,  # Save predictions
    )  # Predict on the test set

