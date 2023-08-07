import open3d as o3d
import numpy as np


def read_xyz(file_path):
    # Read the XYZ file using numpy
    point_data = np.loadtxt(file_path, dtype=np.float32)

    # Extract the XYZ coordinates (dist_x, dist_y, height)
    xyz = point_data[:, :3]

    # Create an Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)

    return pcd


def read_pcd(file_path):
    # return o3d.io.read_point_cloud(file_path)

    # Read the PCD file using numpy
    with open(file_path, 'rb') as f:
        # Read PCD header (first 11 lines)
        for _ in range(11):
            line = f.readline().decode().strip()
            if line.startswith('POINTS'):
                num_points = int(line.split(' ')[-1])
                break

        # Read binary data (assuming little-endian, single precision floats)
        point_data = np.fromfile(f, dtype=np.float32, count=num_points*12)

    # Reshape the data into columns
    points = point_data.reshape(-1, 12)

    # Extract the XYZ coordinates (dist_x, dist_y, height)
    xyz = points[:, :3]

    # Create an Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)

    return pcd


def set_point_cloud_color(point_cloud, color):
    # 將點雲的所有點的顏色設置為指定的顏色
    point_cloud.paint_uniform_color(color)


def visualize_point_cloud_with_image(point_cloud, image):
    # Create a list of geometries containing the point cloud and the image
    geometries = [point_cloud, image]

    # Visualize the point cloud and image together
    o3d.visualization.draw_geometries(geometries)


if __name__ == "__main__":
    # my data
    # pcd_file_path = "/media/stannyho/ssd/rc-pda/data_own/my_data/day/1/pcd/frame000000.pcd"
    # jpg_file_path = "/media/stannyho/ssd/rc-pda/data_own/my_data/day/1/img_jpg/frame000000.jpg"

    xyz_file_path = "/home/stannyho/Downloads/decomp_pc_0512_05/xyz/front_center_day_highway_decomp_pc_0512_05_pc_0.xyz"
    jpg_file_path = "/home/stannyho/Downloads/decomp_pc_0512_05/img/front_center_day_highway_decomp_pc_0512_05_img_0.jpg"

    # nuscenes
    # pcd_file_path = "/media/stannyho/ssd/rc-pda/data_own/nuscenes_sample/pcd/n008-2018-05-21-11-06-59-0400__RADAR_FRONT__1526915243042374.pcd"
    # jpg_file_path = "/media/stannyho/ssd/rc-pda/data_own/nuscenes_sample/img_jpg/n008-2018-07-27-12-07-38-0400__CAM_FRONT__1532707782762404.jpg"
    # # 讀取雷達點雲檔案
    # point_cloud = read_pcd(pcd_file_path)
    point_cloud = read_xyz(xyz_file_path)

    # 將點雲的顏色設置為紅色
    red_color = [1.0, 0.0, 0.0]  # [R, G, B]，這裡設置為紅色
    set_point_cloud_color(point_cloud, red_color)

    # 讀取照片
    image = o3d.io.read_image(jpg_file_path)

    # 可視化雷達點雲和照片
    visualize_point_cloud_with_image(point_cloud, image)
