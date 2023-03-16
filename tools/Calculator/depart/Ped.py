# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QPed.py
date    : 2023/2/19 20:08
desc    :
"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from ui import ui_ped
from base.log import *


class Ped(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_ped.Ui_Form()
		self.ui.setupUi(self)
		self.init_validator()
		self.init_action_connect()

	# 初始化事件响应
	def init_action_connect(self):
		self.ui.lineEdit_year.textChanged.connect(self.update_graf)
		self.ui.lineEdit_month.textChanged.connect(self.update_graf)
		self.ui.lineEdit_a.textChanged.connect(self.update_graf)
		self.ui.lineEdit_b.textChanged.connect(self.update_graf)
		self.ui.lineEdit_d1.textChanged.connect(self.update_fhc)
		self.ui.lineEdit_d2.textChanged.connect(self.update_fhc)

	# 初始化校验器
	def init_validator(self):
		# 浮点校验器 小数点后三位
		double_valid = QDoubleValidator(self)
		# validator.setRange(-1000, 1000)
		double_valid.setNotation(QDoubleValidator.StandardNotation)
		double_valid.setDecimals(3)  # 小数点后3位
		int_valid = QIntValidator(self)
		self.ui.lineEdit_year.setValidator(int_valid)
		self.ui.lineEdit_month.setValidator(int_valid)
		self.ui.lineEdit_a.setValidator(double_valid)
		self.ui.lineEdit_b.setValidator(double_valid)
		self.ui.lineEdit_d1.setValidator(double_valid)
		self.ui.lineEdit_d2.setValidator(double_valid)


	def update_graf(self):
		# 先清空分型和描述
		self.ui.text_type.setText("")
		self.ui.text_desc_graf.setText("")
		# 获取角度值
		age_y = int(self.ui.lineEdit_year.text()) if self.ui.lineEdit_year.text() != "" else 0
		age_m = int(self.ui.lineEdit_month.text()) if self.ui.lineEdit_month.text() != "" else 0
		age = age_y * 12 + age_m
		angle_a = float(self.ui.lineEdit_a.text()) if self.ui.lineEdit_a.text() != "" else 0.0
		angle_b = float(self.ui.lineEdit_b.text()) if self.ui.lineEdit_b.text() != "" else 0.0
		print(age, angle_a, angle_b)
		# 结果分型
		str_type, str_desc = "", ""
		if angle_a >= 60 and angle_b <= 55:
			str_type = "Ia"
			str_desc = """成熟髋关节
			mature hip"""
		elif angle_a >= 60 and angle_b > 55:
			str_type = "Ib"
			str_desc = """成熟髋关节
			mature hip"""
		elif 55 <= angle_a <= 59 and 6 <= age <= 12:
			str_type = "IIa(+)"
			str_desc = """生理性不成熟
			physiological immature"""
		elif 50 <= angle_a < 55 and 6 <= age <= 12:
			str_type = "IIa(-)"
			str_desc = """成熟缺陷
			maturational deficite"""
		elif 50 <= angle_a <= 59 and age > 12:
			str_type = "IIb"
			str_desc = """骨化延迟
			delay of ossification"""
		elif 50 <= angle_a <= 59 and age < 6:
			str_type = "IIa/IIb"
			str_desc = """(结果窗不显示)"""
		elif 43 <= angle_a <= 49 and angle_b <= 77:
			str_type = "IIc"
			str_desc = """可能发生脱位
			decentring can occur"""
		elif 43 <= angle_a <= 49 and angle_b > 77:
			str_type = "D"
			str_desc = """即将脱位
			about to decentre"""

		self.ui.text_type.setText(str_type)
		self.ui.text_desc_graf.setText(str_desc)
		Log(f' 小儿髋关节Graf分型：α：{angle_a}°, β：{angle_b}°,  分型：{str_type},  描述：{str_desc}')

	def update_fhc(self):
		# 先清空分型和描述
		self.ui.text_dradio.setText("")
		self.ui.text_desc_fhc.setText("")
		# 获取d、D值，计算d/D比率
		dist_d1 = float(self.ui.lineEdit_d1.text()) if self.ui.lineEdit_d1.text() != "" else 0.0
		dist_d2 = float(self.ui.lineEdit_d2.text()) if self.ui.lineEdit_d2.text() != "" else 0.0
		if dist_d2 == 0.0:
			return
		dist_radio = float(dist_d1/dist_d2)
		# 结果分型
		str_desc = ""
		if dist_radio>58:
			str_desc = """发育正常
			Normal"""
		elif 33 <= dist_radio <= 58:
			str_desc = """部分正常部分异常
			Partial Normal"""
		elif dist_radio<33:
			str_desc = """发育异常
			Abnormal"""
		str_radio = "%.3f" % dist_radio
		self.ui.text_dradio.setText(str_radio)
		self.ui.text_desc_fhc.setText(str_desc)
		Log(f' 小儿髋关节FHC分型：d：{dist_d1}°, D：{dist_d2}°, FHC：{str_radio} , 描述：{str_desc}')


if __name__ == '__main__':
	app = QApplication([])
	stats = Ped()
	stats.show()
	app.exec_()
	pass
