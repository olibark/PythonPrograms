import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load the audio file
# Replace 'your_audio.mp3' with your audio file path
y, sr = librosa.load('/Users/oliverbarkham/Documents/Python_programs/clocks/mixkit-epic-impact-afar-explosion-2782.wav')

# Basic audio processing examples:

# 1. Display waveform
plt.figure(figsize=(14, 5))
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform')
plt.show()
# 2. Compute and display mel spectrogram
mel_spect = librosa.feature.melspectrogram(y=y, sr=sr)
mel_spect_db = librosa.power_to_db(mel_spect, ref=np.max)
plt.figure(figsize=(14, 5))
librosa.display.specshow(mel_spect_db, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')
plt.show()

# 3. Extract tempo and beat frames
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(f'Estimated tempo: {tempo:.2f} beats per minute')

# 4. Extract pitch features
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
print(f'Pitch shape: {pitches.shape}')