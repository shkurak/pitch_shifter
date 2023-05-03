import numpy as np


def pitch_shift(data: np.ndarray, shift_factor=2) -> np.ndarray:
    # Transform the input data to the frequency domain using the FFT
    freq_data = np.fft.rfft(data)

    # Create an array of zeros with the same length and data type as the frequency data
    shifted_freq_data = np.zeros(len(freq_data), freq_data.dtype)

    # Calculate the indices to shift the frequency data
    shift_amount = int(np.round(shift_factor if shift_factor > 0 else len(freq_data) + shift_factor, 0))
    remaining_amount = len(freq_data) - shift_amount

    # Shift the frequency data
    shifted_freq_data[:shift_amount] = freq_data[remaining_amount:]
    shifted_freq_data[shift_amount:] = freq_data[:remaining_amount]

    # Transform the shifted frequency data back to the time domain using the IFFT
    shifted_data = np.fft.irfft(shifted_freq_data)

    # Return the shifted data with the same data type as the input data
    return shifted_data.astype(data.dtype)
