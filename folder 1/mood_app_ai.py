# mood_app.py

import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

st.title("🧠 AI Mood Detector")
st.write("Speak or type how you feel and let AI detect your mood!")

# Text input
user_input = st.text_input("🗣️ How are you feeling today?")

if user_input:
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']

    # Display result
    st.write(f"**Detected Mood:** {label} ({score*100:.2f}%)")

    # Recommend something based on mood
    if label == "POSITIVE":
        st.success("You seem happy! 😊 Here's a feel-good playlist 🎶: [Spotify](https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0)")
    elif label == "NEGATIVE":
        st.warning("Feeling low? 😔 Try this relaxing video 🌿: [YouTube](https://www.youtube.com/watch?v=2OEL4P1Rz04)")
    else:
        st.info("Neutral mood detected. Here's something interesting: [Article](https://www.psychologytoday.com/)")

