import os

filename = raw_input('文件的路径和文件名:')
print filename
f = open(filename,'w+')
while True:
    aLine = raw_input('请输入一行文本("." 退出输入):')
    if aLine != ".":
        f.write('%s%s' % (aLine,os.linesep))
        print aLine
    else:
        break
f.close()
