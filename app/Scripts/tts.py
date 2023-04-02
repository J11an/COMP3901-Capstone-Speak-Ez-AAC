import pyttsx3

def text_to_speech(text, gender):
 
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    engine.setProperty('rate', 125)

    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)
    
    engine.save_to_file(text , "message.mp3")
    engine.runAndWait()
