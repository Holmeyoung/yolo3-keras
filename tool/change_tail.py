# used to change png,jpeg to jpg

import cv2
import os

print ('change png and jpeg to jpg')
files = os.listdir('JPEGImages')
for f in files:
    if f.split('.')[-1] != 'jpg':
        print ('not jpg:', f)
        img = cv2.imread('JPEGImages/'+f)
        if img is not None:
            cv2.imwrite('JPEGImages/'+f.split('.')[0]+'.jpg', img)

        else:
            subprocess.call('rm JPEGImages/'+f, shell=True)
            subprocess.call('rm Annotations/'+f.split('.')[0]+'.xml', shell=True)
            print ('img None error:', f)

