# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SLabtools/templates/exp5.ui'
#
# Created: Wed Jul 22 01:35:19 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(849, 479)
        MainWindow.setStyleSheet(_fromUtf8(" QPushButton{ background-image: url(:/images/bt_01_off.png);}\n"
" QPushButton:pressed {background-image:url(:/images/bt_01_on.png);}\n"
"QFrame{background-color: rgb(21, 107, 113);}\n"
"\n"
" QDockWidget {\n"
"     border: 1px solid lightgray;\n"
" }\n"
"\n"
" QDockWidget::title {\n"
"     text-align: left; /* align the text to the left */\n"
"     background: lightgray;\n"
"     padding-left: 5px;\n"
"    height:6px;\n"
" }\n"
"\n"
" QDockWidget::close-button, QDockWidget::float-button {\n"
"     border: 1px solid transparent;\n"
"     background: darkgray;\n"
"     padding: 0px;\n"
" }\n"
"\n"
" QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"     background: gray;\n"
" }\n"
"\n"
" QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"     padding: 1px -1px -1px 1px;\n"
" }\n"
"\n"
"QProgressBar {    border: 1px solid black;        text-align: top;\n"
"                padding: 1px;\n"
"                border-bottom-right-radius: 7px;\n"
"                border-bottom-left-radius: 7px;\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                stop: 0 #fff,\n"
"                stop: 0.4999 #eee,\n"
"                stop: 0.5 #ddd,\n"
"                stop: 1 #eee );\n"
"                width: 15px;\n"
"                }\n"
"\n"
"QProgressBar::chunk {\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                stop: 0 #78d,\n"
"                stop: 0.4999 #46a,\n"
"                stop: 0.5 #45a,\n"
"                stop: 1 #238 );\n"
"                border-bottom-right-radius: 7px;\n"
"                border-bottom-left-radius: 7px;\n"
"                border: 1px solid black;\n"
"                }\n"
"            \n"
"\n"
"border-color: rgb(29, 122, 162);\n"
""))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 847, 452))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graph_splitter = QtGui.QSplitter(self.scrollAreaWidgetContents_2)
        self.graph_splitter.setOrientation(QtCore.Qt.Vertical)
        self.graph_splitter.setObjectName(_fromUtf8("graph_splitter"))
        self.verticalLayout.addWidget(self.graph_splitter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 849, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuVoltmeters_2 = QtGui.QMenu(self.menuBar)
        self.menuVoltmeters_2.setObjectName(_fromUtf8("menuVoltmeters_2"))
        self.menuAmplifiers_2 = QtGui.QMenu(self.menuBar)
        self.menuAmplifiers_2.setObjectName(_fromUtf8("menuAmplifiers_2"))
        self.menuWaveform_Generators_2 = QtGui.QMenu(self.menuBar)
        self.menuWaveform_Generators_2.setObjectName(_fromUtf8("menuWaveform_Generators_2"))
        self.menuIV_sources = QtGui.QMenu(self.menuBar)
        self.menuIV_sources.setObjectName(_fromUtf8("menuIV_sources"))
        self.menuPassive_Elements = QtGui.QMenu(self.menuBar)
        self.menuPassive_Elements.setObjectName(_fromUtf8("menuPassive_Elements"))
        self.menuTiming = QtGui.QMenu(self.menuBar)
        self.menuTiming.setObjectName(_fromUtf8("menuTiming"))
        self.menuConsole = QtGui.QMenu(self.menuBar)
        self.menuConsole.setObjectName(_fromUtf8("menuConsole"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionAdd_Button = QtGui.QAction(MainWindow)
        self.actionAdd_Button.setObjectName(_fromUtf8("actionAdd_Button"))
        self.actionInsert_Console = QtGui.QAction(MainWindow)
        self.actionInsert_Console.setObjectName(_fromUtf8("actionInsert_Console"))
        self.actionDigital_outputs = QtGui.QAction(MainWindow)
        self.actionDigital_outputs.setObjectName(_fromUtf8("actionDigital_outputs"))
        self.actionCH1 = QtGui.QAction(MainWindow)
        self.actionCH1.setObjectName(_fromUtf8("actionCH1"))
        self.actionCH2 = QtGui.QAction(MainWindow)
        self.actionCH2.setObjectName(_fromUtf8("actionCH2"))
        self.actionCH3 = QtGui.QAction(MainWindow)
        self.actionCH3.setObjectName(_fromUtf8("actionCH3"))
        self.actionCH4 = QtGui.QAction(MainWindow)
        self.actionCH4.setObjectName(_fromUtf8("actionCH4"))
        self.actionCH5 = QtGui.QAction(MainWindow)
        self.actionCH5.setObjectName(_fromUtf8("actionCH5"))
        self.actionCH2meter = QtGui.QAction(MainWindow)
        self.actionCH2meter.setObjectName(_fromUtf8("actionCH2meter"))
        self.actionCH3meter = QtGui.QAction(MainWindow)
        self.actionCH3meter.setObjectName(_fromUtf8("actionCH3meter"))
        self.actionCH4meter = QtGui.QAction(MainWindow)
        self.actionCH4meter.setObjectName(_fromUtf8("actionCH4meter"))
        self.actionCH5meter = QtGui.QAction(MainWindow)
        self.actionCH5meter.setObjectName(_fromUtf8("actionCH5meter"))
        self.actionCH1meter = QtGui.QAction(MainWindow)
        self.actionCH1meter.setObjectName(_fromUtf8("actionCH1meter"))
        self.actionAll_of_Them = QtGui.QAction(MainWindow)
        self.actionAll_of_Them.setObjectName(_fromUtf8("actionAll_of_Them"))
        self.actionInductance = QtGui.QAction(MainWindow)
        self.actionInductance.setObjectName(_fromUtf8("actionInductance"))
        self.actionR2R_time = QtGui.QAction(MainWindow)
        self.actionR2R_time.setObjectName(_fromUtf8("actionR2R_time"))
        self.actionF2F_time = QtGui.QAction(MainWindow)
        self.actionF2F_time.setObjectName(_fromUtf8("actionF2F_time"))
        self.actionFrequency = QtGui.QAction(MainWindow)
        self.actionFrequency.setObjectName(_fromUtf8("actionFrequency"))
        self.actionPulse_Width = QtGui.QAction(MainWindow)
        self.actionPulse_Width.setObjectName(_fromUtf8("actionPulse_Width"))
        self.actionDuty_Cycle = QtGui.QAction(MainWindow)
        self.actionDuty_Cycle.setObjectName(_fromUtf8("actionDuty_Cycle"))
        self.actionHigh_Frequency = QtGui.QAction(MainWindow)
        self.actionHigh_Frequency.setObjectName(_fromUtf8("actionHigh_Frequency"))
        self.actionSineWave = QtGui.QAction(MainWindow)
        self.actionSineWave.setObjectName(_fromUtf8("actionSineWave"))
        self.actionPVS_1 = QtGui.QAction(MainWindow)
        self.actionPVS_1.setObjectName(_fromUtf8("actionPVS_1"))
        self.actionPVS_2 = QtGui.QAction(MainWindow)
        self.actionPVS_2.setObjectName(_fromUtf8("actionPVS_2"))
        self.actionPVS_3 = QtGui.QAction(MainWindow)
        self.actionPVS_3.setObjectName(_fromUtf8("actionPVS_3"))
        self.actionPCS = QtGui.QAction(MainWindow)
        self.actionPCS.setObjectName(_fromUtf8("actionPCS"))
        self.menuVoltmeters_2.addAction(self.actionCH1meter)
        self.menuVoltmeters_2.addAction(self.actionCH2meter)
        self.menuVoltmeters_2.addAction(self.actionCH3meter)
        self.menuVoltmeters_2.addAction(self.actionCH4meter)
        self.menuVoltmeters_2.addAction(self.actionCH5meter)
        self.menuVoltmeters_2.addAction(self.actionAll_of_Them)
        self.menuAmplifiers_2.addAction(self.actionCH1)
        self.menuAmplifiers_2.addAction(self.actionCH2)
        self.menuAmplifiers_2.addAction(self.actionCH3)
        self.menuAmplifiers_2.addAction(self.actionCH4)
        self.menuAmplifiers_2.addAction(self.actionCH5)
        self.menuWaveform_Generators_2.addAction(self.actionSineWave)
        self.menuIV_sources.addAction(self.actionPVS_1)
        self.menuIV_sources.addAction(self.actionPVS_2)
        self.menuIV_sources.addAction(self.actionPVS_3)
        self.menuIV_sources.addAction(self.actionPCS)
        self.menuPassive_Elements.addAction(self.actionInductance)
        self.menuTiming.addAction(self.actionFrequency)
        self.menuTiming.addAction(self.actionR2R_time)
        self.menuTiming.addAction(self.actionF2F_time)
        self.menuTiming.addAction(self.actionPulse_Width)
        self.menuTiming.addAction(self.actionDuty_Cycle)
        self.menuTiming.addAction(self.actionHigh_Frequency)
        self.menuConsole.addAction(self.actionInsert_Console)
        self.menuBar.addAction(self.menuVoltmeters_2.menuAction())
        self.menuBar.addAction(self.menuAmplifiers_2.menuAction())
        self.menuBar.addAction(self.menuWaveform_Generators_2.menuAction())
        self.menuBar.addAction(self.menuIV_sources.menuAction())
        self.menuBar.addAction(self.menuTiming.menuAction())
        self.menuBar.addAction(self.menuPassive_Elements.menuAction())
        self.menuBar.addAction(self.menuConsole.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionInsert_Console, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.addConsole)
        QtCore.QObject.connect(self.actionCH1, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_ch1)
        QtCore.QObject.connect(self.actionCH2, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_ch2)
        QtCore.QObject.connect(self.actionCH3, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_ch3)
        QtCore.QObject.connect(self.actionCH4, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_ch4)
        QtCore.QObject.connect(self.actionCH5, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_ch5)
        QtCore.QObject.connect(self.actionCH2meter, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_volt2)
        QtCore.QObject.connect(self.actionCH3meter, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_volt3)
        QtCore.QObject.connect(self.actionCH4meter, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_volt4)
        QtCore.QObject.connect(self.actionCH5meter, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_volt5)
        QtCore.QObject.connect(self.actionCH1meter, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_volt1)
        QtCore.QObject.connect(self.actionAll_of_Them, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_voltAll)
        QtCore.QObject.connect(self.actionSineWave, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_sine)
        QtCore.QObject.connect(self.actionInductance, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_inductance)
        QtCore.QObject.connect(self.actionFrequency, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_freq)
        QtCore.QObject.connect(self.actionHigh_Frequency, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_high_freq)
        QtCore.QObject.connect(self.actionR2R_time, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_r2rtime)
        QtCore.QObject.connect(self.actionF2F_time, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_f2ftime)
        QtCore.QObject.connect(self.actionPulse_Width, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_pulse)
        QtCore.QObject.connect(self.actionDuty_Cycle, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_dutycycle)
        QtCore.QObject.connect(self.actionPVS_1, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_pvs1)
        QtCore.QObject.connect(self.actionPVS_2, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_pvs2)
        QtCore.QObject.connect(self.actionPVS_3, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_pvs3)
        QtCore.QObject.connect(self.actionPCS, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.widget_pcs)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Experiments", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVoltmeters_2.setTitle(QtGui.QApplication.translate("MainWindow", "Voltmeters", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAmplifiers_2.setTitle(QtGui.QApplication.translate("MainWindow", "Amplifiers", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWaveform_Generators_2.setTitle(QtGui.QApplication.translate("MainWindow", "Waveform Generators", None, QtGui.QApplication.UnicodeUTF8))
        self.menuIV_sources.setTitle(QtGui.QApplication.translate("MainWindow", "IV sources", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPassive_Elements.setTitle(QtGui.QApplication.translate("MainWindow", "Passive Elements", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTiming.setTitle(QtGui.QApplication.translate("MainWindow", "Timing", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConsole.setTitle(QtGui.QApplication.translate("MainWindow", "Console!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Button.setText(QtGui.QApplication.translate("MainWindow", "Insert Console", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_Console.setText(QtGui.QApplication.translate("MainWindow", "Insert Console", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDigital_outputs.setText(QtGui.QApplication.translate("MainWindow", "digital outputs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH1.setText(QtGui.QApplication.translate("MainWindow", "CH1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH2.setText(QtGui.QApplication.translate("MainWindow", "CH2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH3.setText(QtGui.QApplication.translate("MainWindow", "CH3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH4.setText(QtGui.QApplication.translate("MainWindow", "CH4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH5.setText(QtGui.QApplication.translate("MainWindow", "Sensors (CH5-CH9,PCS)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH2meter.setText(QtGui.QApplication.translate("MainWindow", "CH2meter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH3meter.setText(QtGui.QApplication.translate("MainWindow", "CH3meter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH4meter.setText(QtGui.QApplication.translate("MainWindow", "CH4meter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH5meter.setText(QtGui.QApplication.translate("MainWindow", "CH5meter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCH1meter.setText(QtGui.QApplication.translate("MainWindow", "CH1meter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAll_of_Them.setText(QtGui.QApplication.translate("MainWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInductance.setText(QtGui.QApplication.translate("MainWindow", "Inductance", None, QtGui.QApplication.UnicodeUTF8))
        self.actionR2R_time.setText(QtGui.QApplication.translate("MainWindow", "R2R time", None, QtGui.QApplication.UnicodeUTF8))
        self.actionF2F_time.setText(QtGui.QApplication.translate("MainWindow", "F2F time", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrequency.setText(QtGui.QApplication.translate("MainWindow", "Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPulse_Width.setText(QtGui.QApplication.translate("MainWindow", "Pulse Width", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDuty_Cycle.setText(QtGui.QApplication.translate("MainWindow", "Duty Cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHigh_Frequency.setText(QtGui.QApplication.translate("MainWindow", "High Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSineWave.setText(QtGui.QApplication.translate("MainWindow", "sine wave", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPVS_1.setText(QtGui.QApplication.translate("MainWindow", "PVS 1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPVS_2.setText(QtGui.QApplication.translate("MainWindow", "PVS 2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPVS_3.setText(QtGui.QApplication.translate("MainWindow", "PVS 3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPCS.setText(QtGui.QApplication.translate("MainWindow", "PCS", None, QtGui.QApplication.UnicodeUTF8))

