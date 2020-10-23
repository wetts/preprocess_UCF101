import os
import cv2
import pandas as pd


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

def create_dataframe(label_path, dataset_path, target_path):
    p_list = []
    l_list = []
    cnt_frame_list = []
    with open(label_path, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            (p, l) = line.split(' ')
            p_list.append(p)
            l_list.append(l)

            strs = p.split('/')
            save_path = os.path.join(target_path, strs[0])
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            save_path = os.path.join(save_path, strs[1].split('.')[0])
            if not os.path.exists(save_path):
                os.makedirs(save_path)
                
            video_path = os.path.join(dataset_path, p)
            cap = cv2.VideoCapture(video_path)
            if cap.isOpened():
                cnt_frame_list.append(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                # cnt = 0
                # while True:
                #     ret, frame = cap.read()
                #     if ret == False:
                #         break
                #     img_path = os.path.join(save_path, str(cnt) + '.jpg')
                #     cv2.imwrite(img_path, frame)
                #     cnt += 1
    df = pd.DataFrame({'path': p_list, 'label': l_list, 'frame_count': cnt_frame_list})
    return df
                
if __name__ == "__main__":
    dataset_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/datasets'
    label_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/labels/ucfTrainTestlist/trainlist01.txt'
    image_root_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/_image/original'
    csv_path = '/80f765ab0dcd4fee9c897c6ff9211e3f/userdata/zws/UCF-101/labels/train01.csv'
    
    # for index, d in enumerate(os.listdir(dataset_path)):
    #     print(index, d)
    df = create_dataframe(label_path, dataset_path, image_root_path)
    df['pre_done'] = 0
    df.to_csv(csv_path, index=False)