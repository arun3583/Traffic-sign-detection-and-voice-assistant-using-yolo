from gtts import gTTS
from playsound import playsound
def play(path):
    playsound(path)
mytext="hi how are you"
myobj = gTTS(text=mytext, lang='en', slow=True)
myobj.save("welcome.mp3")
play("welcome.mp3")
