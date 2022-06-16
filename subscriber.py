#!/usr/bin/env python

import rospy
from std_msgs.msg import String

print("I am listening")

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.loginfo(data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter" ,String , callback)

    rospy.spin()

if __name__ == '__main__':
    listener()





