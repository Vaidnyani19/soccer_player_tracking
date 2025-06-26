import torch
from torchvision import transforms
from PIL import Image
import os
from tqdm import tqdm
import torchreid

def load_reid_model():
    print("🧠 Loading Re-ID model (osnet_x1_0)...")
    model = torchreid.models.build_model(
        name='osnet_x1_0',
        num_classes=1000,
        pretrained=True
    )
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    print(f"✅ Model loaded on device: {device}")
    return model

def extract_features_from_folder(model, image_folder, save_path):
    device = next(model.parameters()).device
    transform = transforms.Compose([
        transforms.Resize((256, 128)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])

    features = {}
    if not os.path.exists(image_folder):
        print(f"❌ Folder not found: {image_folder}")
        return

    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png'))]
    if not image_files:
        print(f"⚠ No valid image files in: {image_folder}")
        return

    print(f"🔍 Found {len(image_files)} images in {image_folder}")

    for img_name in tqdm(image_files, desc=f"Extracting features from {image_folder}"):
        img_path = os.path.join(image_folder, img_name)
        try:
            img = Image.open(img_path).convert("RGB")
            img = transform(img).unsqueeze(0).to(device)
            with torch.no_grad():
                feat = model(img).squeeze(0).cpu()
            features[img_name] = feat
        except Exception as e:
            print(f"❌ Error processing {img_name}: {e}")

    if features:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        torch.save(features, save_path)
        print(f"✅ Features saved to {save_path}")
    else:
        print("⚠ No features were extracted. Check your images or model.")
