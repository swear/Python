#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def generatefile(filename1, filename2, filename3):
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')
    file3 = open(filename3, 'w')

    for line1 in file1:
        line1 = line1.strip()
        if line1== None or line1== '':
            continue
        line2 = file2.readline().strip()
        file3.write(line1 + ',' + line2 + '\n')
    file1.close()
    file2.close()
    file3.close()

print '请输入要处理的文件目录:',
filepath = raw_input()
filepath = filepath.strip('\\')
files = os.listdir(filepath)
for filename in files:
    if filename.endswith('物流.txt'):
        index = filename.index('物流')
        basefilename = filename[0:index]
        filename1 = filepath + '\\' + filename
        filename2 = filepath + '\\' + basefilename + '防伪'
        filename3 = filepath + '\\' + basefilename + '物流-防伪-组合.txt'
        print '处理' + filename1 + '和' + filename2 + ', 生成文件：' + filename3
        generatefile(filename1, filename2, filename3)

