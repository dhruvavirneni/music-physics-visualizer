import librosa
import librosa.display
import matplotlib.pyplot as plt


# load audio file
file = r"C:\Users\avirn\Dhruvcoding\music-physics-visualizer\audio\crsound.wav"
y, sr = librosa.load(file, sr=None)

plt.figure(figsize=(10, 6))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform of Audio")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()