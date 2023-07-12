# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QPed.py
date    : 2023/2/19 20:08
desc    :
"""

from PyQt5.QtWidgets import QApplication, QWidget
from ui import ui_ped
from base.defformula import Formula


class Ped(QWidget, Formula):
    def __init__(self):
        # 实例化一个 Ui_MainWindow对象
        super().__init__()
        self.ui = ui_ped.Ui_Form()
        self.ui.setupUi(self)
        self.init_action_connect()

    # 初始化事件响应
    def init_action_connect(self):
        self.ui.spinBox_year.textChanged.connect(self.update_graf)
        self.ui.spinBox_month.textChanged.connect(self.update_graf)
        self.ui.double_a.textChanged.connect(self.update_graf)
        self.ui.double_b.textChanged.connect(self.update_graf)
        self.ui.double_d1.textChanged.connect(self.update_fhc)
        self.ui.double_d2.textChanged.connect(self.update_fhc)

    def update_graf(self):
        # 先清空分型和描述
        self.ui.text_type.setText("")
        self.ui.text_desc_graf.setText("")
        self.ui.text_desc_graf_en.setText("")
        # 获取角度值
        age_y = self.ui.spinBox_year.value()
        age_m = self.ui.spinBox_month.value()
        age = age_y * 12 + age_m
        angle_a = self.ui.double_a.value()
        angle_b = self.ui.double_b.value()
        print(age, angle_a, angle_b)
        # 结果分型
        str_type, str_desc, str_desc_en = "", "", ""
        if angle_a >= 60 and angle_b <= 55:
            str_type = "Ia"
            str_desc = "成熟髋关节"
            str_desc_en = "mature hip"
        elif angle_a >= 60 and angle_b > 55:
            str_type = "Ib"
            str_desc = "成熟髋关节"
            str_desc_en = "mature hip"
        elif 55 <= angle_a <= 59 and 6 <= age <= 12:
            str_type = "IIa(+)"
            str_desc = "生理性不成熟"
            str_desc_en = "physiological immature"
        elif 50 <= angle_a < 55 and 6 <= age <= 12:
            str_type = "IIa(-)"
            str_desc = "成熟缺陷"
            str_desc_en = "maturational deficite"
        elif 50 <= angle_a <= 59 and age > 12:
            str_type = "IIb"
            str_desc = "骨化延迟"
            str_desc_en = "delay of ossification"
        elif 50 <= angle_a <= 59 and age < 6:
            str_type = "IIa/IIb"
            str_desc = "(结果窗不显示)"
        elif 43 <= angle_a <= 49 and angle_b <= 77:
            str_type = "IIc"
            str_desc = "可能发生脱位"
            str_desc_en = "decentring can occur"
        elif 43 <= angle_a <= 49 and angle_b > 77:
            str_type = "D"
            str_desc = "即将脱位"
            str_desc_en = "about to decentre"

        self.ui.text_type.setText(str_type)
        self.ui.text_desc_graf.setText(str_desc)
        self.ui.text_desc_graf_en.setText(str_desc_en)
        self.log.info(f' 小儿髋关节Graf分型：α：{angle_a}°, β：{angle_b}°,  分型：{str_type},  描述：{str_desc}, {str_desc_en}')

    def update_fhc(self):
        # 先清空分型和描述
        self.ui.text_dradio.setText("")
        self.ui.text_desc_fhc.setText("")
        self.ui.text_desc_fhc_en.setText("")
        # 获取d、D值，计算d/D比率
        dist_d1 = self.ui.double_d1.value()
        dist_d2 = self.ui.double_d2.value()
        if dist_d2 == 0.0:
            return
        dist_radio = float(dist_d1/dist_d2)
        # 结果分型
        str_desc,str_desc_en = "",""
        if dist_radio>58:
            str_desc = "发育正常"
            str_desc_en = "Normal"
        elif 33 <= dist_radio <= 58:
            str_desc = "部分正常部分异常"
            str_desc_en = "Partial Normal"
        elif dist_radio<33:
            str_desc = "发育异常"
            str_desc_en = "Abnormal"
        str_radio = "%.3f" % dist_radio
        self.ui.text_dradio.setText(str_radio)
        self.ui.text_desc_fhc.setText(str_desc)
        self.ui.text_desc_fhc_en.setText(str_desc_en)
        self.log.info(f' 小儿髋关节FHC分型：d：{dist_d1}°, D：{dist_d2}°, FHC：{str_radio} , 描述：{str_desc}, {str_desc_en}')


if __name__ == '__main__':
    app = QApplication([])
    stats = Ped()
    stats.show()
    app.exec_()
    pass
