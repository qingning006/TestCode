# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: defCal.py
date    : 2023/2/20 22:08
desc    : 
"""

from enum import IntEnum, unique


# 菜单栏上科室页签顺序定义，注意要与main.ui上的页面顺序一致
@unique
class Depart(IntEnum):
	ABD = 0
	OB = 1
	GYN = 2
	CARD = 3
	VAS = 4
	URO = 5
	SMP = 6
	PED = 7


# 公式系数定义
VOL_479 = 0.479
VOL_523 = 0.523
