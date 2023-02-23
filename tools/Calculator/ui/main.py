# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1091, 591))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QAbd()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QOb()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QGyn()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QCard()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QVas()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QUro()
        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QSmp()
        self.page_7.setObjectName("page_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QPed()
        self.page_8.setObjectName("page_8")
        self.stackedWidget.addWidget(self.page_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_abd = QtWidgets.QAction(MainWindow)
        self.menu_abd.setObjectName("menu_abd")
        self.menu_ob = QtWidgets.QAction(MainWindow)
        self.menu_ob.setObjectName("menu_ob")
        self.menu_gyn = QtWidgets.QAction(MainWindow)
        self.menu_gyn.setObjectName("menu_gyn")
        self.menu_card = QtWidgets.QAction(MainWindow)
        self.menu_card.setObjectName("menu_card")
        self.menu_vas = QtWidgets.QAction(MainWindow)
        self.menu_vas.setObjectName("menu_vas")
        self.menu_uro = QtWidgets.QAction(MainWindow)
        self.menu_uro.setObjectName("menu_uro")
        self.menu_smp = QtWidgets.QAction(MainWindow)
        self.menu_smp.setObjectName("menu_smp")
        self.menu_ped = QtWidgets.QAction(MainWindow)
        self.menu_ped.setObjectName("menu_ped")
        self.menu.addAction(self.menu_abd)
        self.menu.addAction(self.menu_ob)
        self.menu.addAction(self.menu_gyn)
        self.menu.addAction(self.menu_card)
        self.menu.addAction(self.menu_vas)
        self.menu.addAction(self.menu_uro)
        self.menu.addAction(self.menu_smp)
        self.menu.addAction(self.menu_ped)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", " 科室测量 "))
        self.menu_2.setTitle(_translate("MainWindow", " 特殊测量 "))
        self.menu_abd.setText(_translate("MainWindow", "腹部"))
        self.menu_ob.setText(_translate("MainWindow", "产科"))
        self.menu_gyn.setText(_translate("MainWindow", "妇科"))
        self.menu_card.setText(_translate("MainWindow", "心脏"))
        self.menu_vas.setText(_translate("MainWindow", "血管"))
        self.menu_uro.setText(_translate("MainWindow", "泌尿"))
        self.menu_smp.setText(_translate("MainWindow", "小器官"))
        self.menu_ped.setText(_translate("MainWindow", "儿科"))
from depart.QAbd import QAbd
from depart.QCard import QCard
from depart.QGyn import QGyn
from depart.QOb import QOb
from depart.QPed import QPed
from depart.QSmp import QSmp
from depart.QUro import QUro
from depart.QVas import QVas
