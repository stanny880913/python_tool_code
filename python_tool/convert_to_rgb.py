import os
import cv2
import numpy as np
from tqdm import tqdm  # 導入 tqdm

def gray_to_3channel(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    filenames = os.listdir(input_folder)  # 取得檔案列表
    for filename in tqdm(filenames, desc="Converting images"):  # 使用 tqdm 遍歷檔案列表，添加進度條
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, filename)

        gray_img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
        h, w = gray_img.shape
        
        gray_3channel_img = np.stack((gray_img,) * 3, axis=-1)
        
        cv2.imwrite(output_image_path, gray_3channel_img)

input_folder_path = "/media/stannyho/ssd/pseudo_lidar/own_data/depth"
output_folder_path = "/media/stannyho/ssd/pseudo_lidar/own_data/depth_rgb"

gray_to_3channel(input_folder_path, output_folder_path)
