
import rospy
from geometry_msgs.msg import Twist

class go_forward():     #what does the code do
    def __init__(self): #who is the code talking to
        rospy.init_node('go_forward', anonymous=False) #

        rospy.loginfo("To stop turtlebot ctlr + C")
        
        rospy.on_shutdown(self.shutdown)     #how to end program

        self.cmd_vel=rospy.Publisher('cmd_vel',Twist,queue_size=10)  #establish that publisher is cmd_vel
        r= rospy.Rate(10);

        move_cmd= Twist()

        move_cmd.linear.x = 1.0

        move_cmd.angular.z = 0

        while not rospy.is_shutdown():    #when ctrl+C is not pressed run this
            self.cmd_vel.publish(move_cmd)
            r.sleep()

    def shutdown(self):
        rospy.loginfo('Stop Turtlebot')

        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == "__main__":
    try:
    
        go_forward()
    
    except:
            rospy.loginfo("node termianted")










      
