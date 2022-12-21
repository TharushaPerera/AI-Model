#Libraries
import pyttsx3
import speech_recognition as sr   

engine = pyttsx3.init('sapi5')
voice=engine.getProperty('voice')
engine.setProperty('voice',voice[1].id)


#Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__=="__main__":
    speak('Hello I am your personal assistant')


def takeVoiceCommand():
    r=sr.Recognizer()

