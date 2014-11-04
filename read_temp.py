import sys
import os

class TempData(object):

    def __init__(self,data=None,temp=None,idDevice=None):
        self.date = data
        self.temp = temp
        self.idDevice = idDevice

    def parseFromString(self,string, delimeter=' '):
        arr = string.rstrip().split(delimeter)

        if len(arr) == 4:
            self.date = arr[0] + ' ' + arr[1]
            self.temp = float(arr[2])
            self.idDevice = arr[3]
        else:
            print 'Temp::parseFromString: error'

    def __str__(self):
        return self.date +' '+self.temp +' '+self.idDevice

class ReaderTempFromFile(object):

    def __init__(self, fname):
        self.fname = fname

    def tail(self,n,devid = None):
        line_len = 38
        iter = 0
        with open(self.fname) as f:
            data = []
            try:
                f.seek(-(line_len*n),2)
            except IOError:
                #print 'file smaller'
                return None

            while True:
                iter +=1
                try:
                    f.seek(-(line_len*iter),2)
                except IOError:
                    f.seek(0)

                line = f.read(line_len)

                tempData = TempData()
                tempData.parseFromString(line)

                if tempData.idDevice == devid or devid == None: 
                    data.append(tempData)
                            
                if len(data) >= n or f.tell() == line_len:
                    break
            return data
   
    def getTemp(self, devid = None):
        data = self.tail(1,devid)
        if data:
            return data[0].temp
        else:
            return 0


    def getAverageTemp(self, n, devid = None):
        data = self.tail(n,devid)
        if data:
            s = sum(tempData.temp if self.isValidTemp(tempData.temp) else 0 for tempData in data)
            return s / len(filter(self.isValidTemp, data))
        else:
            return 0

    def isValidTemp(self, temp):
        if temp > 0:
            return True
        else:
            return False

if __name__ == '__main__':
  reader = ReaderTempFromFile('temp.dat')
  print reader.getTemp()
  print reader.getAverageTemp(10)
