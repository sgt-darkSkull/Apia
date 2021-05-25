# Resources
#     https://towardsdatascience.com/easy-text-to-speech-with-python-bfb34250036e
#     https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
#     https://gtts.readthedocs.io/en/latest/module.html
#     https://www.systutorials.com/docs/linux/man/1-cvlc/
#     https://pythonbasics.org/python-play-sound/#:~:text=pydub,use%20PyAudio%20and%20ffmpeg%20underneath.

from gtts import gTTS
from playsound import playsound

if __name__ == '__main__':
    text = """Hello, I'm Apia.\
    How can I help You.
    """

    language = 'en'
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("text.mp3")
    playsound('text.mp3')
