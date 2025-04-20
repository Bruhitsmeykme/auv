#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class EdgeDetector:
    def __init__(self):
        rospy.init_node('edge_detector_node', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.callback)
        self.image_pub = rospy.Publisher('/camera/edges', Image, queue_size=10)

    def callback(self, data):
        try:
            frame = self.bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)
            edge_image_msg = self.bridge.cv2_to_imgmsg(edges, encoding='mono8')
            self.image_pub.publish(edge_image_msg)
        except Exception as e:
            rospy.logerr(f"Error in edge detection: {e}")

if __name__ == '__main__':
    try:
        EdgeDetector()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass