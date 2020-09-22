import os
import numpy as np
import codecs
import json
from glob import glob
import cv2
import shutil
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import pandas as pd

defect_name2label = {
    '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0
}

# 1.标签路径
image_path1 = "mchar_train.json"  # 原始labelme标注数据路径
image_path2 = "mchar_val.json"  # 原始labelme标注数据路径
saved_path = "VOCdevkit/VOC2007/"  # 保存路径

# 2.创建要求文件夹
if not os.path.exists(saved_path + "Annotations"):
    os.makedirs(saved_path + "Annotations")
if not os.path.exists(saved_path + "JPEGImages/"):
    os.makedirs(saved_path + "JPEGImages/")
if not os.path.exists(saved_path + "ImageSets/Main/"):
    os.makedirs(saved_path + "ImageSets/Main/")

json_file1 = "mchar_train.json" #比赛json格式路径
json_file2 = "mchar_val.json"
files = [1]
# 4.读取标注信息并写入 xml
for json_file in [json_file1]:
    anno_result = pd.read_json(open(json_file, "r"))
    # file_name_list = list(set(anno_result['name']))
    file_name_list = [key for key in anno_result]

    for file_name in tqdm(file_name_list):

        with codecs.open(saved_path + "Annotations/" + file_name.split('.')[0] + ".xml", "w", "utf-8") as xml:
            height, width, channels = 1000, 2446, 3

            xml.write('<annotation>\n')
            xml.write('\t<folder>' + 'VOC2007' + '</folder>\n')
            xml.write('\t<filename>' + file_name + '</filename>\n')
            xml.write('\t<source>\n')
            xml.write('\t\t<database>The UAV autolanding</database>\n')
            xml.write('\t\t<annotation>UAV AutoLanding</annotation>\n')
            xml.write('\t\t<image>flickr</image>\n')
            xml.write('\t\t<flickrid>NULL</flickrid>\n')
            xml.write('\t</source>\n')
            xml.write('\t<owner>\n')
            xml.write('\t\t<flickrid>NULL</flickrid>\n')
            xml.write('\t\t<name>GuangDongDec</name>\n')
            xml.write('\t</owner>\n')
            xml.write('\t<size>\n')
            xml.write('\t\t<width>' + str(width) + '</width>\n')
            xml.write('\t\t<height>' + str(height) + '</height>\n')
            xml.write('\t\t<depth>' + str(channels) + '</depth>\n')
            xml.write('\t</size>\n')
            xml.write('\t\t<segmented>0</segmented>\n')
            # "height": [219, 219], "label": [1, 9], "left": [246, 323], "top": [77, 81], "width": [81, 96]
            # bbox = anno_result[anno_result['name'] == file_name]
            bbox = anno_result[file_name]
            for h, la, l, t, w in zip(bbox['height'], bbox['label'], bbox['left'], bbox['top'], bbox['width']):
                xmin = l
                xmax = l + w
                ymin = t
                ymax = t + h
                label = la
                if xmax <= xmin:
                    pass
                elif ymax <= ymin:
                    pass
                else:
                    xml.write('\t<object>\n')
                    xml.write('\t\t<name>' + str(label) + '</name>\n')
                    xml.write('\t\t<pose>Unspecified</pose>\n')
                    xml.write('\t\t<truncated>1</truncated>\n')
                    xml.write('\t\t<difficult>0</difficult>\n')
                    xml.write('\t\t<bndbox>\n')
                    xml.write('\t\t\t<xmin>' + str(xmin) + '</xmin>\n')
                    xml.write('\t\t\t<ymin>' + str(ymin) + '</ymin>\n')
                    xml.write('\t\t\t<xmax>' + str(xmax) + '</xmax>\n')
                    xml.write('\t\t\t<ymax>' + str(ymax) + '</ymax>\n')
                    xml.write('\t\t</bndbox>\n')
                    xml.write('\t</object>\n')
                # print(multi['name'],xmin,ymin,xmax,ymax,label)
            xml.write('</annotation>')

