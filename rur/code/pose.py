#from pickle import TRUE
import rospy
import random
import time
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
rospy.init_node("mynode")

goal_publisher = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=10)

goal = PoseStamped()

def keyword(li):
    goal.header.seq = 1
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"

    goal.pose.position.x = li[0]
    goal.pose.position.y = li[1]
    goal.pose.position.z = 0.0

    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = li[2]
    goal.pose.orientation.w = li[3]
    goal_publisher.publish(goal)
def text_key(you):
    if "xin chào" in you:
        bot_brain =["Xin chào bạn","xin chào khách hàng","hoan nghênh khách hàng",
        "xin chào ngài","xin chào quý vị","xin chao giang","chào mừng khách hàng","hello quý khách",
        "chào mừng bạn đến với cửa hàng chúng tôi",]
    elif "khỏe" in you or "ổn"in you:
        bot_brain=["cảm ơn bạn , tôi vẫn ổn","cảm ơn bạn tôi vẫn khỏe","thank you,tôi vẫn tối",
        "vẫn khỏe ,cảm ơn bạn","tôi vẫn ổn , cảm ơn bạn","tôi vất rất khỏe,còn chạy được cả ngày",
        "tôi vẫn rất tốt,tôi có thể giúp gì cho bạn","tôi vẫn khỏe ,cảm ơn,tôi có thể giúp gì cho bạn"]
    elif "menu"in you or"thực đơn" in you:
        bot_brain=["đồ uống có coffee, cà phê sữa,sữa chua,trà xanh, trà sữa,và nhiều nữa,đồ  ăn có bánh quy\
        gà chiên giòn,bò tái,thịt quay và vân vân"]
    elif "coffee"in you or"cà phê"in you or"bánh"in you or"gà"in you or"bò"in you:
        bot_brain=["ok,đồ uống thành công","đã đặt","ok,cảm ơn"]
    elif "kết thúc"in you:
        bot_brain=["cảm ơn bạn","cảm ơn quý khách",""]
    elif "bye"in you or"tạm biệt"in you:
        bot_brain=["cảm ơn bạn,hẹn gặp lại","cảm ơn quý khách","bye"]
    else:
        pass
    return(bot_brain[random.randint(0,len(bot_brain)-1)])
