#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class EdgeViewer:
    def __init__(self):
        rospy.init_node('edge_viewer_node', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/edges', Image, self.callback)

    def callback(self, data):
        try:
            edge_img = self.bridge.imgmsg_to_cv2(data, desired_encoding='mono8')
            cv2.imshow("Edge Detected Image", edge_img)
            cv2.waitKey(1)
        except Exception as e:
            rospy.logerr(f"Error displaying image: {e}")

if __name__ == '__main__':
    try:
        EdgeViewer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        cv2.destroyAllWindows()