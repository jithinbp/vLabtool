from commands_proto import *

class I2C():
	"""
	Methods to interact with the I2C port. An instance of Labtools.Packet_Handler must be passed to the init function
	
	
	Example::  Read Values from an HMC5883L 3-axis Magnetometer(compass) [GY-273 sensor] connected to the I2C port
		>>> ADDRESS = 0x1E
		>>> from Labtools import interface
		>>> I = interface.Interface() 
		>>> # Alternately, you may skip using I2C as a child instance of Interface, 
		>>> # and instead use I2C=Labtools.I2C_class.I2C(Labtools.packet_handler.Handler())
		
		>>> I.I2C.bulkWrite(self.ADDRESS,[0x01,0<<5]) # writing to 0x1E, set gain(0x01) to smallest(0)

		>>> I.I2C.bulkWrite(self.ADDRESS,[0x02,0]) # writing to 0x1E, set mode conf(0x02), continuous measurement(0)

		>>> vals = I.I2C.bulkRead(self.ADDRESS,addr,6) # read 6 bytes from addr register on I2C device located at ADDRESS
			
		>>> from numpy import int16
		>>> x=int16((vals[0]<<8)|vals[1])	#conversion to signed datatype
		>>> y=int16((vals[2]<<8)|vals[3])
		>>> z=int16((vals[4]<<8)|vals[5])
		>>> print x,y,z
	
	"""

	def __init__(self,H):
		self.H = H
		from vLabtool import sensorlist
		self.SENSORS=sensorlist.sensors

	def init(self):
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_INIT)
		self.H.__get_ack__()

	def enable_smbus(self):
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_ENABLE_SMBUS)
		self.H.__get_ack__()

	def pullSCLLow(self,uS):
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_PULLDOWN_SCL)
		self.H.__sendInt__(uS)
		self.H.__get_ack__()
		
		 
	def config(self,freq):
		"""
		Sets frequency for I2C transactions
		
		================	============================================================================================
		**Arguments** 
		================	============================================================================================
		freq			I2C frequency
		================	============================================================================================
		"""
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_CONFIG)
		#freq=1/((BRGVAL+1.0)/64e6+1.0/1e7)
		BRGVAL=int( (1./freq-1./1e7)*64e6-1 )
		if BRGVAL>511:
			BRGVAL=511
			print 'Frequency too low. Setting to :',1/((BRGVAL+1.0)/64e6+1.0/1e7)
		self.H.__sendInt__(BRGVAL) 
		self.H.__get_ack__()

	def start(self,address,rw):
		"""
		Initiates I2C transfer to address via the I2C port
		
		================	============================================================================================
		**Arguments** 
		================	============================================================================================
		address				I2C slave address
		rw					Read/write.
							* 0 for writing
							* 1 for reading.
		================	============================================================================================
		"""
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_START)
		self.H.__sendByte__(((address<<1)|rw)&0xFF) # address
		return self.H.__get_ack__()>>4

	def stop(self):
		"""
		stops I2C transfer
		
		:return: Nothing
		"""
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_STOP)
		self.H.__get_ack__()

	def wait(self):
		"""
		wait for I2C

		:return: Nothing
		"""
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_WAIT)
		self.H.__get_ack__()

	def send(self,data):
		"""
		SENDS data over I2C.
		The I2C bus needs to be initialized and set to the correct slave address first.
		Use I2C.start(address) for this.
		
		================	============================================================================================
		**Arguments** 
		================	============================================================================================
		data				Sends data byte over I2C bus
		================	============================================================================================

		:return: Nothing
		"""
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_SEND)
		self.H.__sendByte__(data)		 #data byte
		return self.H.__get_ack__()>>4
		
	def send_burst(self,data):
		"""
		SENDS data over I2C. The function does not wait for the I2C to finish before returning.
		It is used for sending large packets quickly.
		The I2C bus needs to be initialized and set to the correct slave address first.
		Use start(address) for this.

		================	============================================================================================
		**Arguments** 
		================	============================================================================================
		data				Sends data byte over I2C bus
		================	============================================================================================

		:return: Nothing
		"""
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_SEND_BURST)
		self.H.__sendByte__(data)		 #data byte
		#No handshake. for the sake of speed. e.g. loading a frame buffer onto an I2C display such as ssd1306

	def restart(self,address,rw):
		"""
		Initiates I2C transfer to address

		================	============================================================================================
		**Arguments** 
		================	============================================================================================
		address				I2C slave address
		rw					Read/write.
							* 0 for writing
							* 1 for reading.
		================	============================================================================================

		"""
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_RESTART)
		self.H.__sendByte__(((address<<1)|rw)&0xFF) # address
		return self.H.__get_ack__()>>4

	def simpleRead(self,addr,numbytes):
		self.start(addr,1)
		vals=self.read(numbytes)
		return vals

	def read(self,length):
		"""
		Reads a fixed number of data bytes from I2C device. Fetches length-1 bytes with acknowledge bits for each, +1 byte
		with Nack.

		================	============================================================================================
		**Arguments** 
		================	============================================================================================
		length				number of bytes to read from I2C bus
		================	============================================================================================
		"""
		data=[]
		for a in range(length-1):
			self.H.__sendByte__(I2C_HEADER)
			self.H.__sendByte__(I2C_READ_MORE)
			data.append(self.H.__getByte__())
			self.H.__get_ack__()
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_READ_END)
		data.append(self.H.__getByte__())
		self.H.__get_ack__()
		return data

	def read_repeat(self):
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_READ_MORE)
		val=self.H.__getByte__()
		self.H.__get_ack__()
		return val

	def read_end(self):
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_READ_END)
		val=self.H.__getByte__()
		self.H.__get_ack__()
		return val


	def read_status(self):
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_STATUS)
		val=self.H.__getInt__()
		self.H.__get_ack__()
		return val


	def readBulk(self,device_address,register_address,bytes_to_read):
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_READ_BULK)
		self.H.__sendByte__(device_address)
		self.H.__sendByte__(register_address)
		self.H.__sendByte__(bytes_to_read)
		data=self.H.fd.read(bytes_to_read)
		self.H.__get_ack__()
		try:
			return [ord(a) for a in data]
		except:
			print 'Transaction failed'
			return False
		
	def writeBulk(self,device_address,bytestream):
		self.H.__sendByte__(I2C_HEADER)
		self.H.__sendByte__(I2C_WRITE_BULK)
		self.H.__sendByte__(device_address)
		self.H.__sendByte__(len(bytestream))
		for a in bytestream:
			self.H.__sendByte__(a)
		self.H.__get_ack__()

	def scan(self,frequency = 100000):
		self.config(frequency)
		addrs=[]
		n=0
		print 'Scanning addresses 0-127...'
		print 'Address','\t','Possible Devices'
		for a in range(0,128):
			x = self.start(a,0)
			if x&1 == 0:	#ACK received
				addrs.append(a)
				print hex(a),'\t\t',self.SENSORS.get(a,'None')
				n+=1
			self.stop()
		return addrs






