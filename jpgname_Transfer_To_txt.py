# -*- coding: utf-8 -*-
import os
import random

def listname(path, trainpath, testpath, valpath):
    path = "/home/stannyho/Documents/PyTorch_YOLOv4/data/imgg"  # 存放想轉jpg檔名的照片
    filelist = os.listdir(path)  # 檢視圖片目錄下的檔案,相當於shell指令ls
    filelist.sort()
    f1 = open(trainpath, 'w')  # 開啟圖片列表清單txt檔案
    f2 = open(valpath, 'w')
    f3 = open(testpath, 'w')
    for files in filelist:
        Olddir = os.path.join(path, files)
        if os.path.isdir(Olddir):
            continue
        if "xml" not in str(files):
            if random.randint(0, 9) < 5:  # (0,9)為隨機產生數字
                f1.write("data/img/"+files)
                f1.write('\n')
            elif 6 < random.randint(0, 9) < 8:
                f2.write("data/img/"+files)
                f2.write('\n')
            else:
                f3.write("data/img/"+files)
                f3.write('\n')
    f1.close()
    f2.close()
    f3.close()

savepath = "/home/stannyho/Documents/PyTorch_YOLOv4/data"  # 修改為自己的存放txt路徑
trainpath = savepath+"/train.txt"
valpath = savepath+"/val.txt"
testpath = savepath+"/test.txt"
listname(savepath + "/list", trainpath, valpath, testpath)
print("Txt have been created!")
