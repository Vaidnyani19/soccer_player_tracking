from utils.video_utils import extract_frames
from utils.detection_utils import run_detection_on_folder
from utils.crop_utils import crop_players_from_frames
import os

if __name__ == "__main__":
    print(">>> Starting Frame Extraction...")

    if not os.path.exists("detections/frames_broadcast"):
        extract_frames("videos/broadcast.mp4", "detections/frames_broadcast", step=5)
        print("✓ Frames extracted from broadcast.mp4")
    else:
        print("✓ Skipping frame extraction for broadcast.mp4 (already exists)")

    if not os.path.exists("detections/frames_tacticam"):
        extract_frames("videos/tacticam.mp4", "detections/frames_tacticam", step=5)
        print("✓ Frames extracted from tacticam.mp4")
    else:
        print("✓ Skipping frame extraction for tacticam.mp4 (already exists)")

    print("\n>>> Starting YOLOv11 Player Detection...")

    run_detection_on_folder(
        model_path="models/yolov11.pt",
        frame_folder="detections/frames_broadcast",
        save_json_path="detections/broadcast_detections.json"
    )
    print("✓ Finished player detection on broadcast.mp4")

    run_detection_on_folder(
        model_path="models/yolov11.pt",
        frame_folder="detections/frames_tacticam",
        save_json_path="detections/tacticam_detections.json"
    )
    print("✓ Finished player detection on tacticam.mp4")

    print("\n>>> Cropping player images...")

    crop_players_from_frames(
        frame_folder="detections/frames_broadcast",
        detections_json="detections/broadcast_detections.json",
        output_folder="crops/broadcast"
    )

    crop_players_from_frames(
        frame_folder="detections/frames_tacticam",
        detections_json="detections/tacticam_detections.json",
        output_folder="crops/tacticam"
    )

    print("✅ Player cropping completed!")
    print("\n✅ All tasks completed successfully!")
