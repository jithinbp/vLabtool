from numpy import int16
class MPU6050():
	GYRO_CONFIG = 0x1B
	ACCEL_CONFIG = 0x1C
	GYRO_SCALING= [131,65.5,32.8,16.4]
	ACCEL_SCALING=[16384,8192,4096,2048]
	AR=3
	GR=3
	NUMPLOTS=7
	def __init__(self,I2C):
		self.I2C=I2C
		self.ADDRESS = 0x68
		self.name = 'Accel/gyro'
		self.params={'powerUp':['Go'],'setGyroRange':[250,500,1000,2000],'setAccelRange':[2,4,8,16]}
		self.setGyroRange(2000)
		self.setAccelRange(16)
		'''
		try:
			self.I2C.configI2C(400e3)
		except:
			pass
		'''
		self.powerUp(True)

	def getVals(self,addr,bytes):
		vals = self.I2C.readBulk(self.ADDRESS,addr,bytes) 
		return vals

	def powerUp(self,x):
		self.I2C.writeBulk(self.ADDRESS,[0x6B,0])

	def setGyroRange(self,rs):
		self.GR=self.params['setGyroRange'].index(rs)
		self.I2C.writeBulk(self.ADDRESS,[self.GYRO_CONFIG,self.GR<<3])
		
	def setAccelRange(self,rs):
		self.AR=self.params['setAccelRange'].index(rs)
		self.I2C.writeBulk(self.ADDRESS,[self.ACCEL_CONFIG,self.AR<<3])

	def getRaw(self):
		'''
		This method must be defined if you want GUIs to use this class to generate 
		plots on the fly.
		It must return a set of different values read from the sensor. such as X,Y,Z acceleration.
		The length of this list must not change, and must be defined in the variable NUMPLOTS.
		
		GUIs will generate as many plots, and the data returned from this method will be appended appropriately
		'''
		vals=self.getVals(0x3B,14)
		if vals:
			if len(vals)==14:
				raw=[0]*7
				for a in range(3):raw[a] = 1.*int16(vals[a*2]<<8|vals[a*2+1])/self.ACCEL_SCALING[self.AR]
				for a in range(4,7):raw[a] = 1.*int16(vals[a*2]<<8|vals[a*2+1])/self.GYRO_SCALING[self.GR]
				raw[3] = int16(vals[6]<<8|vals[7])/340. + 36.53
				return raw
			else:
				return False
		else:
			return False

	def getAccel(self):
		vals=self.getVals(0x3B,6)
		ax=int16(vals[0]<<8|vals[1])
		ay=int16(vals[2]<<8|vals[3])
		az=int16(vals[4]<<8|vals[5])
		return [ax/65535.,ay/65535.,az/65535.]

	def getTemp(self):
		vals=self.getVals(0x41,6)
		t=int16(vals[0]<<8|vals[1])
		return t/65535.

	def getGyro(self):
		vals=self.getVals(0x43,6)
		ax=int16(vals[0]<<8|vals[1])
		ay=int16(vals[2]<<8|vals[3])
		az=int16(vals[4]<<8|vals[5])
		return [ax/65535.,ay/65535.,az/65535.]
		
