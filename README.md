# pykit_meng

个人常用python程序中整理

## 结构

1. **file** ： 文件操作
2. **geo** ： 经纬度坐标、地图等相关

## file

### file.suffixFilter()
**以后缀名过滤文件夹中的文件，可同时过滤多个后缀名**

**input**：suffixFilter(文件夹路径,*一个或多个后缀名) 
 *eg.* suffixFilter('./result','.xlsx','.txt')

**output**：(符合该后缀的文件路径数组, 符合该后缀的文件名数组)
*eg.* fileSuffixPath, fileSuffixName = suffixFilter('./result','.xlsx','.txt')


## geo