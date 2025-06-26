import torch
import os
from PIL import Image

# Paths
broadcast_crop_dir = "crops/broadcast"
tacticam_crop_dir = "crops/tacticam"
matches_file = "results/reid_matches.pt"
output_dir = "matches"

os.makedirs(output_dir, exist_ok=True)

# Load saved matches
matches = torch.load(matches_file)

# Iterate and create visual match images
for i, (broadcast_img, match_info) in enumerate(matches.items()):
    tacticam_img = match_info["match"]
    sim_score = match_info["similarity"]

    path_b = os.path.join(broadcast_crop_dir, broadcast_img)
    path_t = os.path.join(tacticam_crop_dir, tacticam_img)

    if not os.path.exists(path_b) or not os.path.exists(path_t):
        continue

    # Open and resize images
    img_b = Image.open(path_b).resize((128, 256))
    img_t = Image.open(path_t).resize((128, 256))

    # Create combined image
    combined = Image.new("RGB", (256, 256))
    combined.paste(img_b, (0, 0))
    combined.paste(img_t, (128, 0))

    # Save with filename showing similarity
    save_name = f"match_{i:03d}_{sim_score:.2f}.jpg"
    combined.save(os.path.join(output_dir, save_name))

print(f"✅ Saved match visualizations to '{output_dir}'")
