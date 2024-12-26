from transformers import pipeline
from gtts import gTTS
import streamlit as st
import os

# Initialize the chatbot model
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

# Streamlit UI
st.title("AI Text-to-Speech Chatbot")
st.write("Chat with an AI-powered bot that speaks its replies! Type your message below.")

# User input
user_input = st.text_input("You:", key="user_input")

if user_input:
    if user_input.lower() in ["exit", "quit"]:
        st.write("Thanks for using this Chatbot! Refresh the page to restart.")
    else:
        # Generate chatbot response
        response = chatbot(user_input, max_length=100, clean_up_tokenization_spaces=True)
        chatbot_reply = response[0]["generated_text"]
        st.write("Chatbot:", chatbot_reply)

        # Text-to-speech with gTTS
        tts = gTTS(chatbot_reply)
        tts.save("response.mp3")

        # Play audio in Streamlit
        audio_file = open("response.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        # Remove audio file after playing
        os.remove("response.mp3")
