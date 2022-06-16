
import rospy
from std_msgs.msg import String

def chat():
    pub=rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous= True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = 'go'
        pub.publish(msg)
        #rospy.loginfo(msg)
        rate.sleep()

if __name__ == "__main__":
    #try:
        chat()
    #except rospy.ROSInterruptException:
       # pass



