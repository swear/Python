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

print '������Ҫ������ļ�Ŀ¼:',
filepath = raw_input()
filepath = filepath.strip('\\')
files = os.listdir(filepath)
for filename in files:
    if filename.endswith('����.txt'):
        index = filename.index('����')
        basefilename = filename[0:index]
        filename1 = filepath + '\\' + filename
        filename2 = filepath + '\\' + basefilename + '��α'
        filename3 = filepath + '\\' + basefilename + '����-��α-���.txt'
        print '����' + filename1 + '��' + filename2 + ', �����ļ���' + filename3
        generatefile(filename1, filename2, filename3)

