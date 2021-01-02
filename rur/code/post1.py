#from pickle import TRUE
import rospy
import time
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
rospy.init_node("mynode")

goal_publisher = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=10)

goal = PoseStamped()
def haha():
    goal.header.seq = 1
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"

    goal.pose.position.x = 1.0 
    goal.pose.position.y = 2.0
    goal.pose.position.z = 0.0

    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    goal_publisher.publish(goal)
    rospy.spin()
def bebe():
    goal.header.seq = 1
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"

    goal.pose.position.x = 55555
    goal.pose.position.y = 22222
    goal.pose.position.z = 0.0

    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    rospy.sleep(1)
    goal_publisher.publish(goal)
    rospy.spin()
while True:
    bebe()
    haha()