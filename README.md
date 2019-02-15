# yolo3_keras

## 工具
### 数据标注工具
参考 `GITHUB` [**tzutalin/labelImg**](https://github.com/tzutalin/labelImg)

用于标注图像中的物体位置并生成 `xml` 文件

- 目录结构
  ```sh
  $ tree -N
  .
  ├── Annotations
  │   └── PartB_02404.xml
  ├── ImageSets
  │   └── Main
  └── JPEGImages
      └── PartB_02404.jpg
  ```

### tool/make_main_txt.py
用于根据生成的 `xml` 文件分割成训练集、测试集、验证集

- 目录结构
  ```sh
  $ tree -N
  .
  ├── Annotations
  │   └── 0.xml
  ├── ImageSets
  │   └── Main
  │       ├── test.txt
  │       ├── train.txt
  │       ├── trainval.txt
  │       └── val.txt
  └── JPEGImages
      └── 0.jpg
  ```

- 文件解析
  - 关于源码文件

    参见 `make_main_txt.py` `第4行--第5行`
    
    ```python
    trainval_percent = 0.66
    ```
    
    `train+val` 所占的比例，剩余为 `test`

    ```python
    train_percent = 0.5
    ```
    
    `train+val` 中 `train` 所占的比例

  - 关于生成文件
    - `test.txt` 测试集

    - `train.txt` 训练集
    
    - `trainval.txt` 训练集+验证集
    
    - `val.txt` 验证集


### tool/voc_annotation.py
用于根据生成的 `train.txt`、`val.txt`、`test.txt`，读取 `txt` 文件里对应的 `xml` 文件并解析，生成对应 `yolo` 格式的数据集

相对于原作者的文件，我做了几处改动
- 增加了当图片中没有要标注的物体时的异常处理
  
- 增加了当 `xml` 中 `xmin`、`ymin`等包含小数的问题

> 注：因为 `train.py` 只用到一个训练数据集文件并会自动将其中的数据按照 `9:1` 的比例切分为训练集和验证集，所以我们在得到 `train.txt`、 `test.txt`、 `val.txt` 数据集切分文件之后应将其合并为一个 `train.txt` 文件并将其指定为训练数据集以避免训练数据的浪费

### tool/wider_annotation.py
用于将 [**WIDER FACE**](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/) 数据集转化为 `yolo3` 的训练集

数据样式
```txt
0--Parade/0_Parade_Parade_0_904.jpg
1
361 98 263 339 0 0 0 0 0 0 
0--Parade/0_Parade_marchingband_1_799.jpg
21
78 221 7 8 2 0 0 0 0 0 
78 238 14 17 2 0 0 0 0 0 
113 212 11 15 2 0 0 0 0 0 
134 260 15 15 2 0 0 0 0 0 
163 250 14 17 2 0 0 0 0 0 
201 218 10 12 2 0 0 0 0 0 
182 266 15 17 2 0 0 0 0 0 
245 279 18 15 2 0 0 0 0 0 
304 265 16 17 2 0 0 0 2 1 
328 295 16 20 2 0 0 0 0 0 
389 281 17 19 2 0 0 0 2 0 
406 293 21 21 2 0 1 0 0 0 
436 290 22 17 2 0 0 0 0 0 
522 328 21 18 2 0 1 0 0 0 
643 320 23 22 2 0 0 0 0 0 
653 224 17 25 2 0 0 0 0 0 
793 337 23 30 2 0 0 0 0 0 
535 311 16 17 2 0 0 0 1 0 
29 220 11 15 2 0 0 0 0 0 
3 232 11 15 2 0 0 0 2 0 
20 215 12 16 2 0 0 0 2 0 
```

样式说明
```wiki
Attached the mappings between attribute names and label values.

blur:
  clear->0
  normal blur->1
  heavy blur->2

expression:
  typical expression->0
  exaggerate expression->1

illumination:
  normal illumination->0
  extreme illumination->1

occlusion:
  no occlusion->0
  partial occlusion->1
  heavy occlusion->2

pose:
  typical pose->0
  atypical pose->1

invalid:
  false->0(valid image)
  true->1(invalid image)

The format of txt ground truth.
File name
Number of bounding box
x1, y1, w, h, blur, expression, illumination, invalid, occlusion, pose
```

### tool/brainwash_annotation.py
用于将 [**Brainwash dataset**](https://exhibits.stanford.edu/data/catalog/sx925dc9385) 数据集转化为 `yolo3` 的训练集

数据样式
```txt
"brainwash_10_27_2014_images/00153000_640x480.png": (389.0, 112.0, 407.0, 138.0), (508.0, 134.0, 527.0, 159.0);
"brainwash_10_27_2014_images/00154000_640x480.png": (383.0, 111.0, 404.0, 137.0);
"brainwash_10_27_2014_images/00156000_640x480.png": (488.0, 123.0, 508.0, 149.0);
"brainwash_10_27_2014_images/00157000_640x480.png": (167.0, 224.0, 237.0, 289.0);
"brainwash_10_27_2014_images/00158000_640x480.png";
"brainwash_10_27_2014_images/00160000_640x480.png": (459.0, 153.0, 494.0, 193.0);
"brainwash_10_27_2014_images/00161000_640x480.png";
```

样式说明
```wiki
"path_to_image": (xmin, ymin, xmax, ymax);
```



### tool/change_tail.py

用于将 `jpeg`、`png` 后缀图像统一修改为 `jpg` 后缀并检测图片是否为空



### tool/auto_convert_script.py

将 `change_tail.py` 、`make_main_txt.py` 、`voc_annotation.py` 合并为一个自动化执行脚本



### yolo 格式的数据集究竟什么样

```sh
One row for one image:
Row format: image_file_path box1 box2 ... boxN
Box format: x_min,y_min,x_max,y_max,class_id (no space)
```

样例
```sh
path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
path/to/img2.jpg 120,300,250,600,2
...
```

> 其实不管中间步骤如何，只是为了最后生成 `yolo` 格式的数据集，进而执行 `train.py` 进行训练

## 运行
### 自己的例子
```sh
python demo.py
```

### 官网的例子
#### 简单运行
1. Download YOLOv3 weights from [YOLO website](https://pjreddie.com/media/files/yolov3.weights)

2. Convert the Darknet YOLO model to a Keras model

3. Run YOLO detection

```sh
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
python yolo_video.py [video_path] [output_path (optional)]
```

For Tiny YOLOv3, just do in a similar way, just specify model path and anchor path with `--model model_file` and `--anchors anchor_file`

#### 具体使用
执行 `python yolo_video.py --help` 查看具体说明

```sh
usage: yolo_video.py [-h] [--model MODEL] [--anchors ANCHORS]
                    [--classes CLASSES] [--gpu_num GPU_NUM] [--image]
                    [--input [INPUT]] [--output [OUTPUT]]

optional arguments:
  -h, --help         show this help message and exit
  --model MODEL      path to model weight file, default model_data/yolo.h5
  --anchors ANCHORS  path to anchor definitions, default
                    model_data/yolo_anchors.txt
  --classes CLASSES  path to class definitions, default
                    model_data/coco_classes.txt
  --gpu_num GPU_NUM  Number of GPU to use, default 1
  --image            Image detection mode, will ignore all positional
                    arguments
  --input [INPUT]    Video input path
  --output [OUTPUT]  [Optional] Video output path
```

**多GPU使用**

MultiGPU usage: use `--gpu_num N` to use N GPUs

## 训练
### 核心要义
**`生成 YOLO 格式的TXT数据集`**
```sh
One row for one image:
Row format: image_file_path box1 box2 ... boxN
Box format: x_min,y_min,x_max,y_max,class_id (no space)
```

样例 -- `train.txt`
```sh
path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
path/to/img2.jpg 120,300,250,600,2
...
```

- `image_file_path`

  图片路径。建议使用**绝对路径**

- `boxN`
  
  标注的图像框坐标 + 图像框内图像对应的类别ID（索引）
  例：
  ```python
  classes = ["aeroplane", "bicycle", "bird", "boat"]
  ```
  则 `bird` 类别对应的 ID 为 `2`



### 标注训练数据

- 通过图像标注工具 [**tzutalin/labelImg**](https://github.com/tzutalin/labelImg) 标注训练图片，具体见教程 [【AI实战】手把手教你训练自己的目标检测模型（SSD篇）](https://my.oschina.net/u/876354/blog/1927351)。生成如下目录

  ```sh
  .
  ├── Annotations
  │   └── 0.xml
  ├── ImageSets
  │   └── Main
  └── JPEGImages
      └── 0.jpg
  
  ```

  - `Annotations`
    里面是 `xml` 文件。由 `labelImg` 生成， 存储着图像名、图像中的物体类别、各个物体的坐标位置等信息

  - `JPEGImages`
    里面是图像

  - `ImageSets`
    下一步用到，用于存储切分的 `txt` 文件

  这一步：主要根据图像标注工具labelImg，基于图片，采用手动标注方式，生成物体坐标及对应类别的xml文件

  

- 执行 `tool/auto_convert_script.py`
  具体参数说明见上

  - 将文件放置于 `Annotations` `同级`目录

    目录结构如下

    ```sh
    $ tree -N            
    .
    ├── auto_convert_script.py
    ├── Annotations
    │   └── 0.xml
    ├── ImageSets
    │   └── Main
    └── JPEGImages
        └── 0.jpg
    
    4 directories, 3 files
    ```

    

  - 运行
    ```sh
    python auto_convert_script.py
    ```
    
    

  - 生成如下目录
    ```sh
    $ tree -N
    .
    ├── auto_convert_script.py
    ├── Annotations
    │   └── 0.xml
    ├── ImageSets
    │   └── Main
    │       ├── test.txt
    │       ├── train.txt
    │       ├── trainval.txt
    │       └── val.txt
    ├── JPEGImages
    │   └── 0.jpg
    └── train.txt
    
    4 directories, 8 files
    ```
    这一步：生成 `train.txt`



- 下载预加载权重
  - 下载yolo权重文件 `yolov3.weights` 
    
    [下载地址](https://pjreddie.com/media/files/yolov3.weights)
    
    下载后放置于 `model_data` 文件夹内

  - 转化权重文件为 `keras` 格式
    ```sh
    python convert.py -w yolov3.cfg model_data/yolov3.weights model_data/yolo_weights.h5
    ```

- 执行 `train.py`
  - 修改配置文件路径 `annotation_path`、`log_dir`、`classes_path`、`anchors_path`
    
    分别对应

    annotation_path：训练集文件路径

    log_dir：输出模型路径

    classes_path：分类文件路径

    anchors_path：切分格子数量配置文件路径

  - 修改预加载权重模型位置 `weights_path='model_data/yolo_weights.h5'`

  - 修改预训练过程的 `batch_size` 、`epoch`

  - 修改训练过程的 `batch_size` 、`epoch`

  运行 `train.py`
  ```sh
  python train.py
  ```

### 根据已有 `VOC` 格式数据训练
同 `自己标注数据训练` 过程

但是去除了自己通过标注工具标注训练数据那一步

### 根据 `WIDER FACE` 数据集训练
- 参考 `tool/wider_annotation.py` 中 `路径设置` ，将 `wider_annotation.py` 置于`相对位置`

- 运行 `wider_annotation.py`
  ```sh
  python wider_annotation.py
  ```

- 将 `train.py` 的 `annotation_path` 指定为 `wider_annotation.py` 的 `out_file` 路径

- 运行 `train.py`
  ```sh
  python train.py
  ```

## 头部识别数据集
[SCUT-HEAD](https://www.ctolib.com/HCIILAB-SCUT-HEAD-Dataset-Release.html)

[HollywoodHeads dataset](https://www.di.ens.fr/willow/research/headdetection/)

[Brainwash dataset](https://exhibits.stanford.edu/data/catalog/sx925dc9385)

[WIDER FACE](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/)

## 参考
### 主要源码
主要基于 [**qqwweee/keras-yolo3**](https://github.com/qqwweee/keras-yolo3) 修改了几个文件

### 参考教程
[【AI实战】动手训练自己的目标检测模型（YOLO篇）](https://my.oschina.net/u/876354/blog/1927881)

[【AI实战】手把手教你训练自己的目标检测模型（SSD篇）](https://my.oschina.net/u/876354/blog/1927351)
