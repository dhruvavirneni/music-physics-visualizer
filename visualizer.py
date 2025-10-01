import librosa
import librosa.display
import matplotlib.pyplot as plt
from flask import Flask, render_template


# load audio file

#file = r"C:\Users\avirn\Dhruvcoding\music-physics-visualizer\audio\crsound.wav"
#y, sr = librosa.load(file, sr=None)

#plt.figure(figsize=(10, 6))
#librosa.display.waveshow(y, sr=sr)
#plt.title("Waveform of Audio")
#plt.xlabel("Time (s)")
#plt.ylabel("Amplitude")
#plt.show()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>')
def user(name):
    return render_template('second.html', name=name)

app.run()