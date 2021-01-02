# encoding: utf-8
import speech_recognition
from gtts import gTTS
import os
from playsound import playsound

while True:
    
    bot_brain= "Ban đầu chưa học gì nên não chưa có thông tin"
    bot_ear = speech_recognition.Recognizer()#Siri nghe
    while True:
        with speech_recognition.Microphone() as mic:
            print("\nSiri: I'm listening")
            #audio = bot_ear.listen(mic)
            audio = bot_ear.record(mic, duration= 3) #Siri nghe trong vòng 3 giây sau đó tắt Mic, tránh treo máy do bật Mic lien tục
            print("\nSiri: ....")
        try:
            you = bot_ear.recognize_google(audio,language='vi-VN')# nó sẽ lấy giọng của chị Google
            print("\nYou: "+you)   
        except:
            you ="Tôi không hiểu bạn nói gì."
            print("\nSiri: "+you)
        else:
            break
    if u"Xin chào" in you:
        bot_brain ="Xin chào giang"
    elif u"thời tiết" in you:
        bot_brain = " Hôm nay trời đẹp vãi cả l "
    elif u"đầu đẹp" in you:
        bot_brain = " vãi l đầu cắt moi "
    elif u"trời" in you:
        bot_brain = " Hôm nay trời đẹp vãi cả lon luôn "
    elif u"ngày" in you:
        bot_brain ="săps tết rồi hỏi ngày làm gì hả bạn"
    elif u"bye" in you:
        bot_brain = "Chào tạm biệt và hẹn mai đi nhậu."
    elif u"Ai đẹp trai nhất" in you:
        bot_brain ="tất nhiên là anh giang đẹp trai rồi"
    elif u"thoát" in you:
        bot_brain="tạm biệt bạn sai giô na ra "
        tts = gTTS(text =bot_brain,lang='vi')
        tts.save("Siri.mp3")
        #os.system("start Siri.mp3")
        playsound('Siri.mp3')
        break

    else:
        bot_brain =" bạn có thể nhắc lại không ạ"
        print("\nSiri: "+bot_brain)
    print("\nSiri: "+bot_brain)
    if bot_brain!="k":
        #print (bot_brain) 
        tts = gTTS(text =bot_brain,lang='vi')
        tts.save("Siri.mp3")
        #os.system("start Siri.mp3")

        playsound('Siri.mp3')