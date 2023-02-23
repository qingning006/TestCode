# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QSmp.py
date    : 2023/2/19 20:08
desc    :
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from TestCode.tools.Calculator.ui import abd


class QAbd(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = abd.Ui_Form()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QApplication([])
	stats = QAbd()
	stats.show()
	app.exec_()
	pass
