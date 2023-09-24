import tkinter
from typing import Text
import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS, tts
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import time
import webbrowser
import ctypes
import winshell
import subprocess
import pyjokes
# client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import requests
import json
import braille
from pytesseract import image_to_string
import wolframalpha
import time
import cv2
import pytesseract
from tkinter import *
from tkinter import filedialog
import sys


#!import the ocr file here and write the braille commands


warnings.filterwarnings("ignore")  # ignores all warnings

engine = pyttsx3.init()  # initializing pyttsx3
voices = engine.getProperty('voices')  # getting the deets of current voice
# engine.setProperty('voice', voices[0].id)  # changing index #changing the voice to male
# changing index #changing the voice to female
engine.setProperty('voice', voices[1].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()  # pass a string and call this func out, it will speak the string


def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <= 12:
        talk("Good morning, how may I help you?")
    elif hour > 12 and hour < 16:
        talk("Good morning, how may I help you?")
    else:
        talk("Good evening, how may i help you?")


print('intializing...')
sys.stdout.flush()
greetings()


def rec_audio():  # works
    recog = sr.Recognizer()  # inistializing the recogniser

    with sr.Microphone() as source:
        print("Listening...")
        sys.stdout.flush()
        audio = recog.listen(source)
# using google speech recognition to recognise the speech

    data = " "
    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
        sys.stdout.flush()

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
        sys.stdout.flush()

    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)
        sys.stdout.flush()
    return data


def response(text):
    print(text)
    sys.stdout.flush()

    tts = gTTS(text=text, lang="en", tld='com')

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "hello"

    text = text.lower()
    # print(text)
    # sys.stdout.flush()

    if action_call in text:
        # print('tiru lub')
        # sys.stdout.flush()
        # print(text.upper())
        # sys.stdout.flush()
        return True

    else:
        # print(":/")
        # sys.stdout.flush()
        # print(text)
        # sys.stdout.flush()
        return False


