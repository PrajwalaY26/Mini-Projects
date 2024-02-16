import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print('Welcome to RoboSpeaker 1.1. Created by Prajwala')
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            break
        speak_text(x)
