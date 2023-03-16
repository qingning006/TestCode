# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: log.py
date    : 2023/2/23 22:10
desc    : 
"""
import time
import logging

# 日志文件名
Log_File = time.strftime("%Y-%m-%d", time.localtime()) + "_meas_cal.log"
# filename 指定日志存放文件，level 指定logging级别


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建 handler 输出到文件
file_handler = logging.FileHandler(Log_File, mode='a') # 一定要加上 mode='w'
file_handler.setLevel(logging.INFO)

# handler 输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建 logging format
formatter = logging.Formatter("%(asctime)s  [%(levelname)s] : %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# 写日志
def Log(content):
	logger.info(content)


def get_logger():
	return logger
