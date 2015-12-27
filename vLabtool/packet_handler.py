from __future__ import print_function

from vLabtool.commands_proto import *
import serial

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Handler(object):
        __metaclass__ = Singleton
        def __init__(self,timeout=1.0,**kwargs):
            self.burstBuffer=b''
            self.loadBurst=False
            self.inputQueueSize=0
            self.BASE_PORT_NAME = "/dev/ttyACM"
            self.timeout=timeout
            self.version_string=b''
            self.connected=False
            if 'port' in kwargs:
                self.portname=kwargs.get('port',None)
                if not self.portname:
                    print ('device not found',self.portname)
                    sys.exit(1)
                self.fd = serial.Serial(self.portname, 9600, stopbits=1, timeout = 0.02)
                self.fd.read(100)
                self.fd = serial.Serial(self.portname, 1000000, stopbits=1, timeout = 1.0)
                if(self.fd.inWaiting()):
                    self.fd.read(1000)
                    self.fd.flush()
                version = self.get_version(self.fd)
                print ('Connected to device at ',self.portname,' ,Version:',version)
                self.connected=True
                self.version_string=version
                return
            else:	#Scan and pick a port
                for a in range(10):
                    try:
                        self.fd = serial.Serial(self.BASE_PORT_NAME+str(a), 9600, stopbits=1, timeout = 0.01)
                        #self.fd.read(100)
                        self.fd.close()
                        self.fd = serial.Serial(self.BASE_PORT_NAME+str(a), 1000000, stopbits=1, timeout = 0.2)
                        self.portname=self.BASE_PORT_NAME+str(a)
                        self.fd.read(1000)
                        self.fd.flush()
                        version = self.get_version(self.fd)
                        self.version_string=version
                        print (version,self.portname)
                        if(version[:3]==b'LTS'):
                            print ('Connected to device at ',self.portname,' ,Version:',version)
                            self.fd.setTimeout(1.)
                            self.connected=True
                            break
                        print (self.BASE_PORT_NAME+str(a)+' .yes.',version)
                    except IOError:
                            print (self.BASE_PORT_NAME+str(a)+' .no.')
                            pass
            if not self.connected:
                    print ('Device not found')

        def get_version(self,fd):
            fd.write(COMMON)
            fd.write(GET_VERSION)
            x=fd.read(100)
            return x

        def reconnect(self):
            try:
                self.fd = serial.Serial(self.portname, 9600, stopbits=1, timeout = 0.1)
                self.fd.close()
                time.sleep(0.2)
                self.fd = serial.Serial(self.portname, 1000000, stopbits=1, timeout = self.timeout)
                print ('connected TestBench')
            except serial.SerialException as ex:
                print ("failed to connect. Check device connections ,Or\nls /dev/TestBench\nOr, check if symlink has been created in /etc/udev/rules.d/proto.rules for the relevant Vid,Pid")
                sys.exit(1)

            if(self.fd.inWaiting()):
                self.fd.read(1000)
                self.fd.flush()

        def __del__(self):
            print ('closing port')
            try:self.fd.close()
            except: pass

        def __get_ack__(self):
            """
            fetches the response byte
             1 SUCCESS
             2 ARGUMENT_ERROR
             3 FAILED
            used as a handshake
            """
            if not self.loadBurst:
                x=self.fd.read(1)
            else:
                self.inputQueueSize+=1
                return 1
            return Byte.unpack(x)[0]

        def __sendInt__(self,val):
            """
            transmits an integer packaged as two characters
            :params int val: int to send
            """
            if not self.loadBurst:self.fd.write(InttoString(val))
            else: self.burstBuffer+=InttoString(val)

        def __sendByte__(self,val):
            """
            transmits a BYTE
            val - byte or numeric value to send
            """
            if(type(val)==int):
                if not self.loadBurst:self.fd.write(Byte.pack(val))
                else:self.burstBuffer+=Byte.pack(val)
            else:
                assert type(val)==type(b" ")
                if not self.loadBurst:self.fd.write(val)
                else:self.burstBuffer+=val

        def __getByte__(self):
            """
            reads a byte from the serial port and returns it as a number
            """
            ss=self.fd.read(1)
            if len(ss): return Byte.unpack(ss)[0]
            else:
                print ('byte communication error.',time.ctime())
                #return False
                sys.exit(1)
	
        def __getInt__(self):
            """
            reads two bytes from the serial port and
            returns an integer after combining them
            """
            ss = self.fd.read(2)
            # if len(ss)==2: return ord(ss[0])|(ord(ss[1])<<8)
            if len(ss)==2: return struct.unpack("<H", ss)[0]
            else:
                print ('int communication error.',time.ctime())
                #return False
                sys.exit(1)

        def __getLong__(self):
            """
            reads four bytes.
            returns long
            """
            ss = self.fd.read(4)
            # if len(ss)==4: return ord(ss[0])|(ord(ss[1])<<8)|(ord(ss[2])<<16)|(ord(ss[3])<<24)
            if len(ss)==4: return struct.unpack("<I",ss)[0]
            else:
                print ('.')
                return -1


        def sendBurst(self):
            """
            Transmits the commands stored in the burstBuffer.
            empties input buffer
            empties the burstBuffer.

            The following example initiates the capture routine and sets OD1 HIGH immediately.

            It is used by the Transient response experiment where the input needs to be toggled soon
            after the oscilloscope has been started.

            >>> I.loadBurst=True
            >>> I.capture_traces(4,800,2)
            >>> I.set_state(I.OD1,I.HIGH)
            >>> I.sendBurst()


            """
            print ([Byte.unpack(a)[0] for a in self.burstBuffer], self.inputQueueSize)
            self.fd.write(self.burstBuffer)
            self.burstBuffer=b''
            self.loadBurst=False
            acks=self.fd.read(int(self.inputQueueSize))
            self.inputQueueSize=0
            return [Byte.unpack(a)[0] for a in acks]

        def send_char(self,c):
            """
            Relays a character through the second UART(9-bit mode)

            ==============	============================================================================================
            **Arguments**
            ==============	============================================================================================
            c				value to transmit
            ==============	============================================================================================

            :return: nothing
            """
            self.__sendByte__(UART_2)
            self.__sendByte__(SEND_CHAR)
            self.__sendByte__(c)
            self.__get_ack__()
