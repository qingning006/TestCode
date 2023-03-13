# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QVas.py
date    : 2023/2/19 20:08
desc    :
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from ui import ui_vas


class Vas(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_vas.Ui_Form()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QApplication([])
	stats = Vas()
	stats.show()
	app.exec_()
	pass
