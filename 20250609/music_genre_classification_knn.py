import os
import numpy as np
import matplotlib.pyplot as plt
import librosa, librosa.display
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

signal, sr = librosa.load('music_genre/jazz/jazz.00001.wav')

librosa.display.waveshow(signal, sr=sr, alpha=0.5)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original waveform")
plt.savefig("waveform.png")

def extract_features(audio_path):
    signal, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(signal, sr)
    return np.mean(mfcc, axis = 0)

data_dir = 'music_genre'
features = []
labels = []

for genre in os.listdir(data_dir):
    genre_path = os.path.join(data_dir, genre)
    for audio_file in os.listdir(genre_path):
        audio_path = os.path.join(genre_path, audio_file)
        feature = extract_features(audio_path)
        features.append(feature)
        labels.append(genre)

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size = 0.3)

knn =KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)