# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Speak Anything :")
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio,language='my')
#         print("You said : {}".format(text))
#     except:
#         print("Sorry could not recognize what you said")

import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='my')
                print("You said : {}".format(text))
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        print("Exiting the loop")
        break

