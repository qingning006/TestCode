# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_smp.ui'
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
        self.tab_thyroid = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_thyroid.setFont(font)
        self.tab_thyroid.setObjectName("tab_thyroid")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_thyroid)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 971, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_thy_b = QtWidgets.QWidget()
        self.tab_thy_b.setObjectName("tab_thy_b")
        self.groupBox = QtWidgets.QGroupBox(self.tab_thy_b)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 191, 181))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.thy_d1 = QtWidgets.QLineEdit(self.groupBox)
        self.thy_d1.setGeometry(QtCore.QRect(90, 20, 60, 20))
        self.thy_d1.setObjectName("thy_d1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.thy_d2 = QtWidgets.QLineEdit(self.groupBox)
        self.thy_d2.setGeometry(QtCore.QRect(90, 50, 60, 20))
        self.thy_d2.setObjectName("thy_d2")
        self.thy_d3 = QtWidgets.QLineEdit(self.groupBox)
        self.thy_d3.setGeometry(QtCore.QRect(90, 80, 60, 20))
        self.thy_d3.setObjectName("thy_d3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.thy_v1 = QtWidgets.QLineEdit(self.groupBox)
        self.thy_v1.setEnabled(True)
        self.thy_v1.setGeometry(QtCore.QRect(90, 110, 91, 20))
        self.thy_v1.setReadOnly(True)
        self.thy_v1.setObjectName("thy_v1")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 71, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.thy_v2 = QtWidgets.QLineEdit(self.groupBox)
        self.thy_v2.setEnabled(True)
        self.thy_v2.setGeometry(QtCore.QRect(90, 140, 91, 20))
        self.thy_v2.setReadOnly(True)
        self.thy_v2.setObjectName("thy_v2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 71, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tabWidget_2.addTab(self.tab_thy_b, "")
        self.tab_thy_d = QtWidgets.QWidget()
        self.tab_thy_d.setObjectName("tab_thy_d")
        self.tabWidget_2.addTab(self.tab_thy_d, "")
        self.tab_thy_m = QtWidgets.QWidget()
        self.tab_thy_m.setObjectName("tab_thy_m")
        self.tabWidget_2.addTab(self.tab_thy_m, "")
        self.tabWidget.addTab(self.tab_thyroid, "")
        self.tab_breast = QtWidgets.QWidget()
        self.tab_breast.setObjectName("tab_breast")
        self.tabWidget.addTab(self.tab_breast, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "甲状腺体积"))
        self.label.setText(_translate("Form", "长 径"))
        self.label_2.setText(_translate("Form", "宽 径"))
        self.label_3.setText(_translate("Form", "厚 径"))
        self.label_4.setText(_translate("Form", "体积(0.479)"))
        self.label_5.setText(_translate("Form", "体积(0.523)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_thy_b), _translate("Form", "B模式"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_thy_d), _translate("Form", "D模式"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_thy_m), _translate("Form", "M模式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_thyroid), _translate("Form", "甲状腺"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_breast), _translate("Form", "乳腺"))