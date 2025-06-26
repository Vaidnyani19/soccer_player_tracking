from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'videos'
MATCHES_FOLDER = 'matches'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    os.makedirs('videos', exist_ok=True)
    os.makedirs('matches', exist_ok=True)
    app.run(debug=True)
