import speech_recognition as SR
import pyttsx3
import pywhatkit
import datetime as timenow
import pyjokes
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.linear_model import LinearRegression

listner = SR.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    # try:
    with SR.Microphone() as source:
        print("listening!!!")
        voice = listner.listen(source)
        command = listner.recognize_google(voice)
        command = command.lower()
                   
    # except:
        # pass 

    return command


while(True):
    def runJarvis():
        command = takeCommand()
        print(command)
        if 'jarvis' in command:
                command = command.replace('jarvis','')
                talk("hi what can i do for you")
        elif 'play' in command:
            command = command.replace('play','')
            talk("playing "+ command)
            pywhatkit.playonyt(command)
        elif 'time' in command:
            time = timenow.datetime.now().strftime('%I:%M %p')
            print("Current time is:")
            talk(time)
            print(time)
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            print(joke)
        elif 'how are you' in command:
            talk('I am fine How are you') 
        elif 'fine' in command:
            talk('thats good')    

        elif 'read' in command:
            talk('name of pdf you want me to read?')
            command = takeCommand()
            if " " in command:
                command = command.replace(' ','')
            print(command)
            command = command+".pdf"
            print(command)
            reader = PdfReader(command,'rb')
            number_of_pages = len(reader.pages)
            talk('Give number of page which you want me to read for you')
            page = reader.pages[int(input("\nEnter page Number:"))-1]
            print(number_of_pages)
            text = page.extract_text()
            talk(text)

        elif 'predict' in command:
            data = pd.read_excel('Book1.csv')
            # print(data.head())
            model = LinearRegression()
            model.fit(data[['version']],data[['price']])
            talk('For which year you want to predict?')
            value = int(input("Enter model:"))
            talk(model.predict([[value]]))
            print(model.predict([[value]]))

        elif "" in command:
            pass
        else:
            pass

        runJarvis()
    
                   
    runJarvis()        