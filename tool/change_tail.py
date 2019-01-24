# used to change png,jpeg to jpg

import cv2
import os

files = os.listdir('VOCdevkit/VOC2007/JPEGImages')
for f in files:
    if f.split('.')[-1] != 'jpg':
        print ('not jpg:', f)
        img = cv2.imread('VOCdevkit/VOC2007/JPEGImages/'+f)
        if img is not None:
            cv2.imwrite('VOCdevkit/VOC2007/JPEGImages/'+f.split('.')[0]+'.jpg', img)

        else:
            print ('img None error:', f)

