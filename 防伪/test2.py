#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
print '������Ҫ������ļ�Ŀ¼:', 
filepath = raw_input()
files = os.listdir(filepath)
for filename in files:
    if filename.endswith('.txt'):
        index = filename.index('����')
        basefilename = filename[0:index]
        filename1 = filename
        filename2 = basefilename + '��α'
        filename3 = basefilename + '����-��α-���'
        print filename1 + ',' + filename2 + ',' + filename3
