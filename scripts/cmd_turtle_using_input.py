#!/usr/bin/env python
#-*- coding: utf-8 -*-
# testing code
# 김재훈 선임 연구원님이 피드백해주신 내 코드 + WeGo의 Convention rule 적용

import rospy
from geometry_msgs.msg import Twist

# return None
def go(_msg=Twist(), _pub=rospy.Publisher("cmd_vel", Twist, queue_size=1)):
    _msg.linear.x = 2.0
    _msg.angular.z = 0.0
    _pub.publish(_msg)

# return None
def right(_msg=Twist(), _pub=rospy.Publisher("cmd_vel", Twist, queue_size=1)):
    _msg.linear.x = 2
    _msg.angular.z = -1.5
    _pub.publish(_msg)

# return None
def left(_msg=Twist(), _pub=rospy.Publisher("cmd_vel", Twist, queue_size=1)):
    _msg.linear.x = 2
    _msg.angular.z = 1.5
    _pub.publish(_msg)

if __name__ == '__main__':
    rospy.init_node("cmd_vel")
    cmd_vel_pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    drive_msg = Twist()
    direction = ""
    try:
        while direction != "stop":
            direction = raw_input("go or left or right, stop for quit : ")
        
            if direction == "go":
                go(drive_msg, cmd_vel_pub)            
            elif direction == "left":
                left(drive_msg, cmd_vel_pub)
            elif direction == "right":
                right(drive_msg, cmd_vel_pub)
        
        
    except Exception as e:
        rospy.logwarn("Please Input One of These : go, left, right, stop")
        rospy.logwarn(e)