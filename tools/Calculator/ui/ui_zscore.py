# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_zscore.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1203, 828)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1131, 741))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_card = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_card.setFont(font)
        self.tab_card.setObjectName("tab_card")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_card)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 1101, 691))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2008 = QtWidgets.QWidget()
        self.tab_2008.setObjectName("tab_2008")
        self.label_3 = QtWidgets.QLabel(self.tab_2008)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 51, 25))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2008)
        self.label_4.setGeometry(QtCore.QRect(130, 10, 51, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2008)
        self.label_5.setGeometry(QtCore.QRect(300, 10, 51, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2008)
        self.label_6.setGeometry(QtCore.QRect(190, 10, 41, 25))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2008)
        self.label_7.setGeometry(QtCore.QRect(480, 10, 51, 25))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2008)
        self.label_8.setGeometry(QtCore.QRect(370, 10, 41, 25))
        self.label_8.setObjectName("label_8")
        self.table_2008 = QtWidgets.QTableWidget(self.tab_2008)
        self.table_2008.setGeometry(QtCore.QRect(10, 50, 941, 611))
        self.table_2008.setObjectName("table_2008")
        self.table_2008.setColumnCount(0)
        self.table_2008.setRowCount(0)
        self.label_2008_bsa_formula = QtWidgets.QLabel(self.tab_2008)
        self.label_2008_bsa_formula.setGeometry(QtCore.QRect(540, 10, 411, 25))
        self.label_2008_bsa_formula.setObjectName("label_2008_bsa_formula")
        self.double_2008_height = QtWidgets.QDoubleSpinBox(self.tab_2008)
        self.double_2008_height.setGeometry(QtCore.QRect(70, 10, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.double_2008_height.setFont(font)
        self.double_2008_height.setStyleSheet("")
        self.double_2008_height.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.double_2008_height.setMaximum(99999.99)
        self.double_2008_height.setSingleStep(0.01)
        self.double_2008_height.setObjectName("double_2008_height")
        self.double_2008_weight = QtWidgets.QDoubleSpinBox(self.tab_2008)
        self.double_2008_weight.setGeometry(QtCore.QRect(240, 10, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.double_2008_weight.setFont(font)
        self.double_2008_weight.setStyleSheet("")
        self.double_2008_weight.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.double_2008_weight.setMaximum(99999.99)
        self.double_2008_weight.setSingleStep(0.01)
        self.double_2008_weight.setObjectName("double_2008_weight")
        self.double_2008_bsa = QtWidgets.QDoubleSpinBox(self.tab_2008)
        self.double_2008_bsa.setGeometry(QtCore.QRect(410, 10, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.double_2008_bsa.setFont(font)
        self.double_2008_bsa.setStyleSheet("")
        self.double_2008_bsa.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.double_2008_bsa.setMaximum(99999.99)
        self.double_2008_bsa.setSingleStep(0.01)
        self.double_2008_bsa.setObjectName("double_2008_bsa")
        self.tabWidget_2.addTab(self.tab_2008, "")
        self.tab_2013 = QtWidgets.QWidget()
        self.tab_2013.setObjectName("tab_2013")
        self.label_9 = QtWidgets.QLabel(self.tab_2013)
        self.label_9.setGeometry(QtCore.QRect(300, 10, 51, 25))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2013)
        self.label_10.setGeometry(QtCore.QRect(130, 10, 51, 25))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2013)
        self.label_11.setGeometry(QtCore.QRect(480, 10, 51, 25))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2013)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 51, 25))
        self.label_12.setObjectName("label_12")
        self.table_2013 = QtWidgets.QTableWidget(self.tab_2013)
        self.table_2013.setGeometry(QtCore.QRect(10, 50, 1081, 611))
        self.table_2013.setObjectName("table_2013")
        self.table_2013.setColumnCount(0)
        self.table_2013.setRowCount(0)
        self.label_2013_bsa_formula = QtWidgets.QLabel(self.tab_2013)
        self.label_2013_bsa_formula.setGeometry(QtCore.QRect(540, 10, 411, 25))
        self.label_2013_bsa_formula.setObjectName("label_2013_bsa_formula")
        self.label_13 = QtWidgets.QLabel(self.tab_2013)
        self.label_13.setGeometry(QtCore.QRect(370, 10, 51, 25))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2013)
        self.label_14.setGeometry(QtCore.QRect(190, 10, 51, 25))
        self.label_14.setObjectName("label_14")
        self.double_2013_height = QtWidgets.QDoubleSpinBox(self.tab_2013)
        self.double_2013_height.setGeometry(QtCore.QRect(70, 10, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.double_2013_height.setFont(font)
        self.double_2013_height.setStyleSheet("")
        self.double_2013_height.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.double_2013_height.setMaximum(99999.99)
        self.double_2013_height.setSingleStep(0.01)
        self.double_2013_height.setObjectName("double_2013_height")
        self.double_2013_weight = QtWidgets.QDoubleSpinBox(self.tab_2013)
        self.double_2013_weight.setGeometry(QtCore.QRect(240, 10, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.double_2013_weight.setFont(font)
        self.double_2013_weight.setStyleSheet("")
        self.double_2013_weight.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.double_2013_weight.setMaximum(99999.99)
        self.double_2013_weight.setSingleStep(0.01)
        self.double_2013_weight.setObjectName("double_2013_weight")
        self.double_2013_bsa = QtWidgets.QDoubleSpinBox(self.tab_2013)
        self.double_2013_bsa.setGeometry(QtCore.QRect(410, 10, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.double_2013_bsa.setFont(font)
        self.double_2013_bsa.setStyleSheet("")
        self.double_2013_bsa.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.double_2013_bsa.setMaximum(99999.99)
        self.double_2013_bsa.setSingleStep(0.01)
        self.double_2013_bsa.setObjectName("double_2013_bsa")
        self.tabWidget_2.addTab(self.tab_2013, "")
        self.tabWidget.addTab(self.tab_card, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "身 高："))
        self.label_4.setText(_translate("Form", " cm"))
        self.label_5.setText(_translate("Form", " kg"))
        self.label_6.setText(_translate("Form", "体 重："))
        self.label_7.setText(_translate("Form", "m²"))
        self.label_8.setText(_translate("Form", "BSA："))
        self.label_2008_bsa_formula.setText(_translate("Form", "BSA="))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2008), _translate("Form", "Bei xia 2008"))
        self.label_9.setText(_translate("Form", " kg"))
        self.label_10.setText(_translate("Form", " cm"))
        self.label_11.setText(_translate("Form", "m²"))
        self.label_12.setText(_translate("Form", "身 高："))
        self.label_2013_bsa_formula.setText(_translate("Form", "BSA="))
        self.label_13.setText(_translate("Form", "BSA："))
        self.label_14.setText(_translate("Form", "体 重："))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2013), _translate("Form", "Pattersen 2013"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_card), _translate("Form", "Z评分"))
