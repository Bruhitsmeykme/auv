#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

pub = None  

def callback(d):
    result = d.data * 10
    rospy.loginfo(f"Received {d.data}, publishing {result}")
    pub.publish(result)

def subscriber():
    global pub
    rospy.init_node('multiplier', anonymous=True)
    pub = rospy.Publisher('times10', Int32, queue_size=10)
    rospy.Subscriber('multipleof2', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()






