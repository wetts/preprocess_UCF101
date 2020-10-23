import os
import cv2

dataset_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/datasets'
label_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/labels/ucfTrainTestlist/trainlist01.txt'
image_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/_image'

# for index, d in enumerate(os.listdir(dataset_path)):
#     print(index, d)
def check(label_path, dataset_path):
    with open(label_path, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            (p, l) = line.split(' ')

            video_path = os.path.join(dataset_path, p)
            cap = cv2.VideoCapture(video_path)
            if cap.isOpened():
                a = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                b = 0
                while True:
                    ret, frame = cap.read()
                    if ret == False:
                        break
                    b += 1
                
                if not int(a) == b:
                    print(p, a, b)

def create_dataframe(label_path, dataset_path):
    p_list = []
    l_list = []
    cnt_frame_list = []
    with open(label_path, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            (p, l) = line.split(' ')
            p_list.append(p)
            l_list.append(l)

            video_path = os.path.join(dataset_path, p)
            cap = cv2.VideoCapture(video_path)
            if cap.isOpened():
                cnt_frame_list.append(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                cnt = 0
                while True:
                    ret, frame = cap.read()
                    if ret == False:
                        break
                    img_path = os.path.join(save_path, str(cnt) + '.jpg')
                    cv2.imwrite(img_path, frame)
                    cnt += 1
                