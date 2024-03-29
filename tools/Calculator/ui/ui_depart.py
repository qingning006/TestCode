# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_depart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1226, 747)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1201, 721))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_abd = Abd()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab_abd.setFont(font)
        self.tab_abd.setObjectName("tab_abd")
        self.tabWidget.addTab(self.tab_abd, "")
        self.tab_ob = Ob()
        self.tab_ob.setObjectName("tab_ob")
        self.tabWidget.addTab(self.tab_ob, "")
        self.tab_gyn = Gyn()
        self.tab_gyn.setObjectName("tab_gyn")
        self.tabWidget.addTab(self.tab_gyn, "")
        self.tab_card = Card()
        self.tab_card.setObjectName("tab_card")
        self.tabWidget.addTab(self.tab_card, "")
        self.tab_vas = Vas()
        self.tab_vas.setObjectName("tab_vas")
        self.tabWidget.addTab(self.tab_vas, "")
        self.tab_uro = Uro()
        self.tab_uro.setObjectName("tab_uro")
        self.tabWidget.addTab(self.tab_uro, "")
        self.tab_smp = Smp()
        self.tab_smp.setObjectName("tab_smp")
        self.tabWidget.addTab(self.tab_smp, "")
        self.tab_ped = Ped()
        self.tab_ped.setObjectName("tab_ped")
        self.tabWidget.addTab(self.tab_ped, "")
        self.tab_lung = QtWidgets.QWidget()
        self.tab_lung.setObjectName("tab_lung")
        self.tabWidget.addTab(self.tab_lung, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_abd), _translate("Form", "腹部"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ob), _translate("Form", "产科"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gyn), _translate("Form", "妇科"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_card), _translate("Form", "心脏"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vas), _translate("Form", "血管"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_uro), _translate("Form", "泌尿"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_smp), _translate("Form", "小器官"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ped), _translate("Form", "儿科"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_lung), _translate("Form", "肺"))
from depart.Abd import Abd
from depart.Card import Card
from depart.Gyn import Gyn
from depart.Ob import Ob
from depart.Ped import Ped
from depart.Smp import Smp
from depart.Uro import Uro
from depart.Vas import Vas