for json_file in [json_file2]:
    anno_result = pd.read_json(open(json_file, "r"))
    # file_name_list = list(set(anno_result['name']))
    file_name_list = [key for key in anno_result]

    for file_name in tqdm(file_name_list):

        with codecs.open(saved_path + "Annotations/" + "0" + str(int(file_name.split('.')[0])+30000) + ".xml", "w", "utf-8") as xml:
            height, width, channels = 1000, 2446, 3

            xml.write('<annotation>\n')
            xml.write('\t<folder>' + 'VOC2007' + '</folder>\n')
            xml.write('\t<filename>' + "0" + str(int(file_name.split('.')[0])+30000) + '</filename>\n')
            xml.write('\t<source>\n')
            xml.write('\t\t<database>The UAV autolanding</database>\n')
            xml.write('\t\t<annotation>UAV AutoLanding</annotation>\n')
            xml.write('\t\t<image>flickr</image>\n')
            xml.write('\t\t<flickrid>NULL</flickrid>\n')
            xml.write('\t</source>\n')
            xml.write('\t<owner>\n')
            xml.write('\t\t<flickrid>NULL</flickrid>\n')
            xml.write('\t\t<name>GuangDongDec</name>\n')
            xml.write('\t</owner>\n')
            xml.write('\t<size>\n')
            xml.write('\t\t<width>' + str(width) + '</width>\n')
            xml.write('\t\t<height>' + str(height) + '</height>\n')
            xml.write('\t\t<depth>' + str(channels) + '</depth>\n')
            xml.write('\t</size>\n')
            xml.write('\t\t<segmented>0</segmented>\n')
            # "height": [219, 219], "label": [1, 9], "left": [246, 323], "top": [77, 81], "width": [81, 96]
            # bbox = anno_result[anno_result['name'] == file_name]
            bbox = anno_result[file_name]
            for h, la, l, t, w in zip(bbox['height'], bbox['label'], bbox['left'], bbox['top'], bbox['width']):
                xmin = l
                xmax = l + w
                ymin = t
                ymax = t + h
                label = la
                if xmax <= xmin:
                    pass
                elif ymax <= ymin:
                    pass
                else:
                    xml.write('\t<object>\n')
                    xml.write('\t\t<name>' + str(label) + '</name>\n')
                    xml.write('\t\t<pose>Unspecified</pose>\n')
                    xml.write('\t\t<truncated>1</truncated>\n')
                    xml.write('\t\t<difficult>0</difficult>\n')
                    xml.write('\t\t<bndbox>\n')
                    xml.write('\t\t\t<xmin>' + str(xmin) + '</xmin>\n')
                    xml.write('\t\t\t<ymin>' + str(ymin) + '</ymin>\n')
                    xml.write('\t\t\t<xmax>' + str(xmax) + '</xmax>\n')
                    xml.write('\t\t\t<ymax>' + str(ymax) + '</ymax>\n')
                    xml.write('\t\t</bndbox>\n')
                    xml.write('\t</object>\n')
                # print(multi['name'],xmin,ymin,xmax,ymax,label)
            xml.write('</annotation>')
# 5.复制图片到 VOC2007/JPEGImages/下

for image_path in [image_path1, image_path2]:
    image_files = glob(image_path + "*.jpg")
    print("copy image files to VOC007/JPEGImages/")
    for image in tqdm(image_files):
        shutil.copy(image, saved_path + "JPEGImages/")

# #6.split files for txt
txtsavepath = saved_path + "ImageSets/Main/"
ftrainval = open(txtsavepath + '/trainval.txt', 'w')
ftest = open(txtsavepath + '/test.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fval = open(txtsavepath + '/val.txt', 'w')
total_files = glob("VOC2007/Annotations/*.xml")
total_files = [i.split("/")[-1].split(".xml")[0] for i in total_files]
# test_filepath = ""
for file in total_files:
    ftrainval.write(file + "\n")
# test
# for file in os.listdir(test_filepath):
#     ftest.write(file.split(".jpg")[0] + "\n")
# split
train_files, val_files = train_test_split(total_files, test_size=0.15, random_state=42)
# train
for file in train_files:
    ftrain.write(file + "\n")
# val
for file in val_files:
    fval.write(file + "\n")

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()