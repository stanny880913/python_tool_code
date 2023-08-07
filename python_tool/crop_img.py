# from tqdm import tqdm
import os
import cv2
# import pandas as pd
NoneType = type(None)


# set path
project_path = "/home/stannyho/Documents/fuban"
img_data_path = str(project_path + "/Calibration_img/192_chess/")

print(img_data_path)


def get_all_files(path):
    files_List = os.listdir(path)  # list
    return files_List

# print(sorted(get_all_files(img_data_path)))
# # tag_df_label = pd.read_csv(
# #     project_path + "/tag_locCoor_label.csv", encoding="Big5")


plant_class_list = sorted(get_all_files(img_data_path))

# os.mkdir(project_path+"/192_cropped/")
# print("success")
for filename in os.listdir("/home/stannyho/Documents/fuban/Calibration_img/192_chess"):
    print(filename)
    img = cv2.imread(img_data_path+"/" + filename)
    if type(img) == NoneType:
        continue
    img_w = img.shape[1]
    #244 105 : 1039 619
    #283,188 : 929 ,596
    # 291,178 918,623(smaller)
    cropped = img[178:623, 291:918]
    # cropped = img[178:623, 291:918]
    # cropped = img[108:663, 276:1034]
    # cropped = img[188:596, 283:926]
    cv2.imwrite("/home/stannyho/Documents/fuban/Calibration_img/192_chess/" + "/" + "cropped_smaller.jpg", cropped)
