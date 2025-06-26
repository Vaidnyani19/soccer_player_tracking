import os
import cv2
import json

def crop_players_from_frames(frame_folder, detections_json, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    with open(detections_json, 'r') as f:
        detections = json.load(f)

    for frame_name, boxes in detections.items():
        frame_path = os.path.join(frame_folder, frame_name)
        if not os.path.exists(frame_path):
            print(f"⚠️ Frame not found: {frame_path}")
            continue

        frame = cv2.imread(frame_path)
        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box['bbox'])

            crop = frame[y1:y2, x1:x2]
            if crop.size == 0:
                continue

            crop_name = f"{os.path.splitext(frame_name)[0]}_player_{i}.jpg"
            crop_path = os.path.join(output_folder, crop_name)
            cv2.imwrite(crop_path, crop)

    print(f"[✓] Saved crops to {output_folder}")
