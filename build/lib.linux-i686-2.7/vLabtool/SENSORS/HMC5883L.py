from numpy import int16
class HMC5883L():
	CONFA=0x00
	CONFB=0x01
	MODE=0x02
	STATUS=0x09
	
	#--------CONFA register bits. 0x00-----------
	samplesToAverage=0
	samplesToAverage_choices=[1,2,4,8]
	
	dataOutputRate=6
	dataOutputRate_choices=[0.75,1.5,3,7.5,15,30,75]
	
	measurementConf=0
	
	#--------CONFB register bits. 0x01-----------
	gainValue = 7 #least sensitive
	gain_choices = [8,7,6,5,4,3,2,1]
	scaling=[1370.,1090.,820.,660.,440.,390.,330.,230.]
	
	#--------------Parameters--------------------
	#This must be defined in order to let GUIs automatically create menus
	#for changing various options of this sensor
	#It's a dictionary of the string represetations of functions matched with an array
	#of options that each one can accept
	params={	'init':['Now'],
	'setSamplesToAverage':samplesToAverage_choices,
	'setDataOutputRate':dataOutputRate_choices,
	'setGain':gain_choices,
	}
	
	NUMPLOTS=3	
	def __init__(self,I2C):
		self.I2C=I2C
		self.ADDRESS = 0x1E
		self.name = 'Magnetometer'
		'''
		try:
			print 'switching baud to 400k'
			self.I2C.configI2C(400e3)
		except:
			print 'FAILED TO CHANGE BAUD RATE'
		'''
		self.init('')

	def init(self,dummy_variable_to_circumvent_framework_limitation):
		self.__writeCONFA__()
		self.__writeCONFB__()
		self.I2C.writeBulk(self.ADDRESS,[self.MODE,0]) #enable continuous measurement mode

	def __writeCONFB__(self):
		self.I2C.writeBulk(self.ADDRESS,[self.CONFB,self.gainValue<<5]) #set gain

	def __writeCONFA__(self):
		self.I2C.writeBulk(self.ADDRESS,[self.CONFA,(self.dataOutputRate<<2)|(self.samplesToAverage<<5)|(self.measurementConf)])
		
	def setSamplesToAverage(self,num):
		self.samplesToAverage=self.samplesToAverage_choices.index(num)
		self.__writeCONFA__()
	
	def setDataOutputRate(self,rate):
		self.dataOutputRate=self.dataOutputRate_choices.index(rate)
		self.__writeCONFA__()
	
	def setGain(self,gain):
		self.gainValue = self.gain_choices.index(gain)
		self.__writeCONFB__()
	
	def getVals(self,addr,bytes):
		vals = self.I2C.readBulk(self.ADDRESS,addr,bytes) 
		return vals
	
	def getRaw(self):
		vals=self.getVals(0x03,6)
		if vals:
			if len(vals)==6:
				return [int16(vals[a*2]<<8|vals[a*2+1])/self.scaling[self.gainValue] for a in range(3)]
			else:
				return False
		else:
			return False
		
