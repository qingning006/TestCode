# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QSmp.py
date    : 2023/2/19 20:08
desc    :
"""

from PyQt5.QtWidgets import QApplication, QWidget
from ui import ui_smp
from base.defformula import *


class Smp(QWidget, Formula):
    def __init__(self):
        # 实例化一个 Ui_MainWindow对象
        super().__init__()
        self.ui = ui_smp.Ui_Form()
        self.ui.setupUi(self)
        self.init_action_connect()

    # 初始化事件响应
    def init_action_connect(self):
        self.ui.thy_l.textChanged.connect(self.update_thyroid_vol)
        self.ui.thy_w.textChanged.connect(self.update_thyroid_vol)
        self.ui.thy_h.textChanged.connect(self.update_thyroid_vol)

        self.ui.cmbox_node_thy.currentIndexChanged.connect(self.update_thy_node_sel)
        self.ui.node_thy_l.textChanged.connect(self.update_node_thy_vol)
        self.ui.node_thy_w.textChanged.connect(self.update_node_thy_vol)
        self.ui.node_thy_h.textChanged.connect(self.update_node_thy_vol)

    def update_thyroid_vol(self):
        self.update_vol_3d(self.ui.thy_l, self.ui.thy_w, self.ui.thy_h, self.ui.thy_vol1, "甲状腺", Vol_Thy_479)
        self.update_vol_3d(self.ui.thy_l, self.ui.thy_w, self.ui.thy_h, self.ui.thy_vol2, "甲状腺", Vol_Thy_523)

    def update_thy_node_sel(self):
        self.ui.node_thy_h.setValue(0)
        self.ui.node_thy_l.setValue(0)
        self.ui.node_thy_w.setValue(0)

    def update_node_thy_vol(self):
        items = self.ui.cmbox_node_thy.currentText()
        print(items)
        self.update_vol_3d(self.ui.node_thy_h, self.ui.node_thy_l, self.ui.node_thy_w, self.ui.node_thy_vol, items)


if __name__ == '__main__':
    app = QApplication([])
    stats = Smp()
    stats.show()
    app.exec_()
    pass
