# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ped.ui'
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
        self.tab_ped = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_ped.setFont(font)
        self.tab_ped.setObjectName("tab_ped")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_ped)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 971, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_ob_b = QtWidgets.QWidget()
        self.tab_ob_b.setObjectName("tab_ob_b")
        self.tabWidget_2.addTab(self.tab_ob_b, "")
        self.tab_ob_d = QtWidgets.QWidget()
        self.tab_ob_d.setObjectName("tab_ob_d")
        self.tabWidget_2.addTab(self.tab_ob_d, "")
        self.tab_ob_m = QtWidgets.QWidget()
        self.tab_ob_m.setObjectName("tab_ob_m")
        self.tabWidget_2.addTab(self.tab_ob_m, "")
        self.tabWidget.addTab(self.tab_ped, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_ob_b), _translate("Form", "B模式"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_ob_d), _translate("Form", "D模式"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_ob_m), _translate("Form", "M模式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ped), _translate("Form", "儿科"))
