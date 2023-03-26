import pyttsx3

# Initialize the Pyttsx3 engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Set the pitch of the voice
engine.setProperty('rate', 250.0)

# Say something
engine.say('Hello, world!')

# Run the engine
engine.runAndWait()