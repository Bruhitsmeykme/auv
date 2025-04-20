 📷 ROS OpenCV Camera Pipeline – Final Task

So for the final task, the goal was to set up a full pipeline: get live camera feed, run edge detection on it, publish that to a ROS topic, and then view the result from another node.

Since I’m using WSL, I couldn’t test OpenCV display windows directly (they don’t work in WSL unless you set up an X server), but I still wrote both the publisher and subscriber nodes and had them reviewed.

---

## 📌 Edge Detection Node

I made a class `EdgeDetector` that:
- Subscribes to `/camera/image_raw`
- Converts the image using `cv_bridge`
- Applies **Canny Edge Detection**
- Publishes the result to `/camera/edges`

### Code Summary:

python
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
📺 Edge Viewer Node
Next, I created a EdgeViewer class that:

Subscribes to the /camera/edges topic

Converts the image to OpenCV format

Displays it using OpenCV's imshow

Code Summary:
python
Copy code
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
✅ Final Pipeline Summary
Camera publishes to /camera/image_raw

EdgeDetector subscribes → runs Canny → publishes to /camera/edges

EdgeViewer subscribes to /camera/edges → shows live image

Everything is connected through ROS, and OpenCV handles the processing and display. Can’t test GUI in WSL but the logic and flow are all in place.
