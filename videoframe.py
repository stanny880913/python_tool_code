# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os


def FrameCut(videoFile, outputFile, timeF):
    vc = cv2.VideoCapture(videoFile)
    c = 1
    if vc.isOpened():
        rval, frame = vc.read()
        print(frame)
    else:
        print('openerror!')
        rval = False

    print(str(rval))
    while rval:
        rval, frame = vc.read()
        if c % timeF == 0:
            cv2.imwrite(outputFile + '_' + str(c).zfill(6) + '.jpg', frame)
        c += 1
        cv2.waitKey(1)
    vc.release()


if __name__ == '__main__':

    FrameCut('/home/stannyho/Downloads/0110/66.mp4',
             '/home/stannyho/Downloads/img/66_', 10)

    # 第一個''為影片所存放的路徑
    # 第二個''為照片存放的路徑
    # 以上述為例，img_test_rear_center為照片檔名稱(並且存放在data資料夾裡)
    # 10 是每10 frame拆一張
