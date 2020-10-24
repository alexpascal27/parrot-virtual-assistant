"""
For Headers:
use text to ASCII (standard)

To Do:

NOW

#reminders = make an alarm as well as working with the reminders text file
#news = read top headlines
#math = conversion

LATER

#Ask for user name and allow for user to name the VA
#Implement ways to stop commands such as negatives ("don't") or buzz words ("cancel")

"""
###THIRD PARTY
#audio output
from playsound import playsound
#text to speech
from gtts import gTTS
#speech recognition
import speech_recognition as sr
#os volume control
import alsaaudio
###
from time import ctime
import os
import re
import webbrowser
import requests
import json
import math
import subprocess
from subprocess import call
import random

#Create an array of all the possible functions
function_list = ["I can remind you to do something", "I can check the weather", "I can tell you a joke", "I can open an app", "I can search the internet", "I can open a website", "I can tell you the time", "I can converse"]
swear_words_list = ["anal","anus","arse","ass","ballsack","balls","bastard","b****","biatch","bloody","blowjob","bollock","bollok","boner","boob","bugger","bum","butt","buttplug","clitoris","cock","coon","crap","c***","dick","dildo","dyke","fag","feck","fellate","fellatio","felching","f***","fudgepacker","flange","cage","homo","jerk","jizz","knobend","labia","muff","nigger","nigga","penis","piss","poop","prick","pube","pussy","scrotum","sex","s***","slut","smegma","spunk","tit","tosser","twat","vagina","wank","whore","wtf"]
#     _             _ _
#    / \  _   _  __| (_) ___
#   / _ \| | | |/ _` | |/ _ \
#  / ___ \ |_| | (_| | | (_) |
# /_/   \_\__,_|\__,_|_|\___/

def speak(audio):
    #prints audio in terminal for user to at least read if there are problems with sounds output
    print(audio)
    #defines output engine
    tts = gTTS(text=audio, lang='en')
    #function to speak
    tts.save("media/audio.mp3")
    playsound("media/audio.mp3")

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        #how long the pause is
        #r.pause_threshold = 1
        #background noise fix
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

# Speech recognition using Google Speech Recognition
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command could not be heard.')
        command = myCommand();
    #if can't access google services
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return command

#   ____                                          _
#  / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |___
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
# | |__| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
#  \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/

#if statements for executing commands

