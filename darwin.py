import pyttsx3,datetime,wikipedia,webbrowser,os,smtplib,time,random
import speech_recognition as sr
import pyautogui as pag
delay = lambda x:time.sleep(x)
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:speak('ggooood morning')
    elif hour>=12 and hour < 18:speak('ggooood afternoon')
    else:speak('ggooood evening')
def takecomand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        speak('listening')
        r.pause_threshold = 0.6
        r.energy_threshold = 200
        r.dynamic_energy_ratio = 1.5
        r.phrase_threshold = 0.3
        r.non_speaking_duration = 0.5
        audio = r.listen(source)
        try:
            print("Recognizeing...")
            speak("Recognizeing")
            query = r.recognize_google(audio, language='en-in')
            print(f"you said: {query}\n")
        except Exception as e:
            print("internet problem...")
            return "None"
        return query
wish_me()
speak("i am darwin your assistent.sir please compleat your work")
while 1:
    try:
        query = takecomand().lower()
        if 'wikipedia' in query:
            query.replace('wikipedia','')
            try:
                results = wikipedia.summary(query, sentences=2)
                print(str(results))
                speak('according to wikipedia')
                speak(results)
            except Exception as e:speak(f'cant find {results} in wikipedia')
        elif 'stop' in query:break
        elif 'code' in query:
            pag.hotkey('winleft','r')
            pag.typewrite('cmd\n')
            delay(0.4)
            pag.typewrite("cd doc\t\ncode dar\t\n")
        elif 'youtube' in query:webbrowser.open("youtube.com")
        elif 'google' in query:webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
        elif 'instagram' in query:webbrowser.open("instagram.com")
        elif 'music' in query:
            music_dir = "E:\\songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs))]))
        elif 'time' in query:speak(f"sir the time is {datetime.datetime.now().strftime("%H:%M:%S")}")
        elif 'type' in query:
            query = query.replace('type ', '')
            pag.typewrite(f"{query}")
        elif 'clear' in query:
            pag.hotkey('ctrl','a')
            pag.press('backspace')
        elif 'enter' in query:pag.press('enter')
        elif 'download' in query:
            path = 'C:\\Users\\Raj_Gaurav\\Downloads'
            os.startfile(path)
        elif 'documents' in query:
            path = 'C\\Users\\Raj_Gaurav\\Documents'
            os.startfile(path)
        elif 'c' in query:
            path = 'C:\\'
            os.startfile(path)
        elif 'say' in query:
            speak('to exit say exit')
            query = query.replace('say','')
            speak(query)
            while 1:
                sp = takecomand()
                if 'exit' in sp:break
                speak(sp)
        elif 'list' in query:
            speak('heare are some of my featurs you can use')
            print('wikipedia\nstop\ncode\nyoutube\ngoogle\ninstagram\nmusic\ntime\ntype\nclear\nenter\ndownloads\ndocuments\ndrivers\nspeak\nlist')
    except Exception as e:print("error...")
