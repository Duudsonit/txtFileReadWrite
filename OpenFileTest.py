import os
filename = raw_input('Enter file name:')
print filename
fobj = open(filename,'w+')
while True:
    aLine = raw_input('Enter a line("." to quit):')
    if aLine != ".":
        fobj.write('%s%s' % (aLine,os.linesep))
        print aLine
    else:
        break
fobj.close()