def assistant(command):
    """
  ___           _         _
 | _ \___ _ __ (_)_ _  __| |___ _ _ ___
 |   / -_) '  \| | ' \/ _` / -_) '_(_-<
 |_|_\___|_|_|_|_|_||_\__,_\___|_| /__/

    """
    #adds a reminder
    if "remind me to" in command:
        reg_ex = re.search('remind me to (.*)', command)
        #if user mentioned what they want to be reminded of
        if reg_ex:
            reminder = reg_ex.group(1)
            #checks whether user what reminder they want
            speak("Shall I remind you to: "+reminder)
            answer = input("Type Y to add the reminder above to the reminder list or N to manually enter your reminder. \n")
            #if voiced reminder is wrong
            if answer == "N":
                #take out reminder from command in case it contains function buzzwords, before you change it
                command = command.replace(("remind me to " +reminder),"")
                #user enters reminder automatically
                speak("Please type your reminder")
                reminder = input()
                edit_todo = open("/media/reminders.txt","a")
                edit_todo.write(reminder + "\n")
                edit_todo.close()
                speak(reminder + " - is now in your list of reminders")
            #if voiced reminder is correct
            elif answer == "Y":
                speak("You have acknowledged the reminder")
                edit_todo = open("/media/reminders.txt","a")
                edit_todo.write(reminder + "\n")
                edit_todo.close()
                speak(reminder + " - is now in your list of reminders")
                #take out reminder from command in case it contains function buzzwords
                command = command.replace(("remind me to " +reminder),"")
            else:
                speak("You have not entered a valid answer!")
                #take out reminder from command in case it contains function buzzwords
                command = command.replace(("remind me to " +reminder),"")
                pass

            print(command)
        else:
            pass
    #recalls reminders
    if "list reminders" in command:
        read_todo = open("/media/reminders.txt","r")
        speak("Your reminders are:" + read_todo.read())
        print(read_todo.read())
        read_todo.close()
    #empties reminder list
    if "clear reminders" in command:
        clear_todo = open("/media/reminders.txt","w")
        clear_todo.write("")
        speak("Your reminders list is now empty")

        """
   ___                             _   _
  / __|___ _ ___ _____ _ _ _____ _| |_(_)___ _ _
 | (__/ _ \ ' \ V / -_) '_(_-< _` |  _| / _ \ ' \
  \___\___/_||_\_/\___|_| /__|__,_|\__|_\___/_||_|

        """
    #Common Greetings
    elif "hi" in command or 'hey' in command or 'hello' in command or 'greetings' in command:
        speak('Hey, Alex')
    #common conversational phrases
    elif "how are you" in command or 'what\'s up' in command:
        speak("Feeling great!")
    #humour
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
        else:
            speak('oops!I ran out of jokes')
    elif any(word in command.split() for word in swear_words_list):
            print("You swore.....naughty")
            playsound('media/nani.mp3')
            """
   ___  ___   ___             _   _
  / _ \/ __| | __|  _ _ _  __| |_(_)___ _ _  ___
 | (_) \__ \ | _| || | ' \/ _|  _| / _ \ ' \(_-<
  \___/|___/ |_| \_,_|_||_\__|\__|_\___/_||_/__/

            """
    #tells the user the time on their machine
    if "what time is it" in command:
        speak(ctime())
    #open an external program
    if "open the app" in command:
        reg_ex = re.search('open the app (.*)', command)
        if reg_ex:
            program = reg_ex.group(1)
            subprocess.Popen([program], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            pass

    #EXITING VA
    if "exit" == command or "stop listening" == command:
        speak("If you are brave enough to say goodbye, life will reward you with a new hello.")
        quit()

    #if volume control
    if "mute" in command or "max volume" in command or "turn it up to max" in command or "volume up to max" in command or "set volume" in command or "turn it up" in command or "volume up" in command or "turn it down" in command or "volume down" in command:
        #first get the master volume for the device
        m = alsaaudio.Mixer()
        vol = m.getvolume()
        #the default change if the user doesn't input a specific change
        def_change = 10
        #determine if the user wants to turn up or turn down the volume or set a specific volume
        vol_set = re.search("set volume to (.*)", command)
        vol_increase = re.search("up by (.*)", command)
        vol_decrease = re.search("down by (.*)", command)
        #if the user wants to set the volume to a specific value
        if vol_set:
            volume = int(vol_set.group(1))
        #if the user wants to increase the volume by a specific amount
        if vol_increase:
            vol_up = vol_increase[1]
            volume = vol[0] + int(vol_up)
        #if the user wants to decrease the volume by a specific amount
        if vol_decrease:
            vol_down = vol_decrease[1]
            volume = vol[0] - int(vol_down)
        #no specific change but wants to increase volume
        if not vol_increase and not vol_decrease and "up" in command:
            volume = vol[0] + def_change
        #no specific change but wants to decrease volume
        if not vol_increase and not vol_decrease and "down" in command:
            volume = vol[0] - def_change
        #mute
        if "mute" in command:
            volume = 0
        #set to max volume
        if "max volume" in command or "turn it up to max" in command or "volume up to max" in command:
            volume = 100
        else:
            pass
        #execute the change in volume
        proc = call(["amixer", "-D", "pulse", "sset", "Master", str(volume) + "%"])


        """
  ___     _                    _
 |_ _|_ _| |_ ___ _ _ _ _  ___| |_
  | || ' \  _/ -_) '_| ' \/ -_)  _|
 |___|_||_\__\___|_| |_||_\___|\__|

        """
    #looks up places on google maps
    if "where is" in command:
        command = command.split(" ")
        location = command[2]
        speak("Hold on, I will show you where " + location + " is.")
        webbrowser.open('https://www.google.nl/maps/place/' + location + '/&amp;')
    #searches Google
    if "search for" in command:
        reg_ex = re.search('search for (.*)', command)
        url = 'https://www.google.com/?#q='
        if reg_ex:
            search = reg_ex.group(1)
            url = url + search
            webbrowser.open(url)
            speak('Searching for: ' + search)
    #Opns reddit
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        speak('Opening Reddit!')
    #opens any  website
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak('Opening ' + url)
        else:
            pass

    #WEATHER
    elif "weather like" in command:
        try:
            #checks whether user is looking for a specific location
            reg_ex = re.search('weather like in (.+)', command)
            #finds ip adress
            url = 'https://extreme-ip-lookup.com/json/'
            r = requests.get(url)
            data = json.loads(r.content.decode())
            #if user mentions a location
            if reg_ex:
                location = reg_ex.group(1)
            else:
                #sets location as the city of the ip adress
                location = data['city']
            #weather api
            api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
            weather_url = api_address + location
            json_data = requests.get(weather_url).json()
            #finds description of forecast
            weather = json_data['weather'][0]['description']
            #the temp from website is in K
            kelvin = json_data['main']['temp']
            #convert temp from K to C
            celsius = kelvin - 273.15
            #if temp below 0
            if celsius < 0:
                celsius = math.sqrt(celsius*celsius)
                celsius = "minus " + str(round(celsius,1))
            else:
                celsius = str(round(celsius, 1))
            #output
            speak(location + " is expecting " + weather + ' with ' + celsius + " degrees celsius")

        #if location cannot be found
        except KeyError as e:
            speak("The location you are looking for cannot be found")

            """
  ___              _ _   _     _
 |_ _|_ _  __ _ __(_) |_(_)_ _| |_ _  _
  | || ' \/ _` / _| |  _| \ V /  _| || |
 |___|_||_\__,_\__|_|\__|_|\_/ \__|\_, |
                                   |__/
            """
    #if asks for features or says nothing
    if "" == command or"help" in command or "features" in command:
        speak("Here are some things I can do: ")
        for i in range(3):
            #Randomise 3 functions from the array listen
            function = random.choice(function_list)
            #output ("Here are some things I can do:" + function + " or " + function + "or" + function )
            speak(function)
            #remove what function has been said
            function_list.remove(function)


"""
    #by default the engine does not look for further commands
    #if the user says ok parrot then the engine looks for further commands
    if "parrot" in command:
        reg_ex = re.search("parrot (.*)", command)
        #if user says something after parrot
        if reg_ex:
            #get what the user says before and after "ok parrot" and stores the strings to a list
            command = command.split("parrot ",2)
            #set command to what the user says after "ok parrot"
            command = command[1]
"""
