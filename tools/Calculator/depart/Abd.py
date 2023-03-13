# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QAbd.py
date    : 2023/2/19 20:08
desc    :
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui import ui_abd


class Abd(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_abd.Ui_Form()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QApplication([])
	stats = Abd()
	stats.show()
	app.exec_()
	pass
