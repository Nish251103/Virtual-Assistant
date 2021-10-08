import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googletrans import Translator
from difflib import SequenceMatcher
import re
import joke_file
import weather_feature
import pyjokes


myname = "Nishchal"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Morning!")
    elif hour >= 12 and hour < 18:
        speak("Afternoon!")
    else:
        speak("Evening!")
    speak("Virtual Assistant N point O online here. ready to combat sir!!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("accessing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def activationCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Kindly say the pass code")
        speak("Kindly say the pass code")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("activating...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        # print(e)
        print("Activation failed please try again...")
        speak("Activation failed please try again...")
        return "None"
    return query


def weather_command():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is the name of the city of which you want to know the weather of : ")
        audio = recogniser.listen(source)
        city_name = ""
        try:
            city_name = recogniser.recognize_google(audio)
            print(city_name)
        except Exception:
            print("Sorry didn't get that, could you please repeat?")
        return city_name


def open_file(user_input):
    os.startfile(user_input)


def removespaces(str1):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', str1)


query1 = activationCommand().lower()
query2 = removespaces(query1)
if query2 == '2511':
    speak("access granted!!")
    if __name__ == "__main__":
        wishMe()
    while True:
        query = takeCommand().lower()
        if 'what can you do for me' in query or similar(query, 'what can you do for me') > 0.7:
            a = speak("try anything sir")
            speak('I can hackdown google for you sir')
            speak('I can get into any system')
            speak('I can track satellites')
            speak('what should I do')

        if "hi" == query or "hello" == query or "good morning" == query or "good evening" == query or "good afternoon" == query:
            speak("Hello, what can I do for you?")
            print("Hello, what can I do for you?")

        elif "how are you" == query:
            speak("I am fine, thank you for asking, how are you?")

        elif "i am fine" == query:
            speak("Good to know")

        if "wikipedia" in query or similar(query, 'search wikipedia') > 0.9:
            speak("what do you want to search")
            query = takeCommand()
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences=2)
            print("result of :", query)
            try:
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("no results found")
                print("no result found")

        elif 'multiply' in query or similar(query, 'multiplication') > 0.7:
            try:
                speak("please tell your first number")
                w122 = int(takeCommand())
                speak("please tell your second number")
                w1 = int(takeCommand())
                result = w1*w122
                print("answer:", result)
                speak('your answer is')
                speak(result)
            except ValueError:
                speak(
                    'sorry could not hear you. please repeat. what was your first number ')
                w122 = int(takeCommand())
                speak("and your second number is")
                w1 = int(takeCommand())
                result = w1*w122
                print("answer:", result)
                speak('your answer is')
                speak(result)

        elif 'google' in query:
            speak("what do you want me to search on google")
            w = takeCommand()
            a = webbrowser.open("https://www.google.com/search?q="+w)
            speak("there you go")

        elif 'youtube' in query:
            speak("what on youtube are you looking for")
            w = takeCommand()
            webbrowser.open("https://www.youtube.com/search?q="+w)
            speak("heres what I found"+w)

        elif 'translate' in query:
            speak("what do you wanna speach")
            w = takeCommand()
            translator = Translator()
            translated_sentence = translator.translate(w, src='en', dest='eo')
            speak(translated_sentence)

        elif 'music' in query:
            # speak('which music buddy')
            # query=takeCommand()
            speak('sure sir')
            webbrowser.open('https://open.spotify.com/')

        elif 'time' in query or similar(query, "the time") > 0.9:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "what is the date" in query:
            date = datetime.datetime.now().strftime("%A,%d %B, %Y")
            speak("The date today is " + date)

        elif "what is the day" in query:
            day = datetime.datetime.now().strftime("%A")
            speak(f"The day today is {day} ")

        elif 'email' in query or similar(query, 'send email') > 0.9:
            speak('To type the mail say m')
            speak('or to speak say s')
            query = takeCommand()
            if query == 's' or query == 'S':
                speak("whom do you want to send email please specify username only")
                str1 = takeCommand()
                to = removespaces(str1)
                to = to+'@gmail.com'
                print('to', to, '\n', 'from', 'your system mail account')
                speak("What should be in the mail?")
                content1 = takeCommand()
            elif query == 'm' or query == 'M':
                to = input('type username')
                to = to+'@gmail.com'
                print('to', to, '\n', 'from', 'your system mail account')
                speak("What should be in the mail?")
                content1 = input('enter text')

            speak("are you sure you want to sent this")
            conf = takeCommand()
            if conf in 'yes':
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login('youremail@gmail.com', 'passward')
                    server.sendmail('youremail@gmail.com', to, content1)
                    server.close()
                    speak("Email has been sent!")
                except Exception as e:
                    speak("Sorry Nishchal. I am not able to send this email")
            else:
                print("okay totally your wish sir")
                speak("okay totally your wish sir")

        elif "weather" in query:
            location = weather_command()
            weather_feature.weather_forecast(location)

        elif "open" in query:
            command = query.replace("open", "")

            try:
                application = command + ".exe"
                open_file(application)
                speak("opened")

            except Exception:
                engine.say(
                    f"Couldn't find {application}, please enter the path of the application: ")
                engine.runAndWait()
                path = input(
                    f"Couldn't find {application}, please enter the path of the application: ")

                if "\\" in path:
                    path = path.replace("\\", "/")
                try:
                    open_file(path)
                    speak("opened")
                except Exception:
                    print("Sorry, couldn't oppen file")

        elif "joke" in query:
            try:
                joke = joke_file.joke_choice()
                speak(joke)
                print(joke)
            except Exception:
                speak("What does the word Algorithm mean? Algorithm is a word used by programmers when they do not want to explain what they did ")

        if 'bye' in query or 'dismiss' in query or 'deactivate' in query:
            speak("Deactivation in enabled")
            engine.runAndWait()
            engine.runAndWait()
            engine.runAndWait()
            speak("Deactivating in process")
            for i in range(100):
                print('Processing...\n')
            engine.runAndWait()
            speak("Deactivation successful")
            print('DeAcTiVaTeD')
            break
            exit()
        elif 'copy data' in query:
            speak("hacker inside the system")
            speak("securing the files")
            speak("forced shutdown")
            for i in range(100):
                print('system saved\n')
            break
