import os

# 指定要更改文件名的文件夹路径
folder_path = '/media/stannyho/ssd/Pseudo_Lidar_V2/data/calib'

# 获取文件夹中的所有文件
file_list = os.listdir(folder_path)

# 文件名的初始编号
start_number = 0

# 遍历文件列表
for file_name in file_list:
    # 构造新的文件名
    new_file_name = f"prediction_d_{start_number:d}.txt"

    # 获取文件的完整路径
    file_path = os.path.join(folder_path, file_name)

    # 构造新的文件路径
    new_file_path = os.path.join(folder_path, new_file_name)

    # 重命名文件
    os.rename(file_path, new_file_path)

    print(f"重命名文件: {file_name} -> {new_file_name}")

    # 增加文件名编号
    start_number += 1
