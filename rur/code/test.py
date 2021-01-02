#!/usr/bin/env python3
# encoding: utf-8
#from pose import keyword
import random
import rospy
from geometry_msgs.msg import PoseStamped
import speech_recognition
from gtts import gTTS
import os
from playsound import playsound
from std_msgs.msg import String
nha_bep=[3.80154156685,-0.643521368504,-0.491017983521,0.871149436009]
ban_1=[0.9,0.1,0.2,0.3]

"""goal_publisher = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=10)
rospy.init_node("mynode")
goal = PoseStamped()
def haha():
    goal.header.seq = 1
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"

    goal.pose.position.x = 3.80154156685 
    goal.pose.position.y = -0.643521368504
    goal.pose.position.z = 0.0

    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = -0.491017983521
    goal.pose.orientation.w = 0.871149436009
    goal_publisher.publish(goal)"""

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
    """if "Hello" in you:
        bot_brain ="Xin chào giang"
    elif "thời tiết" in you:
        bot_brain = " Hôm nay trời đẹp vãi cả l "
    elif "đầu đẹp" in you:
        bot_brain = " vãi l đầu cắt moi "
    elif "trời" in you:
        bot_brain = " Hôm nay trời đẹp vãi cả lon luôn "
    elif "ngày" in you:
        bot_brain ="săps tết rồi hỏi ngày làm gì hả bạn"
        keyword(nha_bep)
    elif "bye" in you:
        bot_brain = "Chào tạm biệt và hẹn mai đi nhậu."
    elif "Ai đẹp trai nhất" in you:
        bot_brain ="tất nhiên là anh giang đẹp trai rồi"
    elif "nhà bếp" in you:
        bot_brain ="vâng"
        keyword(ban_1)
    elif "kết thúc" in you:
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

        playsound('Siri.mp3')"""
    if "xin chào" in you:
        bot_brain =["Xin chào bạn","xin chào khách hàng","hoan nghênh khách hàng",
        "xin chào ngài","xin chào quý vị","xin chao giang","chào mừng khách hàng","hello quý khách",
        "chào mừng bạn đến với cửa hàng chúng tôi",]
    elif "khỏe" in you:
        bot_brain=["cảm ơn bạn , tôi vẫn ổn","cảm ơn bạn tôi vẫn khỏe","thank you,tôi vẫn tốt",
        "vẫn khỏe ,cảm ơn bạn","tôi vẫn ổn , cảm ơn bạn","tôi vất rất khỏe,còn chạy được cả ngày",
        "tôi vẫn rất tốt,tôi có thể giúp gì cho bạn","tôi vẫn khỏe ,cảm ơn,tôi có thể giúp gì cho bạn"]
    elif "menu" in you or "thực đơn"in you:
        bot_brain=["đồ uống có coffee, cà phê sữa,sữa chua,trà xanh, trà sữa,và nhiều nữa,đồ  ăn có bánh quy\
        gà chiên giòn,bò tái,thịt quay và vân vân"]
    elif "coffee"in you or "cà phê"in you:
        bot_brain=["ok,đồ uống thành công","đã đặt","ok,cảm ơn"]
    elif "kết thúc"in you:
        bot_brain=["cảm ơn bạn","cảm ơn quý khách",""]
    elif "bye"in you or"tạm biệt"in you:
        bot_brain=["cảm ơn bạn,hẹn gặp lại","cảm ơn quý khách,hẹn gặp lại","bye"]
    else:
        bot_brain=["bạn có thể nhắc lại được không","xin lỗi tôi không hiểu","xin lỗi,bộ não tôi còn kém"]
    tts = gTTS(text =bot_brain[random.randint(0,len(bot_brain)-1)],lang='vi')
    tts.save("Siri.mp3")
    playsound('Siri.mp3')
