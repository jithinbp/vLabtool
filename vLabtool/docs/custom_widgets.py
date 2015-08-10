"""
These widgets will be used by the Experiment framework

"""
import sip,os

os.environ['QT_API'] = 'pyqt'
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)
# Import the core and GUI elements of Qt
from PyQt4.QtGui  import *
from PyQt4.QtCore import *

import interface

from widgets.sliding import Ui_Form as Ui_Sliding
from widgets.clicking import Ui_Form as Ui_Clicking
from widgets.clickingOptions import Ui_Form as Ui_ClickingOptions

class CustomWidgets:
	parent=None
	def __init__(self):
		print "widgets imported"
		self.I=interface.Interface()
	

	def newWidget(self,widget_type,**args):
			b=widget_type(**args)
			if(args.has_key('object_name')): b.setObjectName(args.get('object_name'))
			if(args.has_key('text')): b.setText(args.get('text'))
			if(args.has_key('items')):
				for a in args.get('items'): b.addItem(a)
			self.updateWidgetBay(b)
			return b

	def assignCommand(self,widget,signal,slot,*args):
			buttonCallback = functools.partial(slot,*args)
			QObject.connect(widget, SIGNAL(signal), buttonCallback)

	class sineHandler(QFrame,Ui_Sliding):
		def __init__(self,chan):
			super(CustomWidgets.sineHandler, self).__init__()
			#QFrame.__init__(self)
			#Ui_Sliding.__init__(self)
			self.I=interface.Interface()
			self.setupUi(self)
			self.name=['SINE1','SINE2'][chan-1]
			self.label.setText(self.name)
			self.chan=chan
			self.slider.setMinimum(0)
			self.slider.setMaximum(500000)
		def setValue(self,val):
			self.label.setText(self.name+':'+str(val)+' Hz')
			if self.chan==1:self.I.set_sine1(val)
			elif self.chan==2:self.I.set_sine2(val)

	def widget_sine1(self):
		self.updateWidgetBay(self.sineHandler(1))

	def widget_sine2(self):
		self.updateWidgetBay(self.sineHandler(2))

	class gainHandler(QFrame,Ui_Sliding):
		def __init__(self,chan,alternate_name=None):
			super(CustomWidgets.gainHandler, self).__init__()
			self.I=interface.Interface()
			self.setupUi(self)
			self.slider.setMinimum(0)
			self.slider.setMaximum(7)
			self.gaintxt=['1x','2x','4x','5x','8x','10x','16x','32x']
			self.name=chan
			if alternate_name:
				self.labeltxt=alternate_name
			else:
				self.labeltxt=chan
			self.label.setText(self.labeltxt)
		def setValue(self,val):
			self.label.setText(self.labeltxt+':'+self.gaintxt[val])
			self.I.set_gain(self.name,val)
			
	def widget_ch1(self):
		self.updateWidgetBay(self.gainHandler('CH1'))
	def widget_ch2(self):
		self.updateWidgetBay(self.gainHandler('CH2'))
	def widget_ch3(self):
		self.updateWidgetBay(self.gainHandler('CH3'))
	def widget_ch4(self):
		self.updateWidgetBay(self.gainHandler('CH4'))
	def widget_ch5(self):
		self.updateWidgetBay(self.gainHandler('CH5','CH5-CH9,PCS'))


	class voltHandler(QFrame,Ui_Clicking):
		def __init__(self,chan):
			super(CustomWidgets.voltHandler, self).__init__()
			#QFrame.__init__(self)
			#Ui_Sliding.__init__(self)
			self.I=interface.Interface()
			self.setupUi(self)
			self.name='READ '+chan
			self.button.setText(self.name)
			self.chan=chan
		def clicked(self):
			val = self.I.get_average_voltage(self.chan)
			self.label.setText('%.3f V'%(val))

	def widget_volt1(self):
		self.updateWidgetBay(self.voltHandler('CH1'))
	def widget_volt2(self):
		self.updateWidgetBay(self.voltHandler('CH2'))
	def widget_volt3(self):
		self.updateWidgetBay(self.voltHandler('CH3'))
	def widget_volt4(self):
		self.updateWidgetBay(self.voltHandler('CH4'))
	def widget_volt5(self):
		self.updateWidgetBay(self.voltHandler('CH5'))


	class voltAllHandler(QFrame,Ui_ClickingOptions):
		def __init__(self):
			super(CustomWidgets.voltAllHandler, self).__init__()
			#QFrame.__init__(self)
			#Ui_Sliding.__init__(self)
			self.I=interface.Interface()
			self.setupUi(self)
			self.names=['CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','CH9','5V','9V','IN1','SEN']
			self.button.setText('Read')
			self.items.addItems(self.names)

		def clicked(self):
			val = self.I.get_average_voltage(self.items.currentText())
			self.label.setText('%.3f V'%(val))

	def widget_voltAll(self):
		self.updateWidgetBay(self.voltAllHandler())


	def widget_inductance(self):
		class Handler(QFrame,Ui_Clicking):
			def __init__(self):
				super(Handler, self).__init__()
				self.I=interface.Interface()
				self.setupUi(self)
				self.button.setText('INDUCTANCE')
			def clicked(self):
				val = self.I.get_inductance()
				self.label.setText('%.3f'%(val))

		self.updateWidgetBay(Handler())

	class timingHandler(QFrame,Ui_ClickingOptions):
		def __init__(self,cmd):
			super(CustomWidgets.timingHandler, self).__init__()
			#QFrame.__init__(self)
			#Ui_Sliding.__init__(self)
			self.I=interface.Interface()
			self.setupUi(self)
			self.cmd = getattr(self.I,cmd)
			self.cmdname=cmd
			self.button.setText(cmd)
			self.items.addItems(['ID1','ID2','ID3','ID4','CH4'])

		def clicked(self):
			val = self.cmd(self.items.currentText())
			if self.cmdname=='duty_cycle':
				if(val[0]!=-1):p=100*val[1]/val[0]
				else: p=0
				self.label.setText(' %.2f %%'%(p))
			elif 'time' in self.cmdname:self.label.setText('%.2e S'%(val))
			else:self.label.setText('%.1f Hz'%(val))

	def widget_freq(self):
		self.updateWidgetBay(self.timingHandler('get_freq'))

	def widget_high_freq(self):
		self.updateWidgetBay(self.timingHandler('get_high_freq'))

	def widget_f2ftime(self):
		self.updateWidgetBay(self.timingHandler('f2f_time'))

	def widget_r2rtime(self):
		self.updateWidgetBay(self.timingHandler('r2r_time'))

	def widget_dutycycle(self):
		self.updateWidgetBay(self.timingHandler('duty_cycle'))

	def widget_pulse(self):
		self.updateWidgetBay(self.timingHandler('pulse_time'))

	class sourceHandler(QFrame,Ui_Sliding):
		def __init__(self,name):
			super(CustomWidgets.sourceHandler, self).__init__()
			self.I=interface.Interface()
			self.setupUi(self)
			self.name=name
			if name=='pvs1':
				self.slider.setRange(0,4095)
			if name=='pvs2':
				self.slider.setRange(0,4095)
			elif name=='pvs3':
				self.slider.setRange(0,31)
			elif name=='pcs':
				self.slider.setRange(0,31)

		def setValue(self,val):
			if self.name=='pvs1':
				retval=self.I.set_pvs1(val*10./4095 - 5)
			elif self.name=='pvs2':
				retval=self.I.set_pvs2(val*3.3/4095)
			elif self.name=='pvs3':
				retval=self.I.set_pvs3(val*6.6/31 - 3.3)
			elif self.name=='pcs':
				retval=self.I.set_pcs(val*3.3/31)

			self.label.setText(self.name+': %.3f'%(retval))

	def widget_pvs1(self):
		self.updateWidgetBay(self.sourceHandler('pvs1'))
	def widget_pvs2(self):
		self.updateWidgetBay(self.sourceHandler('pvs2'))
	def widget_pvs3(self):
		self.updateWidgetBay(self.sourceHandler('pvs3'))
	def widget_pcs(self):
		self.updateWidgetBay(self.sourceHandler('pcs'))




