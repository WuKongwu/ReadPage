import sys, urllib
from getHtml import read
from readTxt import readTxt
from writeNumber import write
html_str = "<html></html>"
re = readTxt()
number = int(re.readNumber())
rep = read()
while (True):
    try:
        rep.readPage(number)
        number+=1
    except:
        print str(number) + ' not find'
        wr = write()
        wr.writeNumber(number)
        #raw_input('Press Enter to exit...')
        sys.exit()