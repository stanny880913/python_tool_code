import os
from PIL import Image

# 指定原始PNG文件夹和目标JPG文件夹的路径
png_folder = '/home/stannyho/Documents/ros/bags/sample_data/7/png'
jpg_folder = '/home/stannyho/Documents/ros/bags/sample_data/7/jpg'

# 遍历原始PNG文件夹中的所有文件
for filename in os.listdir(png_folder):
    if filename.endswith('.png'):
        # 构造完整的文件路径
        png_path = os.path.join(png_folder, filename)
        
        # 生成目标JPG文件路径，将文件名的后缀改为.jpg
        jpg_filename = os.path.splitext(filename)[0] + '.jpg'
        jpg_path = os.path.join(jpg_folder, jpg_filename)
        
        # 打开PNG文件并转换为JPG格式
        image = Image.open(png_path)
        image = image.convert('RGB')
        
        # 保存为JPG文件
        image.save(jpg_path, 'JPEG')
        print(f"转换文件: {filename} -> {jpg_filename}")
