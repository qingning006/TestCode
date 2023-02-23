# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: defcommon.py
date    : 2023/2/22 23:32
desc    : 
"""
from PyQt5.QtCore import QRegExp


# 浮点数
V_FLOAT = QRegExp('^-?([1-9]d*.d*|0.d*[1-9]d*|0?.0+|0)$')
