#!/usr/bin/env python
# encoding=utf8         # 开头注释，说明源程序所用编码

'''导入模块'''
import sys
import logging
import pcl
import re           


if __name__ == "__main__":          # 作用1：作为脚本直接运行；作用2：被其他脚本调用时，不会执行

    if sys.argv.__len__() != 3:         #判断输入参数的个数
        print ("Usage: pyton ./BA.py source.pcd dest.pcd")
        print ("Auto adjust the type of file: binary or ascii")
        exit(0)							# 正常运行程序并退出程序


    pcl_src_path = sys.argv[1]		#输入的第一个参数为 原文件路径
    pcl_dest_path = sys.argv[2]		#输入的第二个参数为 输出路径

    p = re.compile("DATA (?P<data_type>\w*)")   #正则表达式（不太懂）
    data_type = "unknow"             
    with open(pcl_src_path, 'rt') as pcl_src_handle:    # rt 读写打开一个文本文件  读写标识
        lines = pcl_src_handle.readlines()            

        for index in range(12):      # 为什么是12？ 因为pcd文件前十一行是文件格式信息，后面才是点云信息
            m = p.match(lines[index])
            try:
                data_type = m.group("data_type")
                break
            except Exception as e:
                pass

    print (data_type)

    if data_type == "binary":
        print ("Convert binary to ascii")
        B = False
    elif data_type == "ascii":
        print ("Convert ascii to binary")
        B = True
    else:
        print ("Usage: pyton ./BA.py source.pcd dest.pcd")
        print ("Usage: pyton ./BA.py source.pcd ascii.pcd")
        print ("Usage: pyton ./BA.py ascii.pcd binary.pcd")

    pcl_file = pcl.PointCloud_PointXYZI()   # 
    pcl_file.from_file(pcl_src_path)        # 这里没懂
    pcl_file._to_pcd_file(pcl_dest_path, B)	 # 这里也没懂

