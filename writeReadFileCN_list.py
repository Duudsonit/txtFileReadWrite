'''
Created on 2015-4-26
@author: hy
'''

import os
#coding: utf-8
print '�ó���Ĺ������ȴ���һ���ı��ļ������������ݣ�Ȼ���ļ����������'
print os.linesep
fileName = raw_input('�������´����ļ���·�����ļ���:')
print '��������ļ�·�����ļ���Ϊ:'
print fileName
print os.linesep
fileContent = open(fileName,'w+')
while True:
    aLine = raw_input('������һ���ı�("." ��������):')
    if aLine != ".":
        fileContent.write('%s%s' % (aLine,os.linesep))       
    else:
        break
fileContent.close()

print os.linesep
fileContent = open(fileName,'r+')
allLine = fileContent.readlines()
print'�����������Ϊ:'
print allLine
fileContent.close()
