import sys, urllib
class write:
    def writeNumber(self,number):
        try:
            fileName = "number.txt"
            fp = open(fileName,"w+") 
            fp.write(str(number))
            fp.close() 
            print "write number over"
        except:
            print 'write error'
            sys.exit()




