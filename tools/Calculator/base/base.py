# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: base.py
date    : 2023/5/14 21:25
desc    :
"""
import os
from PyQt5.QtGui import QDoubleValidator,QColor

from base.log import Log


class Base:
	def __init__(self):
		self.log = Log()
		self.color = DefColor()
		# 浮点校验器 小数点后两位
		self.double_valid = QDoubleValidator(self)
		self.double_valid.setNotation(QDoubleValidator.StandardNotation)
		self.double_valid.setDecimals(3)  # 小数点后3位


	def get_project_root_path(self):
		# 获取当前文件的目录
		cur_path = os.path.abspath(os.path.dirname(__file__))
		# 获取根目录
		root_path = cur_path[:cur_path.find('Calculator')] + 'Calculator'
		print(root_path)
		return root_path

	def get_double_validator(self):
		return self.double_valid


class DefColor:
	def __init__(self):
		self.HighLight = QColor(230,200,100)

if __name__ == '__main__':
	depart = Base()
	depart.get_project_root_path()
	pass
