import os
from difflib import ndiff

def compare_txt_files(folder_path):
    # 列出資料夾中的所有檔案
    file_list = os.listdir(folder_path)

    # 選取所有.txt檔案的絕對路徑
    txt_files = [os.path.join(folder_path, file) for file in file_list if file.endswith(".txt")]

    if len(txt_files) < 2:
        print("At least two .txt files are required for comparison.")
        return

    # 讀取所有txt檔案的內容
    file_contents = []
    for file in txt_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            file_contents.append((os.path.basename(file), content))

    # 初始化結果字典
    results = {}

    # 進行txt檔案內容比對
    for i in range(len(file_contents)):
        for j in range(i + 1, len(file_contents)):
            file1_name, file1_content = file_contents[i]
            file2_name, file2_content = file_contents[j]

            # 比對內容是否相同
            is_same = (file1_content == file2_content)

            # 若內容不同，則找出差異
            if not is_same:
                diff = list(ndiff(file1_content.splitlines(), file2_content.splitlines()))
                results[(file1_name, file2_name)] = diff

    return results

if __name__ == "__main__":
    # 替換以下路徑為你的資料夾路徑
    folder_path = "/media/stannyho/ssd/pseudo_lidar/KITTI/object/training/calib"

    comparison_results = compare_txt_files(folder_path)
    for files, diff in comparison_results.items():
        print(f"Differences between {files[0]} and {files[1]}:")
        for line in diff:
            if line.startswith("- "):
                print(f"Only in {files[0]}: {line[2:]}")
            elif line.startswith("+ "):
                print(f"Only in {files[1]}: {line[2:]}")
