#https://github.com/cyZhu-upup/AFEW_preprocess/blob/master/video_to_image.py

import cv2
import os
import subprocess
import re
import random
# import dlib

count = 1  # 用来给图片按序号命名


# def face_crop(path, files):
#     global count
#     predictor_model = '/Users/zcyyy/Documents/硕士学习/临时/dataset/AFEW/shape_predictor_68_face_landmarks.dat'
#     detector = dlib.get_frontal_face_detector()  # dlib人脸检测器
#     predictor = dlib.shape_predictor(predictor_model)
#     pre_img = os.path.join(path, files)  # 读入时的图片绝对路径
#     cur_img = str(count)+'.'+'jpg'
#     cur_img = os.path.join(path, cur_img)  # 读出时的图片绝对路径
#     print("file is {}".format(pre_img))
#     # cv2读取图像
#     img = cv2.imread(pre_img)
#     # 人脸数rects
#     rects = detector(img,0)
#     # faces存储full_object_detection对象
#     faces = dlib.full_object_detections()

#     if len(rects) > 0:
#         for i in range(len(rects)):
#             faces.append(predictor(img, rects[i]))

#         face_images = dlib.get_face_chips(
#             img, faces, size=224)  # 输出尺寸（224，224）
#         for image in face_images:
#             cv2.imwrite(cur_img, image)
#         count += 1
#     else:
#         print('未检测到人脸')
#     os.system('rm {}'.format(pre_img))  # 去掉之前的图片


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


root = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/AFEW/train'
dirs = os.listdir(root)
data_list = {}  # key为路径，value为路径下的视频
for dir in dirs:
    if os.path.isdir(os.path.join(root, dir)):
        for croot, _, file in os.walk(os.path.join(root, dir)):
            data_list[croot] = file
            for i in data_list[croot]:
                if i.split('.')[1] == 'avi':
                    name = i.split('.')[0]
                    tmp_path = os.path.join(croot, name)
                    tmp_file = croot+'/'+i
                    split_frame(tmp_file, tmp_path)

root = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/AFEW/validation'
dirs = os.listdir(root)
data_list = {}  # key为路径，value为路径下的视频
for dir in dirs:
    if os.path.isdir(os.path.join(root, dir)):
        for croot, _, file in os.walk(os.path.join(root, dir)):
            data_list[croot] = file
            for i in data_list[croot]:
                if i.split('.')[1] == 'avi':
                    name = i.split('.')[0]
                    tmp_path = os.path.join(croot, name)
                    tmp_file = croot+'/'+i
                    split_frame(tmp_file, tmp_path)