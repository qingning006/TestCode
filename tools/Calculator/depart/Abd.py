# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QAbd.py
date    : 2023/2/19 20:08
desc    :
"""
from PyQt5.QtWidgets import QApplication, QWidget
from ui import ui_abd
from base.defformula import Formula


class Abd(QWidget, Formula):
    def __init__(self):
        # 实例化一个 Ui_MainWindow对象
        super().__init__()
        self.ui = ui_abd.Ui_Form()
        self.ui.setupUi(self)

        self.init_action_connect()

    def init_action_connect(self):
        self.ui.double_gall_l.textChanged.connect(self.update_gall_vol)
        self.ui.double_gall_w.textChanged.connect(self.update_gall_vol)

        self.ui.double_kidney_h.textChanged.connect(self.update_kidney_vol)
        self.ui.double_kidney_l.textChanged.connect(self.update_kidney_vol)
        self.ui.double_kidney_w.textChanged.connect(self.update_kidney_vol)

        self.ui.double_bladder_h.textChanged.connect(self.update_bladder_vol)
        self.ui.double_bladder_l.textChanged.connect(self.update_bladder_vol)
        self.ui.double_bladder_w.textChanged.connect(self.update_bladder_vol)

        self.ui.double_renal_d1.textChanged.connect(self.update_renal_dist_radio)
        self.ui.double_renal_d2.textChanged.connect(self.update_renal_dist_radio)
        self.ui.double_renal_a1.textChanged.connect(self.update_renal_area_radio)
        self.ui.double_renal_a2.textChanged.connect(self.update_renal_area_radio)

        self.ui.double_aorta_d1.textChanged.connect(self.update_aorta_dist_radio)
        self.ui.double_aorta_d2.textChanged.connect(self.update_aorta_dist_radio)
        self.ui.double_aorta_a1.textChanged.connect(self.update_aorta_area_radio)
        self.ui.double_aorta_a2.textChanged.connect(self.update_aorta_area_radio)

    def update_gall_vol(self):
        # 更新胆囊体积
        self.update_vol_3d(self.ui.double_gall_l, self.ui.double_gall_w, self.ui.double_gall_w, self.ui.double_gall_vol, "胆囊")

    def update_kidney_vol(self):
        # 更新肾脏体积
        self.update_vol_3d(self.ui.double_kidney_l, self.ui.double_kidney_h, self.ui.double_kidney_w, self.ui.double_kidney_vol, "肾脏")

    def update_bladder_vol(self):
        # 更新膀胱体积
        self.update_vol_3d(self.ui.double_bladder_l, self.ui.double_bladder_h, self.ui.double_bladder_w, self.ui.double_bladder_vol, "膀胱")

    def update_renal_dist_radio(self):
        self.update_narrow_radio(self.ui.double_renal_d1, self.ui.double_renal_d2, self.ui.double_renal_d_radio, "肾动脉狭窄距离比")

    def update_renal_area_radio(self):
        self.update_narrow_radio(self.ui.double_renal_a1, self.ui.double_renal_a2, self.ui.double_renal_a_radio, "肾动脉狭窄面积比")

    def update_aorta_dist_radio(self):
        self.update_narrow_radio(self.ui.double_aorta_d1, self.ui.double_aorta_d2, self.ui.double_aorta_d_radio, "主动脉狭窄距离比")

    def update_aorta_area_radio(self):
        self.update_narrow_radio(self.ui.double_aorta_a1, self.ui.double_aorta_a2, self.ui.double_aorta_a_radio, "主动脉狭窄面积比")


if __name__ == '__main__':
    app = QApplication([])
    stats = Abd()
    stats.show()
    app.exec_()
    pass
