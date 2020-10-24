###SETUP FOR UBUNTU
from subprocess import call

#make python3 default
call(["sudo", "update-alternatives", "--install", "/usr/bin/python", "python", "/usr/bin/python3", "10"])

#install third-party libraries
call(["python", "-m", "pip" ,"install" ,"playsound"])
call(["python" ,"-m" ,"pip" ,"install" ,"gTTS"])
call(["python" ,"-m", "pip", "install", "SpeechRecognition"])
call(["python", "-m", "pip" ,"install" ,"pyalsaaudio"])
call(["python", "-m", "pip" ,"install" ,"newsapi-python"])

#installing kivy
call(["sudo" ,"add-apt-repository", "ppa:kivy-team/kivy"])
call(["sudo" ,"apt-get", "install" ,"python3-kivy"])

#GETTING RID OF KNOWN BUGS
#if you get an OS:error such as: "OSError: libespeak.so.1: cannot open shared object file: No such file or directory"
call(["sudo", "apt-get", "update" ,"&&" ,"sudo", "apt-get", "install", "espeak"])
#to fix pyAudio problems such as "ERROR: Failed building wheel for PyAudio"
call(["sudo" ,"apt", "install" ,"libasound-dev" ,"portaudio19-dev" ,"libportaudiocpp0"])
#to fix "[CRITICAL] [App         ] Unable to get a Window, abort."
call(["sudo" ,"apt-get" ,"install" ,"libsdl2-2.0-0" ,"libsdl2-image-2.0-0" ,"libsdl2-mixer-2.0-0" ,"libsdl2-ttf-2.0-0"])

#checking if libraries are installed
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import alsaaudio
from kivy.app import App
from newsapi import NewsApiClient

print("if you received no error before this text, you are set to go")
