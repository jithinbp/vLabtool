# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vLabtool/templates/stream.ui'
#
# Created: Mon Aug 10 23:52:02 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(276, 420)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cmdlist = QtGui.QComboBox(Form)
        self.cmdlist.setMinimumSize(QtCore.QSize(250, 0))
        self.cmdlist.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.cmdlist.setEditable(True)
        self.cmdlist.setObjectName(_fromUtf8("cmdlist"))
        self.cmdlist.addItem(_fromUtf8(""))
        self.cmdlist.addItem(_fromUtf8(""))
        self.cmdlist.addItem(_fromUtf8(""))
        self.cmdlist.addItem(_fromUtf8(""))
        self.cmdlist.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.cmdlist)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lastReading = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lastReading.setFont(font)
        self.lastReading.setAlignment(QtCore.Qt.AlignCenter)
        self.lastReading.setObjectName(_fromUtf8("lastReading"))
        self.verticalLayout.addWidget(self.lastReading)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.stream)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdlist.setItemText(0, QtGui.QApplication.translate("Form", "get_average_voltage(\'CH1\')", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdlist.setItemText(1, QtGui.QApplication.translate("Form", "get_freq(\'ID1\')", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdlist.setItemText(2, QtGui.QApplication.translate("Form", "get_high_freq(\'ID1\')", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdlist.setItemText(3, QtGui.QApplication.translate("Form", "DutyCycle(\'ID1\')[1]", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdlist.setItemText(4, QtGui.QApplication.translate("Form", "MeasureInterval(\'ID1\',\'ID2\',\'rising\',\'rising\')", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.lastReading.setText(QtGui.QApplication.translate("Form", "Result", None, QtGui.QApplication.UnicodeUTF8))

