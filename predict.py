#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo import YOLO
from PIL import Image
import os
import time
import pandas as pd
import numpy as np

yolo = YOLO()

while True:
    filelist = os.listdir()
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = yolo.detect_image(image)
        r_image.show()

# TIANCHI
# filelist = os.listdir("mchar_test_a")
# cnt = -1
# test_label_pred = ["123"]*40000
# for img in filelist:
#     try:
#         image = Image.open("mchar_test_a/" + img)
#     except:
#         print('Open Error! Try again!')
#         continue
#     else:
#         cnt += 1
#         print(cnt)
#         # if cnt == 10 :
#         #     break
#         # r_image = yolo.detect_image(image ,test_label_pred, cnt)
#         test_label_pred = yolo.detect_image(image ,test_label_pred, cnt)
#         # time.sleep(2)
#         # r_image.show()

df_submit = pd.read_csv('mchar_sample_submit_A.csv')
df_submit['file_code'] = test_label_pred
df_submit.to_csv('submit9-12.csv', index=None)