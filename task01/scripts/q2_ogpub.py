#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
if __name__ == '__main__':
    pub = rospy.Publisher('multipleof2', Int32,queue_size=10)
    rospy.init_node('ogpub', anonymous=True)
    rate=rospy.Rate(1)

    num=1
    while not rospy.is_shutdown():
        multiple = num*2
        pri = multiple
        rospy.loginfo(f"Publishing: {multiple} " )
        pub.publish(multiple)
        num+=1
        rate.sleep()