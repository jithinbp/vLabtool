'''
Scripts that will be installed to /usr/local/bin, and can be run directly from a shell.

current list

*vLabtool-scope*
	An oscilloscope+logic analyzer utility that also has various control widgets
	
*vLabtool-stream*
	A utility that continuously fetches results and plots them
	

*vLabtool-sensorDemo*
	Plots values from plugged in I2C sensors
	
*vLabtool-bodePlots*
	Allows you to sweep the output of the waveform generator and simultaneously
	digitize two channels of the oscilloscope.  Connect these to the input and output
	of a filter or any other circuit to obtain plots of its frequency dependence.

*vLabtool-console*
    	An embedded iPython console and a PyQtGraph widget.
    	Use it to try out small bits of code, and also plot values easily
    	
*vLabtool-transientRLC*
	obtain the transient response of a series LC circuit.
	Connect an inductor and capacitor in series.
	connect one end to SQR3, the other to ground ,and monitor the midpoint with CH1.
	
	
*vLabtool-diodeIV*
	Obtain the IV characteristics of diodes

*vLabtool-transistorCE*
	Commmon emitter characteristics of transistors

*vLabtool-wirelessDemo*
	This App allows data acquisition from sensors connected to wireless nodes, and subsequent visualization.
	It autodetects wireless nodes, as well as the sensors plugged into them

*vLabtool-AccelerometerDemo*
	uses an MPU6050(accelerometer+gyroscope) plugged into the I2C port to control your mouse cursor.
	requires PyMouse installed	

		sudo easy_install PyMouse

	
	


'''
