#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
import math

class TurtleStateMachine:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.directions = ['East', 'North', 'West', 'South']

    def get_direction(self, theta):
        # Normalize theta (angle in radians) to one of the 4 main directions
        angle_deg = math.degrees(theta)
        if angle_deg < 0:
            angle_deg += 360

        if 45 <= angle_deg < 135:
            return 'North'
        elif 135 <= angle_deg < 225:
            return 'West'
        elif 225 <= angle_deg < 315:
            return 'South'
        else:
            return 'East'

    def update_pose(self, pose):
        self.x = round(pose.x, 2)
        self.y = round(pose.y, 2)
        self.theta = pose.theta
        direction = self.get_direction(pose.theta)
        rospy.loginfo(f"Turtle is at ({self.x}, {self.y}) facing {direction}")

def pose_callback(data):
    bot.update_pose(data)

if __name__ == '__main__':
    rospy.init_node('turtle_pose_tracker', anonymous=True)
    bot = TurtleStateMachine()
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.spin()