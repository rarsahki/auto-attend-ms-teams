import speech_recognition as sr
import sys
r = sr.Recognizer()
i = 0
while(i == 0):
    with sr.Microphone() as source:
        print("start the the music machaa")
        audioData = r.record(source, duration=5, offset=None)
        try:
            text = r.recognize_google(audioData,language = 'en-IN', show_all = True)
            if("roll number" in text["alternative"][0]["transcript"] or text["alternative"][1]["transcript"] or text["alternative"][2]["transcript"] or text["alternative"][3]["transcript"] or text["alternative"][4]["transcript"]):
                print('{}'.format("Na found pann"))
                i = 1
            continue
        except Exception as e:
            print(repr(e))
            print("ommale speak properly da dei ")
            continue


