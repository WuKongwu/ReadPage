import sys, urllib
from pyquery import PyQuery as pq
from readTxt import readTxt
import os,sys
import time
class read:
    def readPage(self,number):
        try:
            your_url = 'http://www.g884.cn/?id='+str(number)
            d = pq(url=your_url)
            # Get context 
            table = d("#post-5580").attr("align","left")
            p = d("p")
            text = p.text()
            end = text.encode('GBK')
            # Get title
            title = d("#content").find("h1").text().encode('GBK')
            title = title.replace("-","_")
            fileName = title + "_"+str(number)+".txt"
            path = sys.path[0] + '/'+ str(time.strftime('%Y%m%d',time.localtime(time.time()))) #create path 
            isExists=os.path.exists(path)
            if not isExists:
                os.makedirs(path)
            filePath = path +'/' + fileName
            fp = open(filePath,"w+") 
            fp.write(end)
            fp.close() 
            print str(number) + ":ok"
        except Exception:
            sys.exit()

