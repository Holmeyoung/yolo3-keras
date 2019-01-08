from yolo import YOLO
from PIL import Image

yolo=YOLO()
path = 'demo.jpg'
try:
    image = Image.open(path)
except:
    print('Open Error! Try again!')
else:
    r_image, _ = yolo.detect_image(image)
    r_image.show()

yolo.close_session()