import cv2

# input image path
img = cv2.imread('/home/stannyho/Documents/aa/1003行使畫面/RGB_221003-_rear_right__000020.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = cv2.Laplacian(gray, cv2.CV_64F).var()
print(result)
