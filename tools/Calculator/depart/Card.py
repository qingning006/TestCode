# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: QCard.py
date    : 2023/2/19 20:08
desc    :
"""

import os.path
import xlrd
import math

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QAbstractItemView
from PyQt5 import QtCore

from ui import ui_card, ui_zscore
from base.base import Base, DefColor


class Card(QWidget, Base):
    def __init__(self):
        # 实例化一个 Ui_MainWindow对象
        super().__init__()
        self.ui = ui_card.Ui_Form()
        self.ui.setupUi(self)


class ZScore(QWidget, Base):
    def __init__(self):
        # 实例化一个 Ui_MainWindow对象
        super().__init__()
        self.ui = ui_zscore.Ui_Form()
        self.ui.setupUi(self)

        self.init_2008_bsa()
        self.init_2008_table()
        self.init_2013_bsa()
        self.init_2013_table()

    def init_2008_bsa(self):
        self.ui.label_2008_bsa_formula.setText(f"BSA = 0.024265 * H(cm)^0.3964 * Wt(kg)^0.5378 ")
        self.ui.double_2008_height.textChanged.connect(self.update_2008_bsa)
        self.ui.double_2008_weight.textChanged.connect(self.update_2008_bsa)

    def update_2008_bsa(self):
        self.ui.double_2008_bsa.setValue(0.0)
        w = self.ui.double_2008_weight.value()
        h = self.ui.double_2008_height.value()
        bsa = 0.024265 * pow(h, 0.3964) * pow(w, 0.5378)
        # bsa = str('{:.3f}'.format(bsa))  # 格式化bsa结果
        self.ui.double_2008_bsa.setValue(bsa)
        self.log.info(f"心脏Z评分 Pettersen 2008，身高{h}cm，体重{w}kg， BSA：{bsa}cm2")
        # BSA改变，整个表都要更新
        self.update_2008_table()

    def init_2008_table(self):
        # 获取根目录
        path_2008 = os.getcwd() + '/conf/ZScore.xls'
        path_2008 = r'./conf/ZScore.xls'
        if os.path.exists(path_2008) is False:
            self.log.warring(f"Z评分文件不存在：{path_2008}")
            # 以下路径仅为调试使用
            path_2008 = f'E:\\gitcode\\TestCode\\tools\\Calculator\\conf\\ZScore.xls'
            if os.path.exists(path_2008) is False:
                # self.log.warring(f"Z评分文件不存在：{path_2008}")
                return

        # 打开excel表格
        data_excel = xlrd.open_workbook(path_2008)
        table = data_excel.sheet_by_name(sheet_name='Pettersen 2008')  # 通过名称获取
        # excel工作表的行列操作
        n_rows = table.nrows  # 获取该sheet中的有效行数
        n_cols = table.ncols  # 获取该sheet中的有效列数
        print(n_rows, n_cols)
        self.ui.table_2008.setRowCount(n_rows-1)  # -1为减掉表头行
        self.ui.table_2008.setColumnCount(n_cols)
        self.ui.table_2008.setShowGrid(True)

        # 设置表头行+数据行
        self.ui.table_2008.setHorizontalHeaderLabels(table.row_values(rowx=0))
        meas_col = 3  # 3列无数据列：实测值，Z0， Z
        # 获取excel数据，填入表格中
        for row in range(1, n_rows):
            for col in range(0, n_cols):
                item = QTableWidgetItem(str(table.cell_value(rowx=row, colx=col)))
                item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                # 公式数据列
                if col != n_cols - meas_col:  #只有测量值所在列可以编辑
                    item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)  # 设置单元格不可编辑
                # 测量值和计算值列
                else:
                    pass
                self.ui.table_2008.setItem(row - 1, col, item)  # -1为去掉表头行

        # 设置行和列的大小设为与内容相匹配
        self.ui.table_2008.resizeColumnsToContents()
        self.ui.table_2008.resizeRowsToContents()
        # 计算相关的3列（实测值，Z0， Z）设置宽度为100
        for col in range(n_cols - meas_col, n_cols):
            self.ui.table_2008.setColumnWidth(col, 100)
        # 合并单元格:单元格的行，列位置，合并行数，合并列数
        self.ui.table_2008.setSpan(0, 0, 14, 1)  # 2D
        self.ui.table_2008.setSpan(14, 0, 7, 1)  # M
        # 设置选中形式为选中一行
        self.ui.table_2008.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置信号函数
        self.ui.table_2008.cellChanged.connect(self.update_2008_row)
        self.color_normal = self.ui.table_2008.item(1, 1).background().color().getRgb()

    def update_2008_row(self, row, col):
        """
        更新2008公式某一个测量项的Z和Z0
        :param row: 发生变化的单元格所在行
        :param col: 发生变化的单元格所在列
        :return: Z0 和 Z
        """
        print(f"数值变化单元格：{row}, {col} ")
        # 判断变化行，避免死循环
        if self.ui.table_2008.horizontalHeaderItem(col).text() == "实测值(mm)":
            β0 = float(self.ui.table_2008.item(row, 3).text())  # β0在第3行
            β1 = float(self.ui.table_2008.item(row, 4).text())  # β1
            β2 = float(self.ui.table_2008.item(row, 5).text())  # β2
            β3 = float(self.ui.table_2008.item(row, 6).text())  # β3
            mse = float(self.ui.table_2008.item(row, 7).text())  # β3
            bsa = self.ui.double_2008_bsa.value()
            # Z0与测量值无关，更新Z0
            value_z0 = β0 + β1 * bsa + β2 * pow(bsa, 2) + β3 * pow(bsa, 3)
            value_z0 = '{:.3f}'.format(value_z0)
            value_z = 0
            self.ui.table_2008.item(row, col + 1).setText(str(value_z0))  # Z0
            # self.ui.table_2008.item(row, col+1).setBackground(self.color.HighLight)
            # 测量值为空清空Z值，不为空更新计算Z值
            if self.ui.table_2008.item(row, col).text() == "":
                self.ui.table_2008.item(row, col + 2).setText("")
            # self.ui.table_2008.item(row, col+2).setBackground(self.color.HighLight)
            else:
                meas = float(self.ui.table_2008.item(row, col).text())
                data = math.log(meas)
                data = pow(mse, 0.5)
                value_z = ((math.log(meas)) - float(value_z0)) / (pow(mse, 0.5))
                value_z = '{:.3f}'.format(value_z)
                self.ui.table_2008.item(row, col + 2).setText(str(value_z))  # Z
                meas = self.ui.table_2008.item(row, col).text()
                item = self.ui.table_2008.item(row, 1).text()
                self.log.info(
                    f"心脏Z评分Pettersen 2008：BSA：{bsa}m2，{item}: {meas}mm,{item}-Z0:{value_z0}, {item}-Z:{value_z}")
            print(value_z0, value_z)
            return value_z0, value_z

    def update_2008_table(self):
        """
        更新2008公式所有测量项的Z和Z0（BSA发生改变时需要更新整个表）
        """
        row_count = self.ui.table_2008.rowCount()
        meas_index = 9  # 测量值所在列为第9列
        for row in range(0, row_count):
            self.update_2008_row(row, meas_index)

    def init_2013_bsa(self):
        self.ui.label_2013_bsa_formula.setText(f"BSA = 0.0061 * H(cm) + 0.0128 * Wt(kg) - 0.1529 ")
        self.ui.double_2013_height.textChanged.connect(self.update_2013_bsa)
        self.ui.double_2013_weight.textChanged.connect(self.update_2013_bsa)

    def update_2013_bsa(self):
        self.ui.double_2013_bsa.setValue(0.0)
        w = self.ui.double_2013_weight.value()
        h = self.ui.double_2013_height.value()
        bsa = 0.0061 * h + 0.0128 * w - 0.1529
        # bsa = str('{:.3f}'.format(bsa))  # 格式化bsa结果
        self.ui.double_2013_bsa.setValue(bsa)
        self.log.info(f"心脏Z评分 BeiXia 2013，身高{h}cm，体重{w}kg， BSA：{bsa}cm2")
        # BSA改变，整个表都要更新
        self.update_2013_table()


    def init_2013_table(self):
        # 获取根目录
        path_2013 = os.getcwd() + '/conf/ZScore.xls'
        path_2013 = r'./conf/ZScore.xls'
        if os.path.exists(path_2013) is False:
            self.log.warring(f"Z评分文件不存在：{path_2013}")
            # 以下路径仅为调试使用
            path_2013 = f'E:\\gitcode\\TestCode\\tools\\Calculator\\conf\\ZScore.xls'
            if os.path.exists(path_2013) is False:
                # self.log.warring(f"Z评分文件不存在：{path_2013}")
                return

        # 打开excel表格
        data_excel = xlrd.open_workbook(path_2013)
        table = data_excel.sheet_by_name(sheet_name='Bei Xia 2013')  # 通过名称获取
        # excel工作表的行列操作
        n_rows = table.nrows  # 获取该sheet中的有效行数
        n_cols = table.ncols  # 获取该sheet中的有效列数
        print(n_rows, n_cols)
        self.ui.table_2013.setRowCount(n_rows-1)  # -1为减掉表头行
        self.ui.table_2013.setColumnCount(n_cols)
        self.ui.table_2013.setShowGrid(True)

        # 设置表头行+数据行
        self.ui.table_2013.setHorizontalHeaderLabels(table.row_values(rowx=0))
        meas_col = 3  # 3列无数据列：实测值，Z0， Z
        # 获取excel数据，填入表格中
        for row in range(1, n_rows):
            for col in range(0, n_cols):
                item = QTableWidgetItem(str(table.cell_value(rowx=row, colx=col)))
                item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                # 公式数据列
                if col != n_cols - meas_col:  #只有测量值所在列可以编辑
                    item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)  # 设置单元格不可编辑
                # 测量值和计算值列
                else:
                    pass
                self.ui.table_2013.setItem(row - 1, col, item)  # -1为去掉表头行

        # 设置行和列的大小设为与内容相匹配
        self.ui.table_2013.resizeColumnsToContents()
        self.ui.table_2013.resizeRowsToContents()
        self.ui.table_2013.setColumnWidth(1, 100)
        #self.ui.table_2013.setColumnHidden(7, True)
        # 计算相关的3列（实测值，Z0， Z）设置宽度为100
        for col in range(n_cols - meas_col, n_cols):
            self.ui.table_2013.setColumnWidth(col, 80)
        # 合并单元格:单元格的行，列位置，合并行数，合并列数
        self.ui.table_2013.setSpan(0, 0, 5, 1)  # Simp
        self.ui.table_2013.setSpan(5, 0, 17, 1)  # M
        self.ui.table_2013.setSpan(22, 0, 3, 1)  # M
        self.ui.table_2013.setSpan(25, 0, 23, 1)  # M
        self.ui.table_2013.setSpan(48, 0, 8, 1)  # M
        # 设置选中形式为选中一行
        self.ui.table_2013.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置信号函数
        self.ui.table_2013.cellChanged.connect(self.update_2013_row)
        self.color_normal = self.ui.table_2013.item(1, 1).background().color().getRgb()


    def update_2013_row(self, row, col):
        """
        更新2013公式某一个测量项的Z和Z0
        :param row: 发生变化的单元格所在行
        :param col: 发生变化的单元格所在列
        :return: Z0 和 Z
        """
        print(f"数值变化单元格：{row}, {col} ")
        # 判断变化行，避免死循环
        if self.ui.table_2013.horizontalHeaderItem(col).text() == "实测值":
            β0 = float(self.ui.table_2013.item(row, 3).text())  # β0在第3行
            β1 = float(self.ui.table_2013.item(row, 4).text())  # β1

            bsa = self.ui.double_2013_bsa.value()
            value_z, value_z0 = 0, 0
            # Z0与测量值无关，更新Z0
            if 22<=row<=24 :  # 冠状动脉测量
                β2 = float(self.ui.table_2013.item(row, 5).text())  # β2
                value_z0 = β0 + β1 * pow(bsa, 0.5) + β2 * bsa
            else:  # 非冠状动脉测量
                value_z0 = β0 + β1 * math.log(bsa)
            value_z0 = '{:.3f}'.format(value_z0)
            self.ui.table_2013.item(row, col + 1).setText(str(value_z0))  # Z0
            # self.ui.table_2008.item(row, col+1).setBackground(self.color.HighLight)

            # 测量值为空清空Z值，不为空更新计算Z值
            if self.ui.table_2013.item(row, col).text() == "":
                self.ui.table_2013.item(row, col + 2).setText("")
            # self.ui.table_2008.item(row, col+2).setBackground(self.color.HighLight)
            else:
                meas = float(self.ui.table_2013.item(row, col).text())
                rmse = float(self.ui.table_2013.item(row, 6).text())
                value_z0 = float(value_z0)
                if 22 <= row <= 24:  # 冠状动脉测量
                    value_z = (meas - value_z0)/rmse
                else:  # 非冠状动脉测量
                    value_z = (math.log(meas) - value_z0)/rmse
                value_z = '{:.3f}'.format(value_z)
                self.ui.table_2013.item(row, col + 2).setText(str(value_z))  # Z
                meas = self.ui.table_2013.item(row, col).text()
                item = self.ui.table_2013.item(row, 1).text()
                self.log.info(f"心脏Z评分BeiXia 2013：BSA：{bsa}m2，{item}: {meas}mm,{item}-Z0:{value_z0}, {item}-Z:{value_z}")
            print(value_z0, value_z)
            return value_z0, value_z


    def update_2013_table(self):
        """
        更新2013公式所有测量项的Z和Z0（BSA发生改变时需要更新整个表）
        """
        row_count = self.ui.table_2013.rowCount()
        meas_index = 10  # 测量值所在列为第10列
        for row in range(0, row_count):
            self.update_2013_row(row, meas_index)


if __name__ == '__main__':
    app = QApplication([])
    stats = ZScore()
    stats.show()
    app.exec_()
    pass
