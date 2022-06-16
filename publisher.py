#!/usr/bin/env python

import rospy 

from std_msgs.msg import String

def hello_world_pub():                      #define function
    pub = rospy.Publisher('chatter', String, queue_size=10)         #publish to channel "hello_world" any subscriber to "hello_world" will hear this
    rospy.init_node('giver', anonymous=True)  #initialize node
    rate = rospy.Rate(10)                    #Rate is ros function to control speed
    i=0
    while not rospy.is_shutdown():          #while ROS is running ie. ctrl+c hasnt been pressed

        pub.publish("hello world" +str(i))
        i+=1
        rate.sleep()

if __name__ == '__main__':
    try:
        hello_world_pub()

    except rospy.ROSInterruptException:
        pass