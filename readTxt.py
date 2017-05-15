#
class readTxt:
    def readNumber(self):
        f = open("number.txt")            
        line = f.readline()       
        f.close() 
        return line 