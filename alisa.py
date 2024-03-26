from pydub import AudioSegment
import os 
import cv2
import os
import uuid
from PIL import Image
import cv2
import speech_recognition as sr
import simpleaudio as sa
import threading
from gradio_client import Client,file

app_url="https://460c1d4fa3515c02dd.gradio.live/" 
#make sure app_url ends with a slash
try:
    client = Client(app_url)
except:
    print("Error: Could not connect to the server. Please make sure the URL is correct and the server is running.")

def mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")


if not os.path.exists("./compressed_image"):
    os.makedirs("./compressed_image")
if not os.path.exists("./audio"):
    os.makedirs("./audio")
# Generate a random image file name
def generate_image_name():
    # return f'./compressed_image/{str(uuid.uuid4())[:8]}.jpg'
    return f'./compressed_image/temp.jpg'

def compress_image(frame, quality=50):
    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    convert_pil = Image.fromarray(frame_rgb)
    output_image_path = generate_image_name()
    convert_pil.save(output_image_path, optimize=True, quality=quality)
    return output_image_path


def play_audio(filename):
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def describe_image(prompt, image_file):
	if len(prompt) == 0:
		prompt = "Describe the image in single sentence"

	result = client.predict(
			prompt, 
			file(image_file),	
			api_name="/predict"
			)
	print(result)
	mp3_file = result
	base_path = os.path.basename(mp3_file).split(".")[0]
	wav_file = f"./audio/{base_path}.wav"
	mp3_to_wav(mp3_file, wav_file)
	play_audio(wav_file)    
def speech_recognition(source):
    recognizer = sr.Recognizer()

    while True:  
        print("Say something...")

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            if "alisha" in text.lower():
                print("Triggering the API...")
                play_audio("okay.wav")
                prompt = text.lower().split("alisha")[-1].strip()
                prompt = prompt.strip().replace(",", " ").strip()
                print("Prompt:", prompt)
                upload_image = compress_image(frame)
                print(upload_image)
                describe_image(prompt, upload_image)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    # mic_list = sr.Microphone.list_microphone_names()
    # print("Available microphones:", mic_list)
    # desired_mic_index = 1
    # with sr.Microphone(device_index=desired_mic_index) as source:
    with sr.Microphone() as source:
        # print("Using microphone:", mic_list[desired_mic_index])
        speech_thread = threading.Thread(target=speech_recognition, args=(source,))
        speech_thread.start()

        while True:
            ret, frame = cap.read()
            cv2.imshow('Webcam', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
 