#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
def callback(d):
    final_reuslt=d.data + 5
    rospy.loginfo(f"Final result: {d.data} + 5 = {final_reuslt}")

def subscriber():
    rospy.init_node('Fsub',anonymous=True)
    rospy.Subscriber('times10',Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()    