#Name-Krisha Joshi
#Email ID - krisha.joshi40@nmims.edu.in
#MPSTME BTech Integrated 4th Year
#Contact No - 9967943080

import speech_recognition as s
r = s.Recognizer()
file = open("Converted-Text.txt","w+")

with s.AudioFile("sales_call_telephone_marketers.wav") as source:
    audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        file.write("Text Recognized:\n{}\r\n".format(s))
        file.close()
        #debug
        print("Open file created successfully in the folder... Text Recognized:\n "+s)
    except Exception as e:
        print("Exception Thrown: "+str(e))