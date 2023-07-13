# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QOb.py
date    : 2023/2/19 20:08
desc    :
"""

from PyQt5.QtWidgets import QApplication, QWidget
from ui import ui_ob, ui_GA
from base.defformula import FormulaOB


class Ob(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_ob.Ui_Form()
		self.ui.setupUi(self)


class GA(QWidget):
	def __init__(self):
		# 实例化一个 Ui_MainWindow对象
		super().__init__()
		self.ui = ui_GA.Ui_Form()
		self.ui.setupUi(self)
		self.fmlOB = FormulaOB()

		self.init_item_value()
		self.init_action_connect()

	# 初始化控件属性
	def init_item_value(self):
		pass

	# 初始化事件响应
	def init_action_connect(self):
		#self.ui.cmbox_bpd_fml.addItems(['AC(Campbell)','AC,BPD(Hadlock)'])
		self.ui.cmbox_LMP.currentIndexChanged.connect(self.updat_LMP)
		self.ui.dateEdit_LMP.dateChanged.connect(self.updat_LMP)
		self.ui.cmbox_fml_CUA.currentIndexChanged.connect(self.update_CUA)
		self.ui.cmbox_fml_efw.currentIndexChanged.connect(self.update_EFW)
		self.ui.cmbox_bpd_fml.currentIndexChanged.connect(self.update_EFW)

	def updat_LMP(self):
		sel = self.ui.cmbox_LMP.currentIndex()
		if sel == 0:
			self.cal_LMP()
		else:
			self.cal_DOC()

		# 更新所有胎重相关计算
		self.update_EFW()
		self.update_all_meas()
		self.update_AUA()
		self.update_CUA()

	def cal_LMP(self):
		# 计算末次月经对应的GA和EDD
		pass

	def cal_DOC(self):
		# 计算受精日期对应的GA和EDD
		pass

	def update_AUA(self):
		# 更新AUA计算值
		self.cal_AUA()

	def cal_AUA(self):
		pass

	def update_CUA(self):
		# 更新CUA结果值
		self.cal_CUA()


	def cal_CUA(self):
		pass


	def update_EFW(self):
		# 胎重公式改变，需要刷新胎重结果，生长误差，胎重估算GA
		self.cal_EFW()
		self.cal_EFW_GA()
		self.cal_EFW_Growth()

	def update_EFW_GA(self):
		# 胎重估算孕龄公式改变
		self.cal_EFW_GA()

	def update_EFW_Growth(self):
		# 胎重生长误差计算公式改变
		self.cal_EFW_Growth()

	def cal_EFW(self):
		# EFW计算公式
		# 获取当前公式选择
		result, sd = "/", "/"
		fml = self.ui.cmbox_fml_efw.currentText()
		# 转换直径单位为cm，FTA单位为cm2，用于胎重公式计算
		bpd = self.ui.double_bpd.value()/10
		hc = self.ui.double_hc.value()/10
		ac = self.ui.double_ac.value()/10
		fl = self.ui.double_fl.value()/10
		fta = 0
		mad = 0
		ttd = 0
		print(fml)
		if fml == "AC(Campbell)":
			result,sd=self.fmlOB.EFW_AC_Campbell(ac)
		elif fml == "AC,BPD(Hadlock)":
			result, sd = self.fmlOB.EFW_AC_BPD_Hadlock(ac,bpd)
		elif fml == "AC,BPD(Merz)":
			result, sd = self.fmlOB.EFW_AC_BPD_Hadlock(ac,bpd)
		elif fml == "AC,BPD(Shepard)":
			result, sd = self.fmlOB.EFW_AC_BPD_Hadlock(ac,bpd)
		elif fml == "AC,FL(Hadlock1)":
			result, sd = self.fmlOB.EFW_AC_BPD_Hadlock(ac,bpd)
		elif fml == "BPD,AC,FL(Hadlock2)":
			result, sd = self.fmlOB.EFW_AC_BPD_Hadlock(ac,bpd)
		elif fml == "BPD,APTD,TTD,FL(Shinozuka1)":
			result, sd = self.fmlOB.EFW_AC_BPD_Hadlock(ac,bpd)
		elif fml == "BPD,APTD,TTD,FL(Tokyo)":
			result, sd = self.fmlOB.EFW_AC_BPD_Hadlock(ac,bpd)
		elif fml == "BPD,APTD,TTD,LV(Shinozuka3)":
			result, sd = self.fmlOB.EFW_AC_BPD_Hadlock(ac,bpd)
		elif fml == "BPD,FL,AC(JSUM)":
			result, sd = self.fmlOB.EFW_BPD_FL_AC_JSUM(bpd,fl,ac)
		elif fml == "BPD,FL,AC(Shinozuka2)":
			result, sd = self.fmlOB.EFW_BPD_FL_AC_Shinozuka2(bpd,fl,ac)
		elif fml == "BPD,FTA,FL(Osaka)":
			result, sd = self.fmlOB.EFW_BPD_FTA_FL_Osaka(bpd,fta,fl)
		elif fml == "BPD,HC,AC,FL(Hadlock4)":
			result, sd = self.fmlOB.EFW_BPD_HC_AC_FL_Hadlock4(bpd,hc,ac,fl)
		elif fml == "BPD,MAD(Persson2)":
			result, sd = self.fmlOB.EFW_BPD_MAD_Persson2(bpd,mad)
		elif fml == "BPD,MAD,FL(Persson1)":
			result, sd = self.fmlOB.EFW_BPD_MAD_FL_Persson1(bpd,mad,fl)
		elif fml == "BPD,TTD(Hansmann)":
			result, sd = self.fmlOB.EFW_BPD_TTD_Hansmann(bpd,ttd)
		elif fml == "HC,AC,FL(Hadlock3)":
			result, sd = self.fmlOB.EFW_HC_AC_FL_Hadlock3(hc,ac,fl)
		elif fml == "HC,AC,FL(Schild)":
			result, sd = self.fmlOB.EFW_HC_AC_FL_Schild(hc,ac,fl)
		print(result, sd)

		#胎重结果值取整
		if result != "?" and result != "/":
			result = str(int(result))+'g'
		if sd != "?" and sd != "/" and result != "/":   # result为/，SD可能返回了文字提示
			sd = str(int(sd))+'g'
		self.ui.label_efw_value.setText(str(result))
		self.ui.label_efw_value_sd.setText(str(sd))

	def cal_EFW_GA(self):
		# 根据EFW计算GA
		pass

	def cal_EFW_Growth(self):
		# 根据胎重计算生长误差
		pass

	def update_all_meas(self):
		# 更新所有测量值对应的GA、SD
		pass


if __name__ == '__main__':
	app = QApplication([])
	stats = GA()
	stats.show()
	app.exec_()

	pass
