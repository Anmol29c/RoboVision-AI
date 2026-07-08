import cv2
from detection.detector import YOLODetector


class Camera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        self.detector = YOLODetector()

    def run(self):
        while True:
            success, frame = self.cap.read()

            if not success:
                print("[ERROR] Unable to read frame.")
                break

            # Detect objects
            frame = self.detector.detect(frame)

            cv2.imshow("RoboVision AI", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()