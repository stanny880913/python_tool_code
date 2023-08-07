import cv2
import numpy as np

# 輸入影片長寬需一致

capL = cv2.VideoCapture('/home/stannyho/Documents/fuban/BSD/code/detect_video/9.mp4')    #左邊影片
capR = cv2.VideoCapture('/home/stannyho/Documents/fuban/BSD/code/detect_video/8.mp4')    #右邊影片

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('/home/stannyho/Documents/fuban/BSD/code/detect_video/8_9_concat.mp4', fourcc, 30, (1280*2, 712))    #輸出影片及長寬

while capL.isOpened():

    ret1, frame1 = capL.read()
    ret2, frame2 = capR.read()

    if ret1 == True:

        img_hconcat = cv2.hconcat([frame1, frame2])

        out.write(np.uint8(img_hconcat))
        cv2.imshow('frame', np.uint8(img_hconcat))

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

capL.release()
capR.release()
out.release()
cv2.destroyAllWindows()