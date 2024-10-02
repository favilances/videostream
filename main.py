from flask import Flask, Response
import cv2
import subprocess

app = Flask(__name__)

video_path = 'video.mp4'  # Kendi video dosyanızın yolunu buraya girin

@app.route('/')
def index():
    return "<p>Yayına erişmek için <a href='/video'>tıklayın</a>.</p>"

def generate_frames():
    command = [
    r'C:\Users\favilances\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1-full_build\bin\ffmpeg.exe',  # FFmpeg'in tam yolunu buraya girin
    '-i', video_path,
    '-f', 'mpegts',
    'pipe:1'
]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        frame = process.stdout.read(1024)
        if not frame:
            break
        yield frame

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='video/mp2t')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# vlc ile çalışıyor http://127.0.0.1:5000/video