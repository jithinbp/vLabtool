from __future__ import print_statement
from commands_proto import *
import I2C_class
import numpy as np

class MCP4728:
	defaultVDD =3300
	RESET =6
	WAKEUP =9
	UPDATE =8
	WRITEALL =64
	WRITEONE =88
	SEQWRITE =80
	VREFWRITE =128
	GAINWRITE =192
	POWERDOWNWRITE =160
	GENERALCALL =0
	#def __init__(self,I2C,vref=3.3,devid=0):
	def __init__(self,H,vref=3.3,devid=0):
		self.devid = devid
		self.addr = 0x60|self.devid		#0x60 is the base address
		self.H=H
		self.I2C = I2C_class.I2C(self.H)
		self.SWITCHEDOFF=[0,0,0,0]
		self.VREFS=[0,0,0,0]  #0=Vdd,1=Internal reference
		self.VRANGES=[[ -3.3e-3,0],[0.,3.3],[-3.3,3.3],[-5.,5.]]
		self.VtoCode=[]
		for a in self.VRANGES:
			slope = (a[1]-a[0])
			intercept = a[0]
			self.VtoCode.append(np.poly1d([4095./slope,-4095.*intercept/slope ]))
		print (self.VtoCode)

	def setVoltage(self,chan,v):
		chanMaps={'PCS':0,'PVS3':0,'PVS2':2,'PVS1':3}
		dacChan = chanMaps[chan]
		chan = ['PCS','PVS3','PVS2','PVS1'].index(chan)
		R=self.VtoCode[chan]
		v = int(R(v))
		self.__setRawVoltage__(dacChan,v)
		R=self.VRANGES[chan]
		return (R[1]-R[0])*v/4095.+R[0]

	def __setRawVoltage__(self,chan,v,ADD_CALIBRATION=False):
		self.H.__sendByte__(DAC) #DAC write coming through.(MCP4922)
		if(ADD_CALIBRATION):self.H.__sendByte__(SET_CALIBRATED_DAC)
		else:self.H.__sendByte__(SET_DAC)
		self.H.__sendByte__(self.addr<<1)	#I2C address
		self.H.__sendByte__(chan)		#DAC channel
		self.H.__sendInt__((self.VREFS[chan] << 15) | (self.SWITCHEDOFF[chan] << 13) | (1 << 12) | v )
		#print (chan,hex((self.VREFS[chan] << 15) | (self.SWITCHEDOFF[chan] << 13) | (1 << 12) | v ))
		if(ADD_CALIBRATION):
			val = self.H.__getInt__()
			#print ('val, correction: ',v,val-v)
		else: pass#print (v)
		self.H.__get_ack__()
		if chan==0:chan=1   #pvs3=pcs=DAC channel 1
		R=self.VRANGES[chan]
		#print ('code',self.VtoCode[chan]((R[1]-R[0])*v/4095.+R[0]))
		return (R[1]-R[0])*v/4095.+R[0]

	def __writeall__(self,v1,v2,v3,v4):
		self.I2C.start(self.addr,0)
		self.I2C.send((v1>>8)&0xF )
		self.I2C.send(v1&0xFF)
		self.I2C.send((v2>>8)&0xF )
		self.I2C.send(v2&0xFF)
		self.I2C.send((v3>>8)&0xF )
		self.I2C.send(v3&0xFF)
		self.I2C.send((v4>>8)&0xF )
		self.I2C.send(v4&0xFF)
		self.I2C.stop()

	def stat(self):
		self.I2C.start(self.addr,0)
		self.I2C.send(0x0) #read raw values starting from address
		self.I2C.restart(self.addr,1)
		vals=self.I2C.read(24)
		self.I2C.stop()
		print (vals)


