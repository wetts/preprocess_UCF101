import cv2
import os
import subprocess


def split_frame(file, path):
    if not os.path.exists(path):
        os.mkdir(path)
    os.system('ffmpeg -i {} -r 25  -qscale:v 2 -f image2 {}/%03\d.jpg'.format(file, path))


root = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/dataset/video'
target_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/dataset/_image'
for dir in os.listdir(root):
    target_path = os.path.join(target_path, dir)
    if os.path.isdir(os.path.join(root, dir)):
        for croot, _, file in os.walk(os.path.join(root, dir)):
            for i in file:
                if i.split('.')[1] == 'avi':
                    print('start', i)
                    name = i.split('.')[0]
                    pic_path = os.path.join(target_path, name)
                    video_path = os.path.join(croot, i)
                    split_frame(video_path, pic_path)
                    print('done', i)
print('done')
