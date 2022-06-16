
import rospy
from std_msgs.msg import String

def talker():

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('tele', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        message = 'a welcome message'
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


