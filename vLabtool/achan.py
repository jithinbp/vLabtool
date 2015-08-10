import numpy as np
TEN_BIT=10
TWELVE_BIT=12
print 'LOADING'
gains=[1,2,4,5,8,10,16,32]
'''
calfacs={}
try:			#Try and load data from a calibration file
	from calib_data import calibs
	print 'found calibs'
	print calibs.__file__
	for A in calibs.calibs:
		calfacs[A] = [np.poly1d(B) for B in calibs.calibs[A]]
except:			#Give up and use default calibration instead
	print 'Loading default calibration values'
	for n in range(2):
		calfacs['CH'+str(n+1)]=[np.poly1d([ 0,-33/1023./gains[a],16.5/gains[a]]) for a in range(8)] #calibrations for all gains , inv channel

	calfacs['CH3'] = [np.poly1d([0, -6.6/1023./gains[a], 3.3/gains[a] ]) for a in range(8)]
	for n in ['CH4','CH5','CH6','CH7']:
		calfacs[n] = [np.poly1d([0, 3.3/1023./gains[a], 0]) for a in range(8)]

calfacs['5V'] = [np.poly1d([0, 2*3.3/1023./gains[a], 0]) for a in range(8)] 
calfacs['I2V'] = [np.poly1d([0, 3.3/1023./gains[a], 0]) for a in range(8)]
calfacs['9V'] = [np.poly1d([0, 36.3/1023./gains[a], 0]) for a in range(8)] 
calfacs['V+'] = [np.poly1d([0, 36.3/1023./gains[a], 0]) for a in range(8)] 

calfacs['IN1']=[np.poly1d([0, 3.3/1023., 0])] #1 gain. normal channels
calfacs['SEN']=[np.poly1d([0, 3.3/1023., 0])] #1 gain. normal channels
calfacs['TEMP']=[np.poly1d([0, 3.3/1023., 0])] #1 gain. normal channels
calfacs['CAP']=[np.poly1d([0, 3.3/1023., 0])] #1 gain. normal channels
calfacs['AN2']=[np.poly1d([0, 3.3/1023., 0])] #1 gain. normal channels
calfacs['AN3']=[np.poly1d([0, 3.3/1023., 0])] #1 gain. normal channels
'''
#-----------------------Classes for input sources----------------------
allAnalogChannels = ['CH1','CH2','CH3','CH4','CH5','CH6','CH7','I2V','V+','SEN','CAP','AN2','AN3']

multiplexedChannels = ['CH1','I2V','CH3','CH4','CH5','CH6','CH7','V+']
bipolars = ['CH1','I2V','CH3']
unipolars = ['CH4','CH5','CH6','CH7',]
directInAnalogs = ['AN2','AN3','AN4','CAP','CAPCHARGE','SEN','5V']

inputRanges={'CH1':[16.5,-16.5],	#Specify inverted channels explicitly by reversing range!!!!!!!!!
'CH2':[16.5,-16.5],
'CH3':[-3.3,3.3],					#external gain control analog input
'I2V':[-3.3,3.3],					#connected to current to voltage convertor
'V+':[0,36.3],
'CH4':[0,3.3],'CH5':[0,3.3],'CH6':[0,3.3],'CH7':[0,3.3],
'SEN':[0,3.3],'CAP':[0,3.3],'AN2':[0,3.3],'AN3':[0,3.3]
}

picADCMultiplex={'CH2':0}
for a in multiplexedChannels: picADCMultiplex[a] = 1
for a in directInAnalogs: picADCMultiplex[a] = directInAnalogs.index(a)+2

