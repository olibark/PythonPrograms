import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Text to convert to speech
text = "Hello! This is a text-to-speech conversion in Python."

# Speak the text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
