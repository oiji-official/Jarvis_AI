import pyttsx3
import datetime
import os
import sys
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
# engine = pyttsx3.init('sapi5') gives the following error ->
# chose dummy instead
# reference link -> https://www.edureka.co/community/87959/i-am-making-a-ai-in-python-but-there-is-a-error
# error goes away but no voice comes out
# reverted back to sapi5
# took care of the error by this -> https://www.youtube.com/watch?v=6RyCt2xWBcM
# my site address is -> C:\Users\xyzno\AppData\Roaming\Python\Python39\site-packages

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("This is the Desktop Assistance prototye. Please tell how can I be of assistance to you.") 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('oiji2504@gmail.com', os.environ.get("Password"))
    server.sendmail('oiji2504@gmail.com', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 

    except Exception:   
        print("Pardon Sire?...")    
        return "None" 
    return query

if __name__ == "__main__":
    wishMe()
    i=1
    while i:
        query = takeCommand().lower() 

        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia, ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open entertainment news' in query:
            webbrowser.open("koreaboo.com")

        elif 'open code' in query:
            codePath = "C:\\Users\\xyzno\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            codePath2 = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
            os.startfile(codePath2)
        
        elif 'email to john' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sreyamajumder01@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                i=0
            except Exception as e:
                print(e)
                speak("I apologise. I was unable to send the mail.")


        
        
        
