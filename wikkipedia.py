import pyttsx3,wikipedia
title = input("enter the title")
result = wikipedia.summary(title, sentence_=_2)
print(result)
engine = pyttsx3.init()
engine.say(result)
engine.runAndWait()
