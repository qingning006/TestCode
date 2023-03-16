# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QSmp.py
date    : 2023/2/19 20:08
desc    :
"""


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from ui import ui_smp
from base.log import *
from base.defformula import *
from base.defCal import *


class Smp(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_smp.Ui_Form()
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
		self.update_vol_3d(self.ui.thy_d1, self.ui.thy_d2, self.ui.thy_d3, self.ui.thy_v1, "甲状腺", VOL_479)
		self.update_vol_3d(self.ui.thy_d1, self.ui.thy_d2, self.ui.thy_d3, self.ui.thy_v2, "甲状腺", VOL_523)

	def update_vol_3d(self, dist1, dist2, dist3, vol, name=None, coe=VOL_Normal):
		vol.setText("")
		# 长宽厚有一个为空，则清空体积
		if dist1.text() == "" or dist2.text() == "" or dist3.text() == "":
			return
		d1 = float(dist1.text()) if dist1.text() != "" else 0.0
		d2 = float(dist2.text()) if dist2.text() != "" else 0.0
		d3 = float(dist3.text()) if dist3.text() != "" else 0.0
		v1 = vol_3d(d1, d2, d2, coe)
		vol.setText(str(v1))
		Log(f' {name}体积：{d1} * {d2} * {d3} * {coe} = {v1}')
		#get_logger().info(f' {name}体积：{d1} * {d2} * {d3} * {coe} = {v1}')


if __name__ == '__main__':
	app = QApplication([])
	stats = Smp()
	stats.show()
	app.exec_()
	pass
