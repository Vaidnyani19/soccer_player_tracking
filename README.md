# ⚽ Soccer Player Re-Identification using YOLOv5 and Re-ID

This project is a complete **soccer player tracking and re-identification system** that uses two different camera views (broadcast and tacticam). It detects players using YOLOv5, crops them, extracts their appearance features using a Re-ID model, and finds matches across views.

🚀 **Live Demo** 

## 🔍 Features

- 🎥 Frame extraction from soccer match videos  
- 🧠 Player detection using YOLOv5  
- ✂️ Cropping player images from frames  
- 🧬 Feature extraction using a Re-Identification model  
- 🔁 Matching players across camera views  
- 🌐 Web interface to upload video and view results  
- 🖼️ Visual output of matched player images  

## 📁 Project Structure

├── app.py # Flask app for the web interface
├── utils/ # Utility functions (detection, cropping, re-id)
├── templates/ # HTML templates (index, result)
├── static/ # Static assets like CSS
├── uploads/ # Uploaded videos
├── detections/ # JSON results from detection
├── crops/ # Cropped player images
├── features/ # .pt files storing extracted embeddings
├── matches/ # Visualized player matches
├── visualize_matches.py # Script to visualize best matches
├── requirements.txt
├── README.md



## 🧠 How It Works

1. **Upload** broadcast & tacticam videos via the web app.  
2. **Extract** frames at intervals.  
3. **Detect** players using a trained YOLOv5 model.  
4. **Crop** detected player images.  
5. **Extract features** using a pretrained Re-ID model.  
6. **Match** players across both views based on embedding similarity.  
7. **Visualize** top-k matches.

## ⚙️ Tech Stack

- **Backend**: Python, Flask  
- **Detection**: [YOLOv5](https://github.com/ultralytics/yolov5)  
- **Re-Identification**: Torch-based Re-ID model  
- **Visualization**: Matplotlib, OpenCV  
- **Deployment**: Render

## 🔧 Setup Instructions

### 
1. Clone the Repo
git clone https://github.com/yourusername/soccer-player-tracking.git
cd soccer-player-tracking
2. Install Dependencies
pip install -r requirements.txt
3. Download YOLOv5 Model
Download from [[Google Drive Link](https://drive.google.com/file/d/18xCk3rRx6194I4TkD73CuXKpiP7oQi09/view?usp=sharing)] and put it in models/.

4. Run the App
python app.py
🧪 Example Results
txt
Copy code
frame_00000_player_0.jpg → frame_00007_player_21.jpg (similarity: 0.7456)
frame_00001_player_1.jpg → frame_00013_player_6.jpg (similarity: 0.825)
Top match visualizations will appear in the matches/ folder and on the web interface!

📬 Contact
Made with ❤️ by Vaidnyani Thakare
📧 vaidnyanithakare19@gmail.com
📱 +91 8208217012

⭐ Future Improvements
1.Real-time tracking and visualization
2.Multi-camera synchronization
3.Player jersey number OCR
4.Dashboard for interactive analysis

🏁 License
This project is licensed under the MIT License - see the LICENSE file for details.
