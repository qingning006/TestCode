# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: application.py
date    : 2023/7/13 
desc    : 
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from ui import ui_depart


class Depart(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_depart.Ui_Form()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QApplication([])
	stats = Depart()
	stats.show()
	app.exec_()
	pass
