# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: defCal.py
date    : 2023/2/20 22:08
desc    : 
"""

from enum import IntEnum, unique


@unique
class Depart(IntEnum):
	ABD = 0
	OB = 1
	GYN = 2
	CARD = 3
	VAS = 5
	URO = 6
	SMP = 7
	PED = 8


# 菜单栏上页签排序
