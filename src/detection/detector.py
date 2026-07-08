"""
YOLO Object Detection Module
RoboVision AI
"""

from ultralytics import YOLO


class YOLODetector:
    def __init__(self, model_path="yolov8n.pt"):
        print("[INFO] Loading YOLO model...")
        self.model = YOLO(model_path)
        print("[INFO] YOLO model loaded successfully!")

    def detect(self, frame):
        results = self.model(frame)
        annotated_frame = results[0].plot()
        return annotated_frame