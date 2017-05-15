import sys, urllib
from pyquery import PyQuery as pq
 
your_url = 'http://www.heiyan.com/ajax/book/68270/1660333?_=1492593247431'
d = pq(url=your_url)
table = d("#ChapterContent1659793")
p = d("p")

end = p.text().encode('GBK')
fileName = "web111.txt"
fp = open(fileName,"w+") 
fp.write(end)
fp.close() 
print "ok"

#text = p.text()
