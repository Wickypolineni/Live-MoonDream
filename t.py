import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define a function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for audio input

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Recognize the audio using Google Speech Recognition
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Sorry, I couldn't request results. Please check your internet connection.")

# Main loop
while True:
    speech = recognize_speech()
    if speech and speech.lower() == "stop":  # Exit loop if "stop" is said
        break
