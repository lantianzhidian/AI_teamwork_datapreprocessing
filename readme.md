# 环境依赖
`import pandas as pd`

`from PIL import Image`

# 用法指南

>注意：只需修改`definitions.py`中的变，`main.py`不用修改。

## 1.必须修改的路径参数
使用前请先设置路径，`definition.py`中的`IMAGEDIR`,`NEWCSVDIR`,`NEWIMAGEDIR`。

`IMAGEDIR`:放置原图像的文件目录，实例：
>`IMAGEDIR = "/home/zhuchencs/yanyi/aihomework/cloud_dataset/images/"`

`NEWCSVDIR`:放置新生成的`train.csv`的文件目录，示例：
>`NEWCSVDIR = "/home/zhuchencs/yanyi/aihomework/cloud_dataset_new/"`

`NEWIMAGEDIR`：放置新生成的图片的文件夹路径，示例：
>`NEWIMAGEDIR = "/home/zhuchencs/yanyi/aihomework/cloud_dataset_new/images/"`

## 2.其他可以自定义的参数
|变量名|用途|备注|
|-----|---|---|
|RESIZE|生成图片的大小|`RESIZE=500`说明生成的图片为500*500|
|IMG_NUM_EACH_TYPE|为每个类型的图片增强到～张|`IMG_NUM_EACH_TYPE=200`说明每个类型的图片生成到2000张|

# 结果

生成`train.csv`和新的图片

新`train.csv`的格式为：

|`image_name`|`type1`|`type2`|...|`type28`|
|-----------|-------|-------|-----|-----|
|1_1.png|1|0|...|0|
|1_2.png|1|0|...|0|
|...|...|...|...|...|
|28_2000.png|0|0|...|1|