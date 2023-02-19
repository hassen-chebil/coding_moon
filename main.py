import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from sentence_splitter import SentenceSplitter
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
from corona import corona
from queue import Queue
from time import sleep
import webbrowser
import requests
import datetime
import re
from voice import talk,take_command


def hello():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        talk("Good morning!")
        print("Good morning!")
    elif hour>= 12 and hour<18:
        talk( "Good afternoon!") 
        print( "Good afternoon!")
    else:
        talk( "Good evening!")
        print( "Good evening!")


def run_chatbot():

    hello()
    
    print( "My name is VoiceAid ...")
    print("I can tell you about:")
    print("Time , City Location , Joke , Corona , Music Listening ")
    print( "what do you want?")
    talk( "My name is VoiceAid ...") 
    talk( "I can tell you about:")
    talk( "Time , City Location , Joke , Corona , Music Listening")
    talk( "what do you want?")
    

    
    
    while True:

        command = take_command()
        print(command)

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            talk('Current time is ' + time)

        elif 'joke' in command:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
       
        elif command.lower() in ["corona", "Corona","coronavirus","Coronavirus","tell me about corona", "situation corona", "corona situation", "coronavirus situation", "situation coronavirus", "situation covid", "covid situation", "covid19 situation", "situation covid19", "covid-19 situation", "situation covid-19", "situation sanitaire", "sanitary situantion"]:
            try:
                dates, cases, deaths = corona()
            except:
                print("Country not in our database!")
                talk("Country not in our database!")
                continue

            talk("Here's the cases for the past 3 days:")
            for date, case, death in zip(dates, cases, deaths):
                print(date+": \n"+case+", "+death)
                talk( date+": \n"+case+", "+death)

        elif command.lower() in ["Localisation d'un lieux", "localisation d'un lieux", "localisation d'un lieu","lieux","localisation des lieux","localisation","lieu","city location","location","location","city","City"]:
            talk( 'Choose the city please!')
            loc=take_command()
            url = 'https://google.nl/maps/place/' + loc + '/&amp;'
            webbrowser.open(url)
            talk("Opened location of "+loc+" in google maps, check your browser.")
            sleep(2)

        elif command.lower() in ["music listening", 'I want to listen a music' ,'i want to listen a music','i want to listen music',"je veux écouter une musique","Je veux écouter une musique","écouter une musique","listen to music","Listen to music","listen a music","Listen a music" ,"music","Music","musique","Musique", "écouter de la musique"]:
            talk( 'Choose the music please')
            song = take_command()
            talk( 'Playing ' + song + ', check your browser!')
            pywhatkit.playonyt(song)
            sleep(2)

        if command.lower() in  "google":
            talk('opening google ' + song)
            webbrowser.open("https://www.google.com/")
        
        if "thank you" in command:
            talk("Welcome !")

        elif 'who is'  in command:
            per = command.replace('who is', '')
            info = wikipedia.summary(per, 1)
            print(info)
            talk(info)

        elif 'what is' in command:
            par = command.replace('what is', '')
            info = wikipedia.summary(par, 1)
            print(info)
            talk(info)
   
    
        else:
            talk('Please say the command again.')


while True:
    run_chatbot()