import cv2
import os
import subprocess
import re
import random

def split_frame(file, path):
    global count
    if not os.path.exists(path):
        os.mkdir(path)
    # 视频逐帧转换为图片
    os.system('ffmpeg -i {} -r 25  -qscale:v 2 -f image2 {}/%03\d.jpg'.format(file, path))
    # tmp = os.listdir(path)
    # for i in tmp:  # macos运行时会有隐藏文件，下面转换时会出错
    #     if i == '.DS_Store':
    #         tmp.remove(i)
    # tmp.sort(key=lambda x: int(x[:-4]))  # tmp中的图片从小到大排序
    # for img in tmp:
    #     # 检测到是图片而不是文件夹时执行
    #     if len(img.split('.')) > 1 and img.split('.')[1] == 'jpg':
    #         face_crop(path, img)
    # count = 1


root = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/dataset/video'
target_path = ''
dirs = os.listdir(root)
data_list = {}  # key为路径，value为路径下的视频
for dir in dirs:
    if os.path.isdir(os.path.join(root, dir)):
        for croot, d, file in os.walk(os.path.join(root, dir)):
            print(croot, d, file)
            # data_list[croot] = file
            # for i in data_list[croot]:
            #     if i.split('.')[1] == 'avi':
            #         name = i.split('.')[0]
            #         tmp_path = os.path.join(croot, name)
            #         tmp_file = croot+'/'+i
            #         # split_frame(tmp_file, tmp_path)