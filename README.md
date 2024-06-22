# 🌔 Moondream Realtime
A tiny vision language model that runs anywhere

[Website](https://moondream.ai/) | [Hugging Face](https://huggingface.co/vikhyatk/moondream2) | [Demo](https://huggingface.co/spaces/vikhyatk/moondream2) | [Moondream Github](https://github.com/vikhyat/moondream)

### Run This to make a gradio server and Copy the gradio url
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuralfalcon/moondream-realtime/blob/main/Moondream_Realtime.ipynb) <br>
### How to setup client:
Using Whisper Speech to text:<br>
```pip install -r whisper_requirements.txt```<br>
```whisper_client.py```
<br><br>
Or, Use google Speech Recognition: <br>
```pip install -r google_requirements.txt```<br>
```google_client.py```<br>

### In the both cases repalce the url
```app_url="https://460c1d4fa3515c02dd.gradio.live/" ```

If you don't want to use the vs code due to low ram
first setup the ``app_url`` in your ```client``` then, 
modify the path in ```run.py``` then click on ```run.bat```

### Credit:
[moondream](https://github.com/vikhyat/moondream)



#### MoonDream Webcam
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuralfalcon/moondream-realtime/blob/main/Moondream_Webcam.ipynb) <br>
