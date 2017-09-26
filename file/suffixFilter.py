# -*- coding:utf-8 -*-

#以后缀名过滤文件,可同时过滤多个后缀名
#input：suffixFilter(文件夹路径,*一个或多个后缀名)  eg.suffixFilter('./result','.xlsx','.txt')
#output：(符合该后缀的文件路径数组, 符合该后缀的文件名数组)

import os

def suffixFilter(folderName,*endstring):
    if not map(folderName.endswith, '/'):
        folderName = folderName+'/'
    listFile = os.listdir(folderName)
    a = endWith(*endstring)
    f_file = filter(a, listFile)
    fileSuffixPath=[]
    fileSuffixName=[]
    for file in f_file:
        filePath = folderName + file
        fileSuffixPath.append(filePath)
        fileSuffixName.append(file)
    return (fileSuffixPath,fileSuffixName)

def endWith(*endstring):
    ends = endstring
    def run(s):
        f=map(s.endswith,ends)
        if True in f:return s
    return run

if __name__=='__main__':
    fileSuffixPath, fileSuffixName = suffixFilter('./result','.xlsx','.txt')
    print(fileSuffixPath)
    print(fileSuffixName)