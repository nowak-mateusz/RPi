#!/usr/bin/python

import sys
import cgi
import os
import re
from time import sleep, strftime

temps={}
path="/sys/bus/w1/devices"
devlist=os.listdir(path)
logfile = os.path.join(os.getcwd(),'temp.dat')


while True:
    for dev in devlist:
        if dev !="w1_bus_master1" and dev !=".":
            tf=open("%s/%s/w1_slave"%(path, dev))
            null=tf.readline()
            temp=tf.readline()
            r=re.match(r'.*t=(\d+)$', temp)
            if r:
                temps[dev]=float(r.group(1))/1000
            tf.close()

    fo = open(logfile, 'a+') 

    for t in temps:
        #print strftime("%d-%m %H:%M:%S")+" %s %s"%(temps[t],t)
        log_entry = strftime("%d-%m %H:%M:%S")+" %.3f %s\n"%(float(temps[t]),t)
        fo.write(log_entry)
    
    fo.close()

    if len(sys.argv)==2:
        sleep(float(sys.argv[1]))
    else:
        sleep(1)
