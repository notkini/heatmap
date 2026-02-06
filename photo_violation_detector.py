import os
import cv2
from ultralytics import YOLO
from violation_logger import log_violation

model = YOLO("model.pt")

PHOTO_FOLDER = "photos"

CLASS_MAP = {
    0: "helmet",
    1: "no_helmet",
    2: "rider",
    3: "plate"
}

for photo in os.listdir(PHOTO_FOLDER):

    path = os.path.join(PHOTO_FOLDER, photo)
    frame = cv2.imread(path)

    if frame is None:
        continue

    print("\nProcessing:", photo)

    results = model(frame)[0]

    for box in results.boxes.data.tolist():

        x1, y1, x2, y2, conf, cls = box
        cls = int(cls)

        if conf < 0.4:
            continue

        label = CLASS_MAP.get(cls, "unknown")

        print("Detected:", label)

        if label == "no_helmet":
            log_violation("no_helmet", photo)

print("\nDetection complete.")
