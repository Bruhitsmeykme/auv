#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import threading

def jolyne(pub):
    while not rospy.is_shutdown():
        msg = input("JOLYNE: ")
        pub.publish("Jolyne: " + msg)

def joestar(pub):
    while not rospy.is_shutdown():
        msg = input("JOESTAR: ")
        pub.publish("Joestar: " + msg)

def callback(msg):
    rospy.loginfo(msg.data)

if __name__ == '__main__':


    rospy.init_node('chatter', anonymous=True)
    pub = rospy.Publisher('chat', String, queue_size=10)
    sub = rospy.Subscriber('chat', String, callback)

    # Launch both chats in separate threads
    threading.Thread(target=jolyne, args=(pub,), daemon=True).start()
    threading.Thread(target=joestar, args=(pub,), daemon=True).start()

    rospy.spin()


    