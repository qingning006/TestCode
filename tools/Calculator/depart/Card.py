# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QCard.py
date    : 2023/2/19 20:08
desc    :
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from ui import ui_card, ui_zscore


class Card(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_card.Ui_Form()
		self.ui.setupUi(self)


class ZScore(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_zscore.Ui_Form()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QApplication([])
	stats = Card()
	stats.show()
	app.exec_()
	pass
