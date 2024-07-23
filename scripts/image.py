from ultralytics import YOLO
model = YOLO("assets/best.pt")
results = model.predict("image.jpg")