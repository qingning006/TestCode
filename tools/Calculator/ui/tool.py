# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: tool.py
date    : 2023/7/3 
desc    : ui文件批量转换成py文件
"""

import os
import os.path


# 列出目录下的所有ui文件
def listUiFile(path):
    list = []
    files = os.listdir(path)
    for filename in files:
        # print( dir + os.sep + f  )
        # print(filename)
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)

    return list


# 把后缀为ui的文件改成后缀为py的文件名
def transPyFile(filename):
    return os.path.splitext(filename)[0] + '.py'


# 调用系统命令把ui转换成py
def ui2py(path):
    list = listUiFile(path)
    for uifile in list:
        pyfile = transPyFile(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile, uifile=uifile)
        print(cmd)
        os.system(cmd)


###### 程序的主入口
if __name__ == '__main__':
    # UI文件所在的路径
    dir = './'
    ui2py(dir)
