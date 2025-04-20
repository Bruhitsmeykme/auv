#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

def teleport_turtle(x=0.0, y=0.0, theta=0.0):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleport = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        teleport(x, y, theta)
        rospy.loginfo("Teleported turtle to (0, 0) facing East.")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

def send_cmd(cmd):
    move = Twist()
    if cmd == 'forward':
        move.linear.x = 2.0
        move.angular.z = 0.0
    elif cmd == 'backward':
        move.linear.x = -2.0
        move.angular.z = 0
    elif cmd == 'right':
        move.linear.x = 0.0
        move.angular.z = -1.6
    elif cmd == 'left':
        move.linear.x = 0.0
        move.angular.z = 1.6
    else:
        rospy.logwarn("Unknown Command, no movement")
    return move

if __name__ == '__main__':
    rospy.init_node('turtlemover', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)

    # Teleport to (0,0) at start
    teleport_turtle(0.0, 0.0, 0.0)

    while not rospy.is_shutdown():
        command = input("Enter command (forward/backward/right/left): ")
        rospy.loginfo(f"Sending command: {command}")
        cmd_msg = send_cmd(command)
        pub.publish(cmd_msg)
        rate.sleep()
