import numpy as np
import matplotlib.pyplot as plt

def visualize_npy(npy_file):
    # 讀取.npy檔案為Numpy數組
    img_array = np.load(npy_file)

    # 設定背景為透明
    fig, ax = plt.subplots(facecolor='none')

    # 顯示圖片
    ax.imshow(img_array, cmap='gray', interpolation='nearest')
    ax.axis('off')  # 不顯示坐標軸
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig('output_image.png', bbox_inches='tight', pad_inches=0, transparent=True)
    plt.show()

if __name__ == "__main__":
    # 替換以下路徑為你的.npy檔案路徑
    npy_file_path = "/media/stannyho/ssd/Pseudo_Lidar_V2/results/depth/npy/prediction_d_0.npy"

    visualize_npy(npy_file_path)
