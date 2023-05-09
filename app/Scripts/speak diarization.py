from vosk import Model,KaldiRecognizer
import pyaudio
import numpy as np 
from app import app, socketio

#Load the Vosk model

model_dir= "model/vosk-model-en-us-aprise-0.2"
model=Model(model_dir)

#Create a KaldiRecognizer with the Vosk model
rec=KaldiRecognizer(model,16000)

#Create a PyAudio object
p=pyaudio.PyAudio()

#Define a callback function to handle audio data

def callback(data,count,time,status):
    if status:
        print(status,file=sys.stderr)

    #Convert the audio to a np array
    audio=np.frombutter(in_data,dtype=np.int16)

    #Send the audio to the recognizer
    rec.AcceptWaveform(audio)

    #Get the partial transcirption to the client
    text=rec.PartialResult()

    #Send the partial trascription to the client
    socketio.emit('transcription',text)
    return (data,pyaudio.paContinue)

#Define a route for the speaker diarization page
@app.route('\')
def speaker_dia():
    return render_template('')

#Define a SocketIO event handler to start and stop the 
# audio stream @socketio.on('stream')

def stream_handler(streaming):
    if streaming:
        #Start the audio stream
        stream=p.open(format=pyaudio.paInt16,channels=1,rate=16000,
        input=True,frameperbuffer=1024,stream_callback=audio_callback)
        stream.start_stream()
    else:
        #Stop the audio stream
        stream.stop_stream()
        stream.close()

#Define a SocketIO event handler to perform speaker diariazation @socterio.on('diarization")
def dia_handler(data):
    #get the full transcription from the recoginzer
    text=rec.FinalResult()

    #Perform speaker dia

    #Send the dia results to the client
    socketio.emit('diarization_results,' results)
