# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QSmp.py
date    : 2023/2/19 20:08
desc    :
"""


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from ui import smp
from base.log import *
from base.apiformula import *
from base.defCal import *


class QSmp(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = smp.Ui_Form()
		self.ui.setupUi(self)

		self.init_validator()
		self.init_action_connect()

# 初始化事件响应
	def init_action_connect(self):
		self.ui.thy_d1.textChanged.connect(self.update_smp_vol)
		self.ui.thy_d2.textChanged.connect(self.update_smp_vol)
		self.ui.thy_d3.textChanged.connect(self.update_smp_vol)

# 初始化校验器
	def init_validator(self):
		# 浮点校验器 小数点后两位
		double_valid = QDoubleValidator(self)
		# validator.setRange(-1000, 1000)
		double_valid.setNotation(QDoubleValidator.StandardNotation)
		double_valid.setDecimals(3)  # 小数点后3位
		self.ui.thy_d1.setValidator(double_valid)
		self.ui.thy_d2.setValidator(double_valid)
		self.ui.thy_d3.setValidator(double_valid)

	def update_smp_vol(self):
		if self.ui.thy_d1.text() == "" or self.ui.thy_d2.text() == "" or self.ui.thy_d3.text() == "":
			return
		d1 = float(self.ui.thy_d1.text()) if self.ui.thy_d1.text() != "" else 0.0
		d2 = float(self.ui.thy_d2.text()) if self.ui.thy_d2.text() != "" else 0.0
		d3 = float(self.ui.thy_d3.text()) if self.ui.thy_d3.text() != "" else 0.0
		v1 = vol_3d(d1, d2, d2, VOL_479)
		self.ui.thy_v1.setText(str(v1))
		v2 = vol_3d(d1, d2, d2, VOL_523)
		self.ui.thy_v2.setText(str(v2))
		write_log(f' 甲状腺体积：{d1} * {d2} * {d3} * 0.479 = {v1},  {d1} * {d2} * {d3} * 0.523 = {v2}')


if __name__ == '__main__':
	app = QApplication([])
	stats = QSmp()
	stats.show()
	app.exec_()
	pass
