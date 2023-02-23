# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: calformula.py
date    : 2023/2/23 22:58
desc    : 
"""


# 体积公式
def vol_1d(d1, radio=1):
	return vol_3d(d1, d1, d1, radio)

def vol_2d(d1, d2, radio=1):
	return vol_3d(d1, d2, d2, radio)

def vol_3d(d1, d2, d3, radio=1):
	return '{:.3f}'.format(d1*d2*d3*radio)

