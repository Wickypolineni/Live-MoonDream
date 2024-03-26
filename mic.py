from whisper_mic import WhisperMic

mic = WhisperMic(model="tiny.en")
while True:  
    text = mic.listen()
    print("You said:", text)