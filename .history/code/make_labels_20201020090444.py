import os
import cv2

dataset_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/datasets'
label_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/labels/ucfTrainTestlist/trainlist01.txt'

# for index, d in enumerate(os.listdir(dataset_path)):
#     print(index, d)

p_list = []
l_list = []
with open(label_path, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        (p, l) = line.split(' ')
        print(p)