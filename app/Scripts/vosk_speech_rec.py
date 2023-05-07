from vosk import Model,KaldiRecognizer
import pyaudio
import os

model = Model(f"{os.path.abspath(os.getcwd())}\\public\\vosk-model-small-en-us-0.15")
recogniszer = KaldiRecognizer(model,16000)

def vosk_speech_reg():
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if recogniszer.AcceptWaveform(data):
            print(recogniszer.Result())

        