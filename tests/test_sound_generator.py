import numpy as np
import pytest
from sound_generator import generate_binaural_beat

def test_generate_binaural_beat_output_shape():
    """
    Tests that the output audio has the correct shape (n_samples, 2).
    """
    sample_rate, audio = generate_binaural_beat(frequency=10, duration=1)
    assert audio.ndim == 2
    assert audio.shape[1] == 2

def test_generate_binaural_beat_output_dtype():
    """
    Tests that the output audio has a float data type.
    """
    sample_rate, audio = generate_binaural_beat(frequency=10, duration=1)
    assert np.issubdtype(audio.dtype, np.floating)

def test_generate_binaural_beat_sample_rate():
    """
    Tests that the returned sample rate is correct.
    """
    sample_rate, audio = generate_binaural_beat(frequency=10, duration=1, sample_rate=48000)
    assert sample_rate == 48000

def test_generate_binaural_beat_duration():
    """
    Tests that the duration of the audio is correct.
    """
    duration = 2
    sample_rate = 44100
    _, audio = generate_binaural_beat(frequency=10, duration=duration, sample_rate=sample_rate)
    expected_samples = duration * sample_rate
    assert audio.shape[0] == expected_samples

def test_generate_binaural_beat_volume():
    """
    Tests that the volume parameters are applied correctly.
    A volume of 0 should result in a silent channel.
    """
    _, audio_left_silent = generate_binaural_beat(frequency=10, duration=1, left_volume=0)
    assert np.all(audio_left_silent[:, 0] == 0)

    _, audio_right_silent = generate_binaural_beat(frequency=10, duration=1, right_volume=0)
    assert np.all(audio_right_silent[:, 1] == 0)
