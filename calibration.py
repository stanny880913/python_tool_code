from re import I
import cv2
import numpy as np
import yaml
import os

with open(os.path.expanduser("~") + "/catkin_ws/src/AWR1843_ros/awr1843_ros/config/config.yaml", 'r') as stream:
    try:
        config = yaml.full_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

size_RGB = config['size_RGB_712p']
size_RGB_Calib = config['size_RGB_Calib']

cmatrix = np.array(config['K4']).reshape(3, 3)
dmatrix = np.array(config['D4']).reshape(1, 5)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(
    cmatrix, dmatrix, size_RGB, 1, size_RGB_Calib)

img = cv2.imread('src/AWR1843_ros/awr1843_ros/scripts/exper/1.jpg')

img = cv2.undistort(img, cmatrix, dmatrix, None, newcameramtx)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite('calib.jpg', img)