class analogInputSource:
	gain_values=[1,2,4,5,8,10,16,32]
	offsetEnabled=False
	gainEnabled=False
	offsetCode=None
	offset=0.
	gain=None
	gainPGA=None
	MAX_DACVAL=4095
	multiplexSelection=None
	inverted=False
	inversion=1.
	calPoly10 = np.poly1d([0,3.3/1023,0.])
	calPoly12 = np.poly1d([0,3.3/4095,0.])
	calibrationReady=False
	defaultOffsetCode=0
	def __init__(self,name,**args):
		self.name = name			#The generic name of the input. like 'CH1', 'IN1' etc
		self.CHOSA = picADCMultiplex[self.name]
		self.adc_shifts=[]
		self.polynomials={}

		if name in multiplexedChannels:
			self.multiplexSelection = multiplexedChannels.index(name)
		self.R=inputRanges[name]
		
		if self.R[1]-self.R[0] < 0:
			self.inverted=True
			self.inversion=-1

		self.scaling=1.
		if name=='CH2':
			self.gainEnabled=True
			self.gainPGA = 2
			self.gain=0		#This is not the gain factor. use self.gain_values[self.gain] to find that.
		elif name in multiplexedChannels:
			self.gainEnabled=True
			self.offsetEnabled=True
			self.offsetCode = 0
			self.defaultOffsetCode=0

			self.gainPGA = 1
			self.gain=0

			if	name in	bipolars:
				self.defaultOffsetCode=int(self.MAX_DACVAL/2)
				self.offsetCode=self.defaultOffsetCode
		else:
			pass


		self.gain=0
		self.regenerateCalibration()

	def getOffset(self):
		if self.offsetCode==None:return 0
		return self.offsetCode*(self.R[1]-self.R[0])/4095.+self.R[0]

	def setOffset(self,offset):
		if not	self.offsetEnabled:
			print 'Offset selection is not available on',self.name
			return False
		if not(min(self.R) <= offset <= max(self.R)):
			print 'Offset out of range ',self.R
			return False

		self.offsetCode=int(4095*(offset-self.R[0])/(self.R[1]-self.R[0]))

		#if self.inverted:self.offsetCode = 4095-self.offsetCode
		print 'setting offset',offset,self.offsetCode
		self.offset=offset
		self.regenerateCalibration()

	def setGain(self,g):
		if not	self.gainEnabled:
			print 'Analog gain is not available on',self.name
			return False
		self.gain=self.gain_values.index(g)
		self.regenerateCalibration()

	def inRange(self,val):
		v = self.voltToCode12(val)
		return (v>=0 and v<=4095)

	def __conservativeInRange__(self,val):
		v = self.voltToCode12(val)
		return (v>=50 and v<=4000)

	def loadCalibrationTable(self,table):
		self.adc_shifts = np.array(table)

	def loadPolynomials(self,polys):
		for a in range(len(polys)):
			epoly = [float(b) for b in polys[a]]
			self.polynomials[a] = np.poly1d(epoly)

	def regenerateCalibration(self):
		B=self.R[1]
		A=self.R[0]
		intercept = self.R[0]
		offset=self.getOffset()
		
		if self.gain!=None:
				gain = self.gain_values[self.gain]
				B = offset + 1.*(B-offset)/gain
				A = offset + 1.*(A-offset)/gain


		slope = B-A
		intercept = A
		if self.calibrationReady and ( (self.offsetCode==self.defaultOffsetCode) or self.offsetEnabled==False ) :
			self.calPoly10 = self.__cal10__
			self.calPoly12 = self.__cal12__
			
		else:
			self.calPoly10 = np.poly1d([0,slope/1023.,intercept])
			self.calPoly12 = np.poly1d([0,slope/4095.,intercept])

		self.voltToCode10 = np.poly1d([0,1023./slope,-1023*intercept/slope])
		self.voltToCode12 = np.poly1d([0,4095./slope,-4095*intercept/slope])


	def __cal12__(self,RAW):
		avg_shifts=(self.adc_shifts[np.int16(np.floor(RAW))]+self.adc_shifts[np.int16(np.ceil(RAW))])/2.
		RAW = RAW-4095*(avg_shifts/25e3 - 4e-3)/3.3
		return self.polynomials[self.gain](RAW)

	def __cal10__(self,RAW):
		RAW*=4095/1023.
		avg_shifts=(self.adc_shifts[np.int16(np.floor(RAW))]+self.adc_shifts[np.int16(np.ceil(RAW))])/2.
		RAW = RAW-4095*(avg_shifts/25e3 - 4e-3)/3.3
		return self.polynomials[self.gain](RAW)


'''
for a in ['CH1']:
	x=analogInputSource(a)
	print x.name,x.calPoly10#,calfacs[x.name][0]
	print 'CAL:',x.calPoly10(0),x.calPoly10(1023)
	x.setOffset(1.65)
	x.setGain(32)
	print x.name,x.calPoly10#,calfacs[x.name][0]
	print 'CAL:',x.calPoly10(0),x.calPoly10(1023)
'''
#---------------------------------------------------------------------



class analogAcquisitionChannel:
	'''
	This class takes care of oscilloscope data fetched from the device.
	Each instance may be linked to a particular input.
	Since only up to two channels may be captured at a time with the vLabtool, only two instances will be required
	
	Each instance will be linked to a particular inputSource instance by the capture routines.
	When data is requested , it will return after applying calibration and gain details
	stored in the selected inputSource
	'''
	def __init__(self,a):
		self.name=''
		self.gain=0
		self.channel=a
		self.channel_names=['CH1','CH2','CH3','CH4','CH5','CH6','CH7','I2V','5V','PCS','9V','IN1','SEN','TEMP']
		#REFERENCE VOLTAGE = 3.3 V
		self.calibration_ref196=1.#measured reference voltage/3.3
		self.resolution=TEN_BIT
		self.xaxis=np.zeros(10000)
		self.yaxis=np.zeros(10000)
		self.length=100
		self.timebase = 1.
		self.source = analogInputSource('CH1')

	def fix_value(self,val):
		#val[val>1020]=np.NaN
		#val[val<2]=np.NaN
		if self.resolution==TWELVE_BIT:return self.calibration_ref196*self.source.calPoly12(val)
		else:return self.calibration_ref196*self.source.calPoly10(val)

	def set_yval(self,pos,val):
		self.yaxis[pos] = self.fix_value(val)

	def set_xval(self,pos,val):
		self.xaxis[pos] = val

	def set_params(self,**keys):
		self.gain = keys.get('gain',self.gain)	
		self.name = keys.get('channel',self.channel)	
		self.source = keys.get('source',self.source)
		self.resolution = keys.get('resolution',self.resolution)	
		l = keys.get('length',self.length)	
		t = keys.get('timebase',self.timebase)
		if t != self.timebase or l != self.length:
			self.timebase = t
			self.length = l
			self.regenerate_xaxis()

	def regenerate_xaxis(self):
		for a in range(self.length): self.xaxis[a] = self.timebase*a

	def get_xaxis(self):
		return self.xaxis[:self.length]
	def get_yaxis(self):
		return self.yaxis[:self.length]

