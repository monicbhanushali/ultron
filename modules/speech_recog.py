import webbrowser
import speech_recognition as sr

r = sr.Recognizer()

#with sr.Microphone() as source:
#		print ('Say Something!')
#		audio = r.listen(source)
#		print ('Done!')

#text = r.recognize_google(audio)
#print(text)

#if text=="open Google":
 #   url = "https://www.google.com/"
  #  webbrowser.get().open(url)
#else:
 #   print("ok")

while True:
    command=""
    with sr.Microphone() as source:
        audio = r.listen(source)
        print(audio)
        if audio==None:
            print("no voice")
        command = r.recognize_google(audio).lower()
        print(command)
        if command=="hi ultron":
            print("speak now......")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            if text=="open Google":
                url = "https://www.google.com/"
                webbrowser.get().open(url)
            else:
                print("command not found")
        else:
            print("ultron not called..")
