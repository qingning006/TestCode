# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: log.py
date    : 2023/2/23 22:10
desc    : 
"""
import time
import logging


class Log:
	def __init__(self):
		# 日志文件名
		self.Log_File = time.strftime("%Y-%m-%d", time.localtime()) + "_meas_cal.log"
		# filename 指定日志存放文件，level 指定logging级别
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.INFO)

		# 创建 handler 输出到文件
		self.file_handler = logging.FileHandler(self.Log_File, mode='a') # 一定要加上 mode='w'
		self.file_handler.setLevel(logging.INFO)

		# handler 输出到控制台
		self.console_handler = logging.StreamHandler()
		self.console_handler.setLevel(logging.DEBUG)

		# 创建 logging format
		formatter = logging.Formatter("%(asctime)s  [%(levelname)s] : %(message)s")
		self.file_handler.setFormatter(formatter)
		self.console_handler.setFormatter(formatter)
		# add the handlers to the logger
		self.logger.addHandler(self.file_handler)
		self.logger.addHandler(self.console_handler)

	# 写日志
	def info(self, content):
		self.logger.info(content)

	def warring(self, content):
		self.logger.warning(content)