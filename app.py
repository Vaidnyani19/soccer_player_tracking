from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from werkzeug.utils import secure_filename
import subprocess
import gdown

app = Flask(__name__)

UPLOAD_FOLDER = 'videos'
MATCHES_FOLDER = 'matches'
MODEL_PATH = 'models/yolov11.pt'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MATCHES_FOLDER, exist_ok=True)
os.makedirs("models", exist_ok=True)

# Auto-download YOLO model if not present
if not os.path.exists(MODEL_PATH):
    print("🔽 Downloading yolov11.pt model from Google Drive...")
    gdown.download("https://drive.google.com/uc?id=18xCk3rRx6194I4TkD73CuXKpiP7oQi09", MODEL_PATH, quiet=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'broadcast' not in request.files or 'tacticam' not in request.files:
        return "Missing file(s)", 400

    broadcast_file = request.files['broadcast']
    tacticam_file = request.files['tacticam']

    if broadcast_file.filename == '' or tacticam_file.filename == '':
        return "No selected file(s)", 400

    broadcast_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename('broadcast.mp4'))
    tacticam_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename('tacticam.mp4'))

    broadcast_file.save(broadcast_path)
    tacticam_file.save(tacticam_path)

    # Run detection, ReID, and matching
    subprocess.run(['python', 'main.py'])
    subprocess.run(['python', 'visualize_matches.py'])

    return redirect(url_for('show_matches'))

@app.route('/matches')
def show_matches():
    match_files = os.listdir(MATCHES_FOLDER)
    match_files = [f for f in match_files if f.endswith('.jpg') or f.endswith('.png')]
    return render_template('matches.html', match_files=match_files)

@app.route('/matches/<filename>')
def get_match_image(filename):
    return send_file(os.path.join(MATCHES_FOLDER, filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

