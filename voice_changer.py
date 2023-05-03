import time
import pyaudio
import numpy as np
from pitch_shifter import pitch_shift

WIDTH = 2
CHANNELS = 2
RATE = 44100
FRAMES_PER_BUFFER = 4096
SHIFT_FACTOR = 5

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    # Convert the byte data into a numpy array
    in_data_np = np.frombuffer(in_data, dtype=np.int16)

    # Apply the pitch shift
    new_data_np = pitch_shift(in_data_np, shift_factor=SHIFT_FACTOR)

    # Convert the numpy array back into byte data
    new_data = new_data_np.astype(np.int16).tobytes()

    return (new_data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback,
                frames_per_buffer=FRAMES_PER_BUFFER)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()
