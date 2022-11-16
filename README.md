# CustomObjectDetection

本项目基于opencv，实现了自定义物品的目标识别。

目标识别与颜色识别结合

2022/11/16 
由于项目要求，库中删除部分源代码

## Tips：

pos文件夹：储存正样本

neg文件夹：储存负样本

xmlversion文件夹：训练好的xml文件

datagen脚本: 用于在将/data/dataset1中的文件复制到/data/Train_data中。并转换为能训练的格式。

addarg文件：辅助datagen脚本生成数据

train脚本：用于训练/data/Train_data中的数据，并产生xml文件。

opencv2.py：目标识别的核心文件

colorDectect.py：用于测试颜色识别的单元

raw：暂时存储用于训练的数据
