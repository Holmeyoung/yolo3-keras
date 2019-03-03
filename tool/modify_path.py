# used to change the file path

import os
import re
from tqdm import tqdm
import subprocess

if os.path.exists('tmp') == False:
    os.makedirs('tmp')

files = os.listdir('Annotations')
for f in tqdm(files):
    if f.split('.')[-1] != 'xml':
        print ('xml format error:', f)
        subprocess.call('rm Annotations/%s' % (f), shell = True) 
        continue
    # re.sub(str to be changed, str to change)
    open('tmp/'+f, 'w').write(re.sub(r'C:\\Users\\lianjia\\Desktop\\JPEGImages\\JPEGImages\\', r'/root/tmp/yolo_1/data/JPEGImages/', open('Annotations/'+f).read()))

subprocess.call('rm -r Annotations', shell = True)
subprocess.call('mv tmp Annotations', shell = True)
