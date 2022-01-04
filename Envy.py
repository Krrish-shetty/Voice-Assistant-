import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Krrish Dinesh Shetty ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Krrish Dinesh Shetty ")   

    else:
        speak("Good Evening! Krrish Dinesh Shetty ")  

    speak("I am Envy Here. Please tell me how may I assist you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kshetty200319@gmail.com', 'kds2003')
    server.sendmail('kshetty200319@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'how is the weather' in query:
            webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1VDKB_enIN965IN965&oq=weather&aqs=chrome..69i57j35i39j0i67l2j0i67i457j0i402j0i67i433j0i67i131i433j0i433i512j0i512.2056j1j7&sourceid=chrome&ie=UTF-8")

        elif 'open spotify' in query:
            webbrowser.open("https://www.spotify.com/in-en/free/?utm_source=in-en_brand_contextual_text&utm_medium=paidsearch&utm_campaign=alwayson_asia_in_premiumbusiness_core_brand+contextual-desktop+text+exact+in-en+google&ds_rl=1270915&gclid=CjwKCAiAn5uOBhADEiwA_pZwcKmKfB-I4hvy-dIk83905DWJ1SN5LP7b7YDdnlpGKNjOWD4G7pPr7hoC3m8QAvD_BwE&gclsrc=aw.ds")   
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"krrish, the time is {strTime}")


        elif 'email to home' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kshetty2003@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my Boss Krrish. I am not able to send this email")    