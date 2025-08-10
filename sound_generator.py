import numpy as np

def generate_binaural_beat(frequency, duration=1220, left_volume=0.5, right_volume=0.5, sample_rate=44100):
    """
    Generates a binaural beat audio signal.

    Args:
        frequency (float): The frequency difference between the left and right channels.
        duration (int, optional): The duration of the audio in seconds. Defaults to 1220.
        left_volume (float, optional): The volume of the left channel (0.0 to 1.0). Defaults to 0.5.
        right_volume (float, optional): The volume of the right channel (0.0 to 1.0). Defaults to 0.5.
        sample_rate (int, optional): The sample rate of the audio. Defaults to 44100.

    Returns:
        tuple: A tuple containing the sample rate and the generated stereo audio as a numpy array.
    """
    # Generate sine wave for left and right channels
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    base_frequency = 440  # A4 note as the base frequency
    left_freq = base_frequency + frequency / 2
    right_freq = base_frequency - frequency / 2
    left_channel = left_volume * np.sin(2 * np.pi * left_freq * t)
    right_channel = right_volume * np.sin(2 * np.pi * right_freq * t)

    # Combine channels into stereo audio
    audio = np.vstack((left_channel, right_channel)).T
    return sample_rate, audio
