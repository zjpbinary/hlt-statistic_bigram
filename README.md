# hlt-statistic_bigram

## bigram语言模型
### 基于极大似然与统计实现
### 一.目录结构
.\data:  
     train.conll:已经分好词的中文文本，用于建立模型   
     dev.conll:已经分好词的中文文本，用于测试  
.\establish.py:建立bigram模型，保存概率转移矩阵于transfermatrix,保存词及其对应的索引于worddict  
.\eva.py:读取保存的bigram模型，在dev上进行计算困惑度  

### 二.运行
#### 1.运行环境
python3.8  
windows  
#### 2.执行
python establish.py  
python eva.py
