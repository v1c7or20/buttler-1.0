from pc_comands import *
from bot_actions import  *
import speech_recognition as sr


def get_voice_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def action(command):
    if command.partition(' ')[0] == "close" or command.partition(' ')[0] == "cerrar":
        kill_process(process_name=command.partition(' ')[2])

