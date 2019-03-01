# used to change the file path

import os
import re
files = os.listdir('Annotations')
num_total = len(files)
num_now = 1
for f in files:
    print (num_now, num_total)
    num_now += 1
    if f.split('.')[-1] != 'xml':
        print ('xml format error:', f)
        continue
    # re.sub(str to be changed, str to change)
    open('tmp/'+f, 'w').write(re.sub(r'/Users/apple/Desktop/data/JPEGImages/', r'/root/tmp/data/JPEGImages/', open('Annotations/'+f).read()))
