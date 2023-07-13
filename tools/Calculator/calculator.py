
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import ui_main


class Calculator(QMainWindow):
	def __init__(self):
		super().__init__()
		# 实例化一个 Ui_MainWindow对象
		self.ui = ui_main.Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle("测量计算器V1.0")
		# self.setFont()
		# 这里使用的是 self.show(),和之后的区分一下
		self.show()

		#默认显示第一个科室
		self.depart_change()

		#设置菜单栏动作触发信号triggled()
		self.ui.menu_zscore.triggered.connect(self.meas_zscore)
		self.ui.menu_ga.triggered.connect(self.meas_ga)
		self.ui.menu_depart.triggered.connect(self.meas_depart)

	def depart_change(self, index=0):
		print("depart_change")
		self.ui.stackedWidget.setCurrentIndex(index)

	def depart_abd(self):
		#self.depart_change(Depart.ABD)
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_abd)

	def depart_ob(self):
		#self.depart_change(Depart.OB)
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_ob)

	def depart_gyn(self):
		#self.depart_change(Depart.GYN)
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_gyn)

	def depart_card(self):
		#self.depart_change(Depart.CARD)
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_card)

	def depart_vas(self):
		#self.depart_change(Depart.VAS)
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_vas)

	def depart_uro(self):
		#self.depart_change(Depart.URO)
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_uro)

	def depart_smp(self):
		#self.depart_change(Depart.SMP)
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_smp)

	def depart_ped(self):
		#self.depart_change(Depart.PED)
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_ped)

	def meas_zscore(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_zscore)

	def meas_ga(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_ga)

	def meas_depart(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_depart)


if __name__ == '__main__':
	app = QApplication([])
	stats = Calculator()
	stats.show()
	app.exec_()
	pass



