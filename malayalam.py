import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import datetime
import wikipedia
import pywhatkit

earings=sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("listening..")
        earings.adjust_for_ambient_noise(source)
        voice=earings.listen(source)
        text=earings.recognize_google(voice,language="ml-IN")
        print(text)
except:
    pass

if 'എന്താണ് പേര്' in text:
    txt='എന്റെ പേര് സോഫിയ'
    mal=gTTS(txt,lang='ml')
    mal.save("voice.mp3")
    playsound("voice.mp3")
elif 'എന്താണ് വിശേഷം' in text:
    txt1="എനിക്ക് സുഖമാണ്"
    txt2="താങ്കൾക്കു സുഖമാണോ"
    mal1=gTTS(txt1,lang='ml')
    mal2=gTTS(txt2,lang='ml')
    mal1.save('voice1.mp3')
    mal2.save('voice2.mp3')
    playsound('voice1.mp3')
    playsound('voice2.mp3')
elif 'സമയം' in text:
    time=datetime.datetime.now().strftime("%I:%M %p")
    print(time)
    mal=gTTS(time,lang='ml')
    mal.save("voice.mp3")
    playsound("voice.mp3")
elif 'തീയതി' in text:
    date=datetime.datetime.now().strftime("%d/%B/%Y")
    print(date)
    mal=gTTS(date,lang='ml')
    mal.save("voice.mp3")
    playsound("voice.mp3")
elif 'ആരാണ്' in text:
    person=text.replace('ആരാണ്','')
    wikipedia.set_lang('ml')
    info=wikipedia.summary(person,3
    )
    print(info)
    mal=gTTS(info,lang='ml')
    mal.save("voice.mp3")
    playsound("voice.mp3")
elif ('കേൾക്കണം' in text)or('കാണണം' in text):
    if 'കേൾക്കണം' in text:
        song=text.replace('കേൾക്കണം','')
        pywhatkit.playonyt(song)
    elif 'കാണണം' in text:
        film=text.replace('കാണണം','')
        pywhatkit.playonyt(film)








       