import numpy as np
import librosa
import soundfile as sf
from pitch_shifter import pitch_shift

# Load the audio file
audio_file_path = "sample.wav"
audio, sample_rate = librosa.load(audio_file_path, sr=None, mono=True)

# Set the hop size and initialize an empty list to store pitch-shifted chunks
chunk_size = 0.08 # sec
hop_size = int(chunk_size * sample_rate)
PITCH_FACTOR = -5
pitch_shifted_chunks = []

# Iterate through the audio in chunks and apply the pitch_shift function
for i in range(audio.shape[0] // hop_size):
    chunk = audio[i * hop_size : (i + 1) * hop_size]
    pitch_shifted_chunk = pitch_shift(chunk, PITCH_FACTOR)
    pitch_shifted_chunks.append(pitch_shifted_chunk)

# Concatenate the pitch-shifted chunks into a single audio array
shifted_audio = np.hstack(pitch_shifted_chunks)

# Save the pitch-shifted audio to a file
output_file_path = 'shifted.wav'
sf.write(output_file_path, shifted_audio, sample_rate)