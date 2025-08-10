import streamlit as st
import numpy as np
import scipy.io.wavfile as wavfile
import io
import json
from sound_generator import generate_binaural_beat

def load_brainwave_frequencies(config_path="config.json"):
    """Loads brainwave frequencies from a JSON config file."""
    with open(config_path, "r") as f:
        return json.load(f)

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("Binaural Beat Generator")

    # Load brainwave frequencies from config
    brainwave_frequencies = load_brainwave_frequencies()

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

if __name__ == "__main__":
    main()