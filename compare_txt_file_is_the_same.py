import os

def compare_txt_files(folder_path):
    # 列出資料夾中的所有檔案
    file_list = os.listdir(folder_path)

    # 選取所有.txt檔案的絕對路徑
    txt_files = [os.path.join(folder_path, file) for file in file_list if file.endswith(".txt")]

    if not txt_files:
        print("No .txt files found in the folder.")
        return

    # 讀取第一個txt檔案的內容
    with open(txt_files[0], 'r', encoding='utf-8') as file:
        reference_content = file.read()

    # 初始化結果字典
    results = {}

    # 進行txt檔案內容比對
    for file in txt_files[1:]:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 比對內容是否相同
        is_same = (content == reference_content)

        # 將結果保存到字典
        results[(os.path.basename(txt_files[0]), os.path.basename(file))] = is_same

    return results

if __name__ == "__main__":
    # 替換以下路徑為你的資料夾路徑
    folder_path = "/media/stannyho/ssd/Pseudo_Lidar_V2/data/trainval/train/calib"

    comparison_results = compare_txt_files(folder_path)
    for files, is_same in comparison_results.items():
        if is_same:
            print(f"Content of {files[1]} is the same as {files[0]}.")
        else:
            print(f"Content of {files[1]} is different from {files[0]}.")



