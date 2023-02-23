
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui import main
from base.defCal import Depart


class Calculator(QMainWindow):
	def __init__(self):
		super().__init__()
		# 实例化一个 Ui_MainWindow对象
		self.ui = main.Ui_MainWindow()
		self.ui.setupUi(self)
		# 这里使用的是 self.show(),和之后的区分一下
		self.show()

		#默认显示第一个科室
		self.depart_change()

		#设置菜单栏动作触发信号triggled()
		self.ui.menu_abd.triggered.connect(self.depart_abd)
		self.ui.menu_ob.triggered.connect(self.depart_ob)
		self.ui.menu_gyn.triggered.connect(self.depart_gyn)
		self.ui.menu_card.triggered.connect(self.depart_card)
		self.ui.menu_vas.triggered.connect(self.depart_vas)
		self.ui.menu_uro.triggered.connect(self.depart_uro)
		self.ui.menu_smp.triggered.connect(self.depart_smp)
		self.ui.menu_ped.triggered.connect(self.depart_ped)

	def depart_change(self, index=0):
		print("depart_change")
		self.ui.stackedWidget.setCurrentIndex(index)

	def depart_abd(self):
		self.depart_change(Depart.ABD)

	def depart_ob(self):
		self.depart_change(Depart.OB)

	def depart_gyn(self):
		self.depart_change(Depart.GYN)

	def depart_card(self):
		self.depart_change(Depart.CARD)

	def depart_vas(self):
		self.depart_change(Depart.VAS)

	def depart_uro(self):
		self.depart_change(Depart.URO)

	def depart_smp(self):
		self.depart_change(Depart.SMP)

	def depart_ped(self):
		self.depart_change(Depart.PED)


if __name__ == '__main__':
	app = QApplication([])
	stats = Calculator()
	stats.show()
	app.exec_()
	pass



