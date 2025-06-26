from ultralytics import YOLO
import cv2
import os
import json
from tqdm import tqdm

def run_detection_on_folder(model_path, frame_folder, save_json_path):
    model = YOLO(model_path)

    results_data = {}

    frame_files = sorted([f for f in os.listdir(frame_folder) if f.endswith(".jpg")])

    for frame in tqdm(frame_files, desc=f"Detecting in {frame_folder}"):
        frame_path = os.path.join(frame_folder, frame)
        result = model(frame_path, conf=0.3)[0]

        detections = []
        for box in result.boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = box
            detections.append({
                "bbox": [x1, y1, x2, y2],
                "confidence": conf,
                "class": int(cls)
            })

        results_data[frame] = detections

    with open(save_json_path, "w") as f:
        json.dump(results_data, f, indent=2)

    print(f"[✓] Detection results saved to {save_json_path}")
