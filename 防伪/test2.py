#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
print '请输入要处理的文件目录:', 
filepath = raw_input()
files = os.listdir(filepath)
for filename in files:
    if filename.endswith('.txt'):
        index = filename.index('物流')
        basefilename = filename[0:index]
        filename1 = filename
        filename2 = basefilename + '防伪'
        filename3 = basefilename + '物流-防伪-组合'
        print filename1 + ',' + filename2 + ',' + filename3
