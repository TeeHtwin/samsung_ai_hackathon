import pyttsx3
import gtts
import speech_recognition as sr
import openai
import env

# openai key
openai.api_key = env.OPEN_AI_KEY

# initialize speech engine
engine = pyttsx3.init()


def speak(word):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()


# Initialize Speech Recognizer
rec = sr.Recognizer()
speak('hello Sir, I am listening for your command')
with sr.Microphone() as source:
    audio = rec.listen(source)
    speak('I am computing an answer for your request. i will be done soon')

text = rec.recognize_google(audio)
print(text)

discussion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
#
# answer = discussion.choices[0].message['content']
answer = discussion['choices'][0]['message']['content']

if answer:
    speak(answer)