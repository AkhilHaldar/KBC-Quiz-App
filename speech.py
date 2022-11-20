import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak")
    audio = r.listen(source)

    try:
        def call():
            text = r.recognize_google(audio)
            return text
    except:
            print('Sorry not recognisable')
