# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: base.py
date    : 2023/5/14
desc    :
"""
import os
from PyQt5.QtGui import QColor
from base.log import Log


class Base:
    def __init__(self):
        self.log = Log()
        self.color = DefColor()

    # os.listdir()方法获取文件夹名字，返回数组
    def getAllFiles(self, targetDir):
        listFiles = os.listdir(targetDir)
        for i in listFiles:
            print(str(i))
        return listFiles

    def screenshot(self):
        """
        截屏保存
        :return:
        """
        pass


class DefColor:
    def __init__(self):
        self.HighLight = QColor(230,200,100)


if __name__ == '__main__':
    depart = Base()

    ac,bpd = 10,12
    print(eval("9.57+0.524*ac+0.1220*bpd**2"))
    print(eval("ac+bpd*2"))


