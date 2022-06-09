#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class WhereToGo():
    def __init__(self):
        rospy.init_node('order_to_turtle')
        rospy.Subscriber('sub_string',String, self.string_callback)
        self.turtle_cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    
# ==================================================
#                 Callback Functions
# ==================================================
    def string_callback(self,_string_msg=String()):
        twist_msg = Twist()

        if _string_msg.data == "go":
            twist_msg.linear.x = 3.0
            twist_msg.angular.z = 0.0
        
        elif _string_msg.data == "left":
            twist_msg.linear.x = 0.0
            twist_msg.linear.y = 1.0
            twist_msg.angular.z = 0.0
            
        elif _string_msg.data == "right":
            twist_msg.linear.x = 0.0
            twist_msg.linear.y =  - 1.0
            twist_msg.angular.z = 0.0
        elif _string_msg.data == "turn":
            twist_msg.linear.x = 0.0
            twist_msg.linear.y =  0.0
            twist_msg.angular.z = 1.5
        
        else:
            rospy.logwarn("input String should be 'go', 'left', 'right', try again")
            
        self.turtle_cmd_vel_pub.publish(twist_msg)

def run():
    new_class = WhereToGo()
    rospy.loginfo("Initialized")
    rospy.spin()
    
if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        rospy.logwarn(e)
        
