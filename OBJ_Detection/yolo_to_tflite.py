from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO(r"Path to your model file")

# Export the model to TFLite format
model.export(format="tflite")  # creates 'yolo11n_float32.tflite'

