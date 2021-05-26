# Resources
#     https://realpython.com/python-speech-recognition/
#     https://www.geeksforgeeks.org/convert-mp3-to-wav-using-python/
#     https://pythonbasics.org/convert-mp3-to-wav/
#     https://towardsdatascience.com/speech-recognition-in-python-the-complete-beginners-guide-de1dd7f00726

import speech_recognition as sr
from pydub import AudioSegment


def mp32wav(aud_file):
    sound = AudioSegment.from_mp3(aud_file)
    renamed = aud_file[:-4] + 'conv.wav'
    sound.export(renamed, format="wav")
    return renamed


if __name__ == '__main__':
    r = sr.Recognizer()
    r.energy_threshold = 300

    file = mp32wav("text.mp3")
    aud = sr.AudioFile(file)
    # aud = sr.AudioFile("audio_files_harvard.wav")
    with aud as source:
        aud = r.record(source)
        print(r.recognize_google(aud, language='en-in'))
