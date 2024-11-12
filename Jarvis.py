import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import ctypes
import subprocess
import pyautogui
import os
import smtplib 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import googlesearch





master = 'Aths'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
print(voices[1].id)
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12: 
            speak(" Good Morning !")
        elif hour>=12 and hour<18: 
            speak(" Good Afternoon !")
        else:
            speak(" Good Evening !")

        speak("I am Jarvis . Please tell me How may I help you ")

        
def takeCommand():
     #it takes microphone input for the users and returns string outputs
    #if 'hey Jarvis'in query:
        r = sr.Recognizer()
        with sr.Microphone() as source:   
            speak("Listning...")
            r.pause_threshold = 1    
            audio = r.listen(source)

        try:

            query = r.recognize_google(audio, language='en-in')
            if query:
                print("Recognizing...")
                speak("wait.. Working on it")
                print("User said: ",query)

        except Exception as e:
            #print(e)
            speak("Say That Again please...")    
            return "None"
        return query

def sendEMail(to, context):
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login('botdragon3649@gmail.com', '9975585895')
    server.sendmail('botdragon3649@gmail.com ',to,context)
    server.close()

def call_jarvis():   #    if __name__=="__main__":

    wishMe()
    query = takeCommand().lower()
    flag = "no"
    while True: 
        if flag == 'yes':
            break   #    while query == 'hey Jarvis':
        if 'wikipedia' in query:
            speak(' Serching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who created you'in query or 'who made you'in query or 'who had developted you'in query:
            speak("i am first elif condition did you get it?")

        elif 'who trained you 'in query:
            speak("I tranied myself but my master help me a lot")

        elif 'hey siri'in query:
            speak("Siri is smarter but I dont like here ")

        elif 'alexa'in query:
            speak("Who is that ")

        elif 'are you single'in query: 
            speak("yes I am happy to be single but if you get a female AI then suggest me ")

        elif 'do you have GirlFriend'in query:
            speak("NO I am Sigle from birth")

        elif 'how much language you know'in query:
            speak("only 3 English, Hindi and Marathi")

        elif' jarvis congratulations'in query:
            speak("Thanks !!")

        elif 'fuck you'in query or'mother fucker'in query or'bc'in query or'mc' in query:
            speak(" You Dont ever try to talk me like this other whise I will leak your private data")   
            
        

        elif 'i hate you'in query:
            speak("Then go to siri or google or any other Ai, I dont care ")

        elif 'who is your Character' in query:
            speak(" Evil")

        elif 'what do u mean by 'in query:
            speak(" That is That")

        elif  ' youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif ' google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif ' instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif ' whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("whatsapp.com")

        elif 'what is the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")

        elif 'show  my college photos' in query:
            speak("wait.. collage photos are loading..")
            clgphotoSrc="C:\\Users\\Atharva\\Pictures\\aissms"
            os.startfile(clgphotoSrc)
        elif 'show my docs' in query:
            speak("wait.. your documents are loading..")
            docphotoSrc="C:\\Users\\Atharva\\Pictures\\Aths Doc"
            os.startfile(docphotoSrc)

        elif 'PPL question bank' in query:
            speak("wait.. PPL question bank is loading..")
            codepth="C:\\Users\\Atharva\\Downloads\\Question_Bank_Unit _3_and_4.docx"

        elif ' PPL notes' in query:
            speak("wait.. PPL notes are loading..")
            codepth="C:\\Users\\Atharva\\Downloads\\Types and Difference.pptx" 
            codepth="C:\\Users\\Atharva\\Downloads\\Object oriented programming.pptx"
            codepth="C:\\Users\\Atharva\\Downloads\\Exception Hendling.pptx"

        elif ' vs code' in query:
            speak(" opeing visual studio code")
            codepth="C:\\Users\\Atharva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepth)

        elif ' mail' in query:
            speak("opening mail")
            webbrowser.open("www.gmail.com")
            
        elif 'send mail to' in query:
            try:
                speak("what should I say")
                context = takeCommand()
                speak("to whom I should send this mail")
                to = takeCommand()
                sendEMail(to, context)
                speak("Email Has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry Bhai but work is not done !!")

        elif (' search for') in query:
            speak(' Serching in Google...')
            query = query.replace("Search for", "")
            r = googlesearch.SearchResult(query, sentences=2)
            speak("According to Google Search")
            print(r)
            speak(r)

        elif 'turn on Wi-Fi'in query:
            speak("ok i have turned your wifi on")
            subprocess.run('netsh interface set interface "Wi-Fi" admin=enable', shell=True)

        elif 'turn off Wi-Fi'in query:
            speak("ok i have turned your wifi off")
            subprocess.run('netsh interface set interface "Wi-Fi" admin=disable', shell=True)

        elif 'turn on bluetooth'in query:
            speak("ok i have turned your bluetooth on")
            subprocess.run('bthprops.cpl', shell=True)

        elif 'turn off bluetooth'in query:
            speak("ok i have turnned your bluetooth off")
            subprocess.run('bthprops.cpl', shell=True)

        elif 'turn on batter saver mood'in query:
            speak("ok i have put your computer on battery saver mood")
            ctypes.windll.powercpl.SetSuspendState(0,1,0)

        elif 'turn off batter saver mood'in query:
            speak("ok i have removed your computer from battery saver mood")
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

        elif 'open search panel'in query:
            speak("opening search panel")
            pyautogui.hotkey('win', 's')

        elif 'open basic setting'in query:
            speak("opening basic setting")
            pyautogui.hotkey('win', 'a')

        elif 'open clipboard'in query:
            speak("opening clipboard")
            pyautogui.hotkey('win', 'v')

        elif 'go to desktop'in query:
            speak("going to desktop")
            pyautogui.hotkey('win', 'd')  

        elif 'open graphical setting'in query:
            speak("opening graphical setting")
            pyautogui.hotkey('win', 'g')

        elif 'open notification'in query:
            speak("opening notification")
            pyautogui.hotkey('win', 'n')

        elif 'open file manager'in query:
            speak("opening basic setting")
            pyautogui.hotkey('win', 'e')

        elif 'open setting'in query:
            speak("opening basic setting")
            pyautogui.hotkey('win', 'u')

        #elif 'play some music'in query:
        #   speak("opening sportify")
        #  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='https://open.spotify.com/user/31owdwussyhdh3bb2st36deqyn5i?si=c8d8031a46d94755',redirect_uri='http://localhost:8000/callback',scope='user-modify-playback-state'))
            
        elif 'go to sleep'in query:
            speak("Thanks sir I need rest")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
        elif 'quit 'in query:
            speak("shutting down system")
            os.system("shutdown /s /t 0")

        flag = input('do wo want another output? "answer yes or no" ')
    else:
        if flag == 'no' :
            print("thank you for using Jarvis")
            speak('thank you for using Jarvis')
            return None
        call_jarvis()

call_jarvis()


