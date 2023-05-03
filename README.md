# Pitch Shifter

This repository contains a pitch shifting implementation for audio processing using the Fast Fourier Transform (FFT) and the Inverse Fast Fourier Transform (IFFT). The pitch shifting can be applied to audio files or in real-time using the provided scripts.

## Files

### pitch_shifter.py

This file contains the `pitch_shift` function, which takes an input audio array and a pitch shift factor and returns a pitch-shifted audio array.

```python
def pitch_shift(data: np.ndarray, shift_factor=2) -> np.ndarray:
    ...
```

### change_voice_in_file.py

This script demonstrates how to apply the `pitch_shift` function to an audio file in chunks. It reads an audio file, processes it in chunks using the `pitch_shift` function, and saves the pitch-shifted audio to a new file.

### voice_changer.py

This script demonstrates how to apply the `pitch_shift` function in real-time using the `pyaudio` library. It captures audio input from the microphone, applies the pitch shift, and plays back the pitch-shifted audio through the speakers.

## Usage

### Requirements

- Python 3.7 or higher
- NumPy
- LibROSA
- SoundFile
- PyAudio

### Example: Change the pitch of an audio file

1. Set the input audio file path in `change_voice_in_file.py`:

   ```python
   audio_file_path = "sample.wav"
   ```

2. Set the pitch shift factor (positive or negative integer) in `change_voice_in_file.py`:

   ```python
   PITCH_FACTOR = -5
   ```

3. Run the `change_voice_in_file.py` script:

   ```
   python change_voice_in_file.py
   ```

   The pitch-shifted audio will be saved as `shifted.wav`.

### Example: Real-time pitch shifting

1. Set the pitch shift factor (positive or negative integer) in `voice_changer.py`:

   ```python
   SHIFT_FACTOR = 5
   ```

2. Run the `voice_changer.py` script:

   ```
   python voice_changer.py
   ```

   The script will capture audio from the microphone, apply the pitch shift, and play back the pitch-shifted audio through the speakers. To stop the script, press `Ctrl+C`.