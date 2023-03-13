# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QOb.py
date    : 2023/2/19 20:08
desc    :
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from ui import ui_ob, ui_GA


class Ob(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_ob.Ui_Form()
		self.ui.setupUi(self)


class GA(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_GA.Ui_Form()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QApplication([])
	stats = Ob()
	stats.show()
	app.exec_()
	pass
