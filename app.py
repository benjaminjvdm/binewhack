import streamlit as st
import numpy as np
import scipy.io.wavfile as wavfile
import io

# Define brainwave frequencies
brainwave_frequencies = {
    "Gamma": (30, 100),
    "Beta": (14, 30),
    "Alpha": (9, 13),
    "Theta": (4, 8),
    "Delta": (1, 3),
}

# Function to generate binaural beat audio
def generate_binaural_beat(frequency, duration=1220, left_volume=0.5, right_volume=0.5, sample_rate=44100):
    # Generate sine wave for left and right channels
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    left_freq = 440 + frequency / 2
    right_freq = 440 - frequency / 2
    left_channel = left_volume * np.sin(2 * np.pi * left_freq * t)
    right_channel = right_volume * np.sin(2 * np.pi * right_freq * t)

    # Combine channels into stereo audio
    audio = np.vstack((left_channel, right_channel)).T
    return sample_rate, audio

# Streamlit UI
st.title("Binaural Beat Generator")

# Brainwave state selection
brainwave_state = st.selectbox("Select Brainwave State", list(brainwave_frequencies.keys()))

# Volume control
left_volume = st.slider("Left Volume", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
right_volume = st.slider("Right Volume", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

# Generate audio
frequency_range = brainwave_frequencies[brainwave_state]
frequency = np.mean(frequency_range)  # Use the mean frequency for simplicity
sample_rate, audio = generate_binaural_beat(frequency, left_volume=left_volume, right_volume=right_volume)

# Convert audio to WAV bytes
wav_bytes = io.BytesIO()
wavfile.write(wav_bytes, sample_rate, audio.astype(np.float32))
wav_bytes = wav_bytes.getvalue()

# Play audio
st.audio(wav_bytes, format="audio/wav", sample_rate=sample_rate, loop=True)