#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def img_sub(data):
	cvb = CvBridge()
	try:
		cv_image = cvb.imgmsg_to_cv2(data, "bgr8")
	except CvBridgeError as e:
		print(e)

	cv2.imshow("Cam_Feed", cv_image)
	cv2.waitKey(3)

def main():
	imgSub = rospy.Subscriber("/usb_cam/image_raw", Image, img_sub)
	rospy.init_node('image_sub', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()
if __name__=="__main__":
	main()
