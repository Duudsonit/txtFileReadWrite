import os


filename = raw_input('Enter file name:')

print fileName
fobj = open(fileName,'w+')
while True:
    aLine = raw_input('Enter a line("." to quit):')
    if aLine != ".":
        fobj.write('%s%s' % (aLine,os.linesep))       
    else:
        break
fobj.close()

fobj = open(fileName,'r+')
allLine = fobj.readlines()
fobj.close()
print allLine
