import speech_recognition as sr #library for performing speech recognition
import pyttsx3 #text to speech
import pywhatkit #For YouTube automation
import datetime #To get the time
import pyjokes #To get the jokes

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id) #Sets the voice to a female voice

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()


def user_commands(): #Funtion to get the user commands
    try:
        with sr.Microphone() as source: #input from default microphone
            print("I am your home assistant, how can i help you? Say Alexa, followed by what you wish for...") #Welcomes the user
            voice = listener.listen(source) #Listens out for input from the microphone
            command = listener.recognize_google(voice) #recognize the voice
            command = command.lower() #Turns command into lowercase
            if 'alexa' in command:
                command = command.replace('alexa', '') #Only listens when the user says Alexa
                print(command)
    except:
        pass
    return command

def run_alexa(): #Function called run_alexa
    command = user_commands()
    if 'play' in command: #if the user says play in the command
        song = command.replace('play', '') #so alexa doesn't say "playing play ..."
        engine_talk('playing' +song) #If play is in the user command then the system will say what it is doing
        pywhatkit.playonyt(song) #pywhatkit to open the video on YouTube
    elif 'time' in command: #if the user says time in the command
        time = datetime.datetime.now().strftime('%I:%M %p') #I is hour in 24hr format, M gets the minutes too and P gets Am & Pm
        engine_talk('The time is' +time) #Will say what the time is
    elif 'joke' in command: #if the user says joke in the command
        engine_talk(pyjokes.get_joke()) #Will get a joke and will say it
    else:
        engine_talk('I could not understand you, could you please repeat that') #If none of these words are said from these commands then this error message will be said

run_alexa() #program runs