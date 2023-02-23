# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QSmp.py
date    : 2023/2/19 20:08
desc    :
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from TestCode.tools.Calculator.ui import smp
from TestCode.tools.Calculator.base.defcommon import *


class QSmp(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = smp.Ui_Form()
		self.ui.setupUi(self)

		self.ui.thy_d1.textChanged.connect(self.update_smp_vol)
		self.ui.thy_d2.textChanged.connect(self.update_smp_vol)
		self.ui.thy_d3.textChanged.connect(self.update_smp_vol)

		# 浮点校验器 小数点后两位
		validator = QDoubleValidator(self)
		#validator.setRange(-360, 360)
		validator.setNotation(QDoubleValidator.StandardNotation)
		validator.setDecimals(3)
		#validator = QRegExpValidator(self)
		#validator.setRegExp(V_FLOAT)
		self.ui.thy_d1.setValidator(validator)
		self.ui.thy_d2.setValidator(validator)
		self.ui.thy_d3.setValidator(validator)

	def update_smp_vol(self):
		print("update_smp_vol")
		d1 = float(self.ui.thy_d1.text()) if self.ui.thy_d1.text() != "" else 0.0
		d2 = float(self.ui.thy_d2.text()) if self.ui.thy_d2.text() != "" else 0.0
		d3 = float(self.ui.thy_d3.text()) if self.ui.thy_d3.text() != "" else 0.0
		v = 0.523*d1*d2*d3
		print(v, d1, d2, d3)
		self.ui.thy_v1.setText(str(v))
		pass


if __name__ == '__main__':
	app = QApplication([])
	stats = QSmp()
	stats.show()
	app.exec_()
	pass
