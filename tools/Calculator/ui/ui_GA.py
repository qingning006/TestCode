# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_GA.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 573)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1001, 521))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_card = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_card.setFont(font)
        self.tab_card.setObjectName("tab_card")
        self.label = QtWidgets.QLabel(self.tab_card)
        self.label.setGeometry(QtCore.QRect(50, 50, 54, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_card)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 54, 25))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab_card)
        self.label_5.setGeometry(QtCore.QRect(120, 50, 54, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_card)
        self.label_6.setGeometry(QtCore.QRect(250, 50, 54, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_card)
        self.label_7.setGeometry(QtCore.QRect(380, 50, 54, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_card)
        self.label_8.setGeometry(QtCore.QRect(490, 50, 54, 20))
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.tab_card)
        self.comboBox.setGeometry(QtCore.QRect(120, 80, 100, 25))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_card)
        self.lineEdit.setGeometry(QtCore.QRect(240, 80, 71, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab_card)
        self.label_3.setGeometry(QtCore.QRect(320, 80, 31, 25))
        self.label_3.setObjectName("label_3")
        self.label_GA_BPD = QtWidgets.QLabel(self.tab_card)
        self.label_GA_BPD.setGeometry(QtCore.QRect(360, 80, 101, 25))
        self.label_GA_BPD.setText("")
        self.label_GA_BPD.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_GA_BPD.setObjectName("label_GA_BPD")
        self.label_EDD_BPD = QtWidgets.QLabel(self.tab_card)
        self.label_EDD_BPD.setGeometry(QtCore.QRect(480, 80, 101, 25))
        self.label_EDD_BPD.setText("")
        self.label_EDD_BPD.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_EDD_BPD.setObjectName("label_EDD_BPD")
        self.checkBox = QtWidgets.QCheckBox(self.tab_card)
        self.checkBox.setGeometry(QtCore.QRect(20, 80, 21, 25))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(self.tab_card)
        self.label_4.setGeometry(QtCore.QRect(15, 50, 31, 20))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_card, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "测量项"))
        self.label_2.setText(_translate("Form", "BPD"))
        self.label_5.setText(_translate("Form", "公式"))
        self.label_6.setText(_translate("Form", "测量值"))
        self.label_7.setText(_translate("Form", "GA"))
        self.label_8.setText(_translate("Form", "EDD"))
        self.label_3.setText(_translate("Form", "mm"))
        self.label_4.setText(_translate("Form", "AUA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_card), _translate("Form", "孕龄"))
