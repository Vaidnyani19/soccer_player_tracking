from utils.reid_utils import load_reid_model, extract_features_from_folder
import os

print("📁 Broadcast Crops:", os.listdir("crops/broadcast")[:5])
print("📁 Tacticam Crops:", os.listdir("crops/tacticam")[:5])

model = load_reid_model()

print("🔍 Extracting features for broadcast...")
extract_features_from_folder(
    model=model,
    image_folder="crops/broadcast",
    save_path="features/broadcast_features.pt"
)

print("🔍 Extracting features for tacticam...")
extract_features_from_folder(
    model=model,
    image_folder="crops/tacticam",
    save_path="features/tacticam_features.pt"
)