def openFile():
    root = Tk()
    root.withdraw()
    root.update()
    filepath = filedialog.askopenfilename(initialdir="D:\Projects\Blind Assistant\raw\test_images",
                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    file = open(filepath, 'r')
    #tkinter.Label.config(path = filepath)
    print(filepath)
    sys.stdout.flush()
    # print(file.read())
    # sys.stdout.flush()
    file.close()

    root.destroy()

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(filepath)
    # img=cv2.resize(img,(400,450))
    cv2.imshow("image", img)
    result = pytesseract.image_to_string(img)
    print(result)
    sys.stdout.flush()
    talk(result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def today_date():
    now = datetime.datetime.now()  # month,date,hours,min,secs
    date_now = datetime.datetime.today()  # this will give the present date and time
    week_now = calendar.day_name[date_now.weekday()]  # day of the week
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31th",
    ]

    return f'Today is {week_now}, {months[month_now -1]} the {ordinals[day_now -1]}.'


def greeting(text):
    greet = ["Hello", "Hey", "Hi", "Supp", "Hey there",
             "Greetings", "Howdy", "wassup", "Henlo", "yo"]

    response = ["Hey yourself!", "Hello!", "Hi", "Greetings",
                "hey hey hey!", "yo", "wassup", "Hey", "Hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choices(response)

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki)-1 and list_wiki[i].lower() == "who" and list_wiki[i+1].lower() == "is":
            return list_wiki[i+2] + " " + list_wiki[i+3]


def note(text):  # this needs more work
    date = datetime.datetime.now()
    # using replace method to replace ":" with "-"
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("atharvvyas0202@gmail.com", "SiyaVyas!23")
    server.sendmail("atharvvyas0202@gmail.com", to, content)
    server.close()


def test(text):
    if "test" in text.lower():
        talk('What is your answer?')
        answer = rec_audio()
        print("recording answer")
        sys.stdout.flush()
        if "yes" in answer.lower():
            talk("yes it works")
        elif "no" in answer.lower():
            talk("no it works")
    else:
        talk("test doesn't work")

# def wiki(text):
#     if "who is" in text:
#         person = wiki_person(text)
#         wiki = wikipedia.summary(
#             person, sentences=2, auto_suggest=False)
#         speak = speak + " " + wiki


#braille.textToBraille("Hello world")----WORKS
#braille.brailleToSpeechArray(['⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙'])
#braille.imageToText(r"D:\Projects\Blind Assistant\test\hello_world.jpeg")
while True:
    try:
        text = rec_audio()
        speak = ""
        #talk("I'm ready")

        if call(text):

            speak = speak + greeting(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "test" in text:
                test(text)

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + \
                    str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in text or "Wikipedia" in text:
                 if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(
                        person, sentences=2, auto_suggest=False)
                    speak = speak + " " + wiki

            elif "who are you" in text or "define yourself" in text:
                speak = speak + """Hello, I am , an Assistant. I am here to make your life easier. You can command me to perform various tasks such as solving mathematical questions or opening applications etcetera."""

            elif "your name" in text:
                speak = speak + "My name is ."

            elif "your creator" in text or "who is your creator" in text:
                speak = speak + "I'm created by Atharv Vyas"

            elif "who am I" in text:
                speak = speak + "You must probably be a human."
            elif "why do you exist" in text or "why did you come" in text:
                speak = speak + "It is a secret."

            elif "how are you" in text:
                speak = speak + "I am fine, Thank you!"
                speak = speak + "\nHow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that you are fine"

            elif "convert" in text or "translate" in text.lower():
                if "text to braille" in text.lower():
                    talk("What would you like me to convert? Please type it below.")
                    ind = input()
                    braille.textToBraille(ind)

                elif "image to Braille" in text.lower():
                    talk("works lol")
                    # ? img = Image.open("name")
                    # ? str = pytesseract.image_to_string(img)
                    # ? braille.textToBraille(str)
                elif "image to speech" in text.lower():
                    talk("image to speech")
                    # ? img = Image.open("name")
                    # ? str = pytesseract.image_to_string(img)
                    # ? speak = speak + str(str)

            elif "text to speech" in text.lower():
                openFile()

            elif "open" in text.lower():  # !Try to make it without using PATH
                # **os.system("program_name") # To open any program by their name recognized by windows

                """Change this code, make it shorter and customisable."""

                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"chrome.exe"
                    )

                elif "word" in text.lower():
                    speak = speak + "Opening Microsoft Word"
                    os.startfile(
                        r"WINWORD.EXE"
                    )

                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft Excel"
                    os.startfile(
                        r"EXCEL.EXE"
                    )

                elif "vs code" in text.lower():
                    speak = speak + "Opening Visual Studio Code"
                    os.startfile(
                        r"C:\Windows.old\Users\athar\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    )

                elif "brave" in text.lower():
                    speak = speak + "Opening Brave"
                    os.startfile(
                        r"brave.exe"
                    )

                elif "spotify" in text.lower():
                    speak = speak + "Opening Spotify"
                    os.startfile(
                        r"C:\Users\athar\AppData\Roaming\Spotify\Spotify.exe"
                    )

                elif "Discord" in text.lower():
                    speak = speak + "Opening Discord"
                    os.startfile(
                        r"C:\Users\athar\AppData\Local\Discord\Update.exe --processStart Discord.exe"
                    )
                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = speak + "Opening Google\n"
                    webbrowser.open("https://google.com/")

                elif "stack overflow" in text.lower():
                    speak = speak + "Opening StackOverFlow"
                    webbrowser.open("https://stackoverflow.com/")

                else:
                    speak = speak + "Application not available."

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )
                speak = speak + "Opening " + str(search) + " on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search)
                )
                speak = speak + "Searching " + str(search) + " on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search)
                )
                speak = speak + "Searching " + str(search) + " on google"

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Recycle Bin Emptied"

            elif "note" in text or "remember this" in text:  # this needs more work
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that."

            elif "joke" in text:
                speak = speak + pyjokes.get_joke()

            elif "where is" in text:  # MAPS needs nore work
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)

            # elif "email to computer" in text or "gmail to computer" in text or "mail to computer" in text:
            #     try:
            #         talk("What should I say?")
            #         content = rec_audio()
            #         to = rec_audio()
            #         send_email(to, content)
            #         speak = speak + "Email has been sent !"
            #     except Exception as e:
            #         print(e)
            #         sys.stdout.flush()
            #         talk("I am not able to send this email")

            elif "mail" in text or "email" in text or "gmail" in text or "email to computer" in text or "gmail to computer" in text or "mail to computer" in text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    talk("Whom should I send it to?. Please type the email I.D below.")
                    to = input("Enter To Address: ")
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                except Exception as e:
                    print(e)
                    sys.stdout.flush()
                    speak = speak + "I am not able to send this email"

            elif "calculate" in text:
                app_id = "5GK6VJ-26H5K4262V"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            elif "what is" in text or "who is " in text or "why is" in text:
                app_id = "5GK6VJ-26H5K4262V"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("is")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            elif "why" in text:
                app_id = "5GK6VJ-26H5K4262V"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("why")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            # elif "don't listen" in text or "do not listen" in text or "stop listening" in text: #!needs to be created into a function and re-code the whole thing
            #     talk("for how much time do you want me to sleep?")
            #     a = int(rec_audio())
            #     if "hours" in a:
            #         time.sleep(a*60*60)
            #         speak = speak + str(a) + " hours completed. Now you can ask me anything!"
            #     elif "minutes" in a:
            #         time.sleep(a*60)
            #         speak = speak + str(a) + " minutes completed. Now you can ask me anything!"

            #     else:
            #         time.sleep(a)
            #         speak = speak + str(a) + " seconds completed. Now you can ask me anything!"

            elif "exit" in text or "quit" in text:
                exit_responses = ["Bye!", "See you!", "Goodbye!", "Bye Bye!",
                                  "You can always press the hotkey to call me again! Bubye!"]
                talk(random.choices(exit_responses))
                break

                """OPTIONAL"""
                # elif "change background" in text or "change wallpaper" in text:
                #     img = r"Location of directory"
                #     list_img = os.listdir(img)
                #     imgChoice = random.choice(list_img)
                #     randomImg = os.path.join(img, imgChoice)
                #     ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                #     speak = speak + "Background changed successfully"

                # elif "play music" in text or "play song" in text:
                #     talk("Here you go with music")
                #     music_dir = r"Location of directory"
                #     songs = os.listdir(music_dir)
                #     d = random.choice(songs)
                #     random = os.path.join(music_dir, d)
                #     playsound.playsound(random)
                """/OPTIONAL"""
        # else:

        #     #rec_audio()
        #     talk("I don't know that!")

        response(speak)

    except:
        if "hello" not in text:
            continue
        else:
            # rec_audio()
            talk("I don't know that!")
