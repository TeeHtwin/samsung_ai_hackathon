import os
from gtts import gTTS
import speech_recognition as sr
import pygame
# from playsound import playsound
import openai
import env

# OpenAI key
openai.api_key = env.OPEN_AI_KEY

def speak(word):
    # Use gTTS to convert text to speech
    tts = gTTS(text=word, lang='my')
    mp3_filename = "output.mp3"
    # if os.path.exists(mp3_filename):
    #     os.remove(mp3_filename)
    tts.save(mp3_filename)
    print(f"MP3 file saved as {mp3_filename}")

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_filename)
    pygame.mixer.music.play()

    # Wait for the audio to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    print(f"Playing {mp3_filename}")

    pygame.mixer.music.stop()
    pygame.mixer.quit()

# Initialize Speech Recognizer
rec = sr.Recognizer()
speak('မင်္ဂလာပါ၊ ဦးဆောင်မှုများပေးရန် အသင့်ရှိပါတယ်။')
with sr.Microphone() as source:
    audio = rec.listen(source)
    # speak('ကျွန်ုပ် အကြံပြုချက်များ ရေးသားနေပါတယ်။ ခဏစောင့်ပါ။')

# text = rec.recognize_google(audio, language='my')
# print("You said: " + text)

text = rec.recognize_google(audio,language='my')
print(text)

discussion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "သင့်သည် အကျိုးရှိသော အကူအညီပေးသူဖြစ်ပါသည်။"},
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
print(answer)

if answer:
    speak(answer)



