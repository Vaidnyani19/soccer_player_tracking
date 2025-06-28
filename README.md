⚽ Soccer Player Re-Identification using YOLOv5 and Re-ID

A complete web-based system for soccer player tracking and re-identification using two different camera views (broadcast and tacticam). It uses YOLOv5 for player detection and a Re-ID model for matching players across views.


🔍 Features

- 🎥 Frame extraction from soccer videos
- 🧠 Player detection using YOLOv5
- ✂️ Cropping player images
- 🧬 Feature extraction via a Re-ID model
- 🔁 Matching players across camera views
- 🌐 Flask-based web interface
- 🖼️ Visual output of player matches

 📁 Project Structure

├── app.py # Flask web app
├── templates/ # HTML templates
├── static/ # CSS/JS/static assets
├── uploads/ # Uploaded videos
├── detections/ # YOLOv5 detection outputs
├── crops/ # Cropped player images
├── features/ # Re-ID features
├── matches/ # Matched player images
├── visualize_matches.py # Match visualization
├── requirements.txt
├── README.md

 🧠 How It Works

1. Upload broadcast and tacticam videos via the web interface.
2. Extract frames at intervals.
3. Detect players using YOLOv5.
4. Crop and save player images.
5. Extract features using a Re-ID model.
6. Match players based on feature similarity.
7. Visualize top matches in the `matches/` folder and on the web.


 ⚙️ Tech Stack

- **Backend**: Python, Flask
- **Detection**: YOLOv5 (PyTorch)
- **Re-Identification**: Torch ReID model
- **Visualization**: OpenCV, Matplotlib
- **Deployment**: Render (can be moved to Fly.io or GCP)

🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/soccer-player-tracking.git
cd soccer-player-tracking
2. Install Dependencies

pip install -r requirements.txt
📌 Recommended: Use Python 3.8 or 3.9

3. Download YOLOv5 Model
Download yolov11.pt from Google Drive
Place it in the models/ directory.

4. Run the App
python app.py
App will be available at http://localhost:10000/

🧪 Example Results
frame_00000_player_0.jpg → frame_00007_player_21.jpg (similarity: 0.7456)
frame_00001_player_1.jpg → frame_00013_player_6.jpg (similarity: 0.825)
Visualizations will appear in the matches/ folder and web interface.

🧩 Dependencies
Key dependencies (also listed in requirements.txt):
flask
torch, torchvision
opencv-python
matplotlib
gdown
yolov5 (local repo)

⭐ Future Improvements
Real-time video tracking and updates
Multi-camera synchronization
OCR for jersey numbers
Interactive dashboard with stats

📬 Contact
Made with ❤️ by Vaidnyani Thakare
📧 vaidnyanithakare19@gmail.com
📱 +91 8208217012
