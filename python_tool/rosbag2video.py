import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rosbag

# Function to convert ROS image messages to OpenCV images
def ros_image_to_cv2(ros_image):
    bridge = CvBridge()
    cv2_image = bridge.imgmsg_to_cv2(ros_image, desired_encoding="bgr8")
    return cv2_image

# Function to convert a ROS bag containing image data to a video
def rosbag_to_video(input_bagfile, output_video_file, image_topic):
    cap = None
    out = None
    bridge = CvBridge()

    try:
        bag = rosbag.Bag(input_bagfile, 'r')
        for topic, msg, t in bag.read_messages(topics=[image_topic]):
            cv2_image = ros_image_to_cv2(msg)
            if cap is None:
                height, width, _ = cv2_image.shape
                out = cv2.VideoWriter(output_video_file, cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
                cap = True
            out.write(cv2_image)
        bag.close()
        out.release()
        print(f"Video saved to {output_video_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    input_bagfile = "/home/stannyho/Documents/ros/bags/test_2023-10-05-11-39-57.bag"  # Replace with your ROS bag file
    output_video_file = "/home/stannyho/Documents/ros/bags/output_video.avi"  # Replace with the desired output video file
    image_topic = "/camera/image_color"  # Replace with the actual image topic in your bag file

    rosbag_to_video(input_bagfile, output_video_file, image_topic)
