'''
Created on 2015-4-26
@author: hy
'''

import os
#coding: utf-8
print '该程序的功能是先创建一个文本文件，并输入内容，然后将文件的内容输出'
print os.linesep
fileName = raw_input('请输入新创建文件的路径和文件名:')
print '您输入的文件路径和文件名为:'
print fileName
print os.linesep
fileContent = open(fileName,'w+')
while True:
    aLine = raw_input('请输入一行文本("." 结束输入):')
    if aLine != ".":
        fileContent.write('%s%s' % (aLine,os.linesep))       
    else:
        break
fileContent.close()

print os.linesep
fileContent = open(fileName,'r+')
allLine = fileContent.readlines()
print'您输入的内容为:'
print allLine
fileContent.close()
