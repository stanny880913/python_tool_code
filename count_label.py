# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 05:00:08 2021

@author: Hsiang
"""




import os

def CountLabel(path):

    # path = "/home/stannyho/Documents/PyTorch_YOLOv4/data/img" #TXT路徑
    
    
    files= os.listdir(path) #得到路徑下所有檔案名稱
    txts = []
    frames = 0
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    count14 = 0
    count15 = 0
    count16 = 0
    count17 = 0
    count18 = 0
    count19 = 0
    count20 = 0
    count21 = 0
    count22 = 0
    count23 = 0
    count24 = 0
    count25 = 0
    count26 = 0
    count27 = 0
    
    
    for file in files:    #瀏覽資料夾
    
        if file[-2] == 'x':
            position = path+'/'+ file
            #print (position)
            with open(position, "r", encoding="utf-8") as f:
                lines=f.readlines()
                frames += 1
        
            for line in lines:
                if('0' in line[0]):     #若字首為0
                    count0 += 1         #計算類別數
                elif('1' in line[0]):
                    if('0' in line[1]):
                        count10 += 1
                    elif('1' in line[1]):
                        count11 += 1
                    elif('2' in line[1]):
                        count12 += 1
                    elif('3' in line[1]):
                        count13 += 1
                    elif('4' in line[1]):
                        count14 += 1
                    elif('5' in line[1]):
                        count15 += 1
                    elif('6' in line[1]):
                        count16 += 1
                    elif('7' in line[1]):
                        count17 += 1
                    elif('8' in line[1]):
                        count18 += 1
                    elif('9' in line[1]):
                        count19 += 1
        
                    else:
                        count1 += 1
        
                elif('2' in line[0]):
                    if('0' in line[1]):
                        count20 += 1
                    elif('1' in line[1]):
                        count21 += 1
                    elif('2' in line[1]):
                        count22 += 1
                    elif('3' in line[1]):
                        count23 += 1
                    elif('4' in line[1]):
                        count24 += 1
                    elif('5' in line[1]):
                        count25 += 1
                    elif('6' in line[1]):
                        count26 += 1
                    elif('7' in line[1]):
                        count27 += 1
        
                    else:
                        count2 += 1
        
                elif('3' in line[0]):
                    count3 += 1
                elif('4' in line[0]):
                    count4 += 1
                elif('5' in line[0]):
                    count5 += 1
                elif('6' in line[0]):
                    count6 += 1
                elif('7' in line[0]):
                    count7 += 1
                elif('8' in line[0]):
                    count8 += 1
                elif('9' in line[0]):
                    count9 += 1
    
    
    print("\n========== LabelSum ==========")

    print()
    print("Frames :", frames) #Frames = 有label的照片數量
    
    print("\nperson :", count0)
    print("motor :", count1)
    print("bike :", count2)
    print("car :", count3)
    print("truck :", count4)
    print("bus :", count5)
    print("motor-people :", count6)
    print("bike-people :", count7)
    print("NB3 :", count8)
    print("NC3 :", count9)
    print("ND3 :", count10)
    print("ND4 :", count11)
    print("NA4 :", count12)
    print("SC1 :", count13)
    print("SB1 :", count14)
    print("Trafficlight :", count15)
    print("C16 :", count16)
    print("C17 :", count17)
    print("C18 :", count18)
    print("C19 :", count19)
    print("C20 :", count20)
    print("C21 :", count21)
    print("C22 :", count22)
    print("C23 :", count23)
    print("C24 :", count24)
    print("C25 :", count25)
    print("C26 :", count26)
    print("C27 :", count27)


    print("==============================")

if __name__ == '__main__':

    path = '/home/stannyho/Documents/PyTorch_YOLOv4/data/img'

    files=os.listdir(path)

    print(files)

    CountLabel(path)