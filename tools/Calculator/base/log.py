# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: log.py
date    : 2023/2/23 22:10
desc    : 
"""
import time

Log_File = time.strftime("%Y-%m-%d", time.localtime()) + "_meas_cal.log"


# 写日志
def write_log(content):
	log = open(Log_File, 'a')  # 以追加方式打开日志文件
	time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 系统时间格式化
	log.writelines(time_now+': '+content+'\n')      # 写入内容
	log.close()
	print(content)
