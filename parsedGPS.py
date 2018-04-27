#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time
import numpy as np


test = RFM69.RFM69(RF69_915MHZ, 2, 10, True)
  
    
print "reading"



def all_same(items):
	return all(x == items[0] for x in items)
	
	
def gpsgo():	
  
	validate=False 




	while (validate==False):
		test.receiveBegin()
	   
									
		while not test.receiveDone():
			time.sleep(2)      
			
			D1=[]
			D2=[]
			D3=[]
		
			i=0
			
			
			while (i<=2):
			
				GPS=("".join([chr(letter) for letter in test.DATA]))
				GPS_DATA=GPS.split()
				
				rx=int(GPS_DATA[1])
				ry=int(GPS_DATA[2])
				rt=int(GPS_DATA[4])
				px=int(GPS_DATA[7])
				py=int(GPS_DATA[8])
				pt=int(GPS_DATA[10])
				dx=int(GPS_DATA[13])
				dy=int(GPS_DATA[13])
		
			
				ROB_DATA=[rx,ry,rt]
				PSG_DATA=[px,py,pt]
				DES_DATA=[dx,dy]
				D1.append(ROB_DATA)
				D2.append(PSG_DATA)
				D3.append(DES_DATA)
				
				i+=1
		
			
		#print "%s from %s RSSI:%s" % ("".join([chr(letter) for letter in test.DATA]), test.SENDERID, test.RSSI)
		#print(ROB_DATA,PSG_DATA,DES_DATA) 
		validateROB=all_same(D1)
		validatePSG=all_same(D2)
		validateDES=all_same(D3)
		validateVEC=[validateROB,validatePSG,validateDES]
		validate=all_same(validateVEC)
		#print(validateVEC)
		#print(validate)
		
		
		
		if test.ACKRequested():
			test.sendACK()
	#print "shutting down"
	test.shutdown()
	return (ROB_DATA,PSG_DATA,DES_DATA)
	
