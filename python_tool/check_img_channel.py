import cv2


def check_channels_opencv(image_path):
    img = cv2.imread(image_path)
    channels = img.shape[2]
    return channels

img_path = '/media/stannyho/ssd/pseudo_lidar/own_data/depth_rgb/prediction_d_0.jpg'
channels = check_channels_opencv(img_path)
print(f"Image channels: {channels}")
