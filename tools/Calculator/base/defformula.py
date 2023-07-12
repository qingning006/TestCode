# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: calformula.py
date    : 2023/2/23
desc    : 
"""
import math

# 体积公式
import re
import glob
import pandas as pd
from base.base import Base

# 公式系数定义
Vol_Normal = math.pi / 6
Vol_Thy_479 = 0.479
Vol_Thy_523 = 0.523


class Formula(Base):
    def vol_3d(self, d1, d2, d3, radio=Vol_Normal):
        return float('{:.3f}'.format(d1 * d2 * d3 * radio))

    def update_vol_3d(self, dist1, dist2, dist3, vol, info=None, coeff=Vol_Normal):
        """
        更新三径法体积结果值
        :param dist1: 三径法的长宽高控件，浮点型编辑框
        :param dist2: 三径法的长宽高控件，浮点型编辑框
        :param dist3: 三径法的长宽高控件，浮点型编辑框
        :param vol: 体积控件，浮点型编辑框
        :param info: 日志信息
        :param coeff: 倍数，默认是π/6
        :return: 浮点型体积结果值
        """
        d1, d2, d3 = dist1.value(), dist2.value(), dist3.value()
        v1 = self.vol_3d(d1, d2, d3, coeff)
        vol.setValue(v1)
        if v1 != 0:
            self.log.info(f' {info}体积：{d1} * {d2} * {d3} * {coeff} = {v1}')

    def update_narrow_radio(self, edit1, edit2, edit_radio, info):
        """
        更新狭窄比：距离比，面积比
        :param edit1: 控件1，浮点型编辑框
        :param edit2: 控件2，浮点型编辑框
        :param edit_radio: 狭窄比，浮点型编辑框
        :param info: 日志信息
        :return:
        """
        v1 = edit1.value()
        v2 = edit2.value()
        radio = math.fabs(v1-v2)/max(v1, v2) * 100
        edit_radio.setValue(radio)
        self.log.info(f' {info}：{v1}/{v2} = {radio}%')




class FormulaOB:
    def EFW_AC_Campbell(self,AC):
        """
        Equation    EFW=e^(0.282*AC-0.00331*AC^2-4.564)*1000
        Input   Output
        Unit	cm	g
        min	21	903
        max	40	4137
        Deviatiom   14.60%
        :param AC: 单位为cm，有效值范围为21~40cm
        :return: 胎重、误差
        """
        if 21<=AC<=40:
            value = math.exp(0.282*AC-0.00331*AC**2-4.564)*1000
            return value, value*0.146
        else:
            return "/", r"21<=AC<=40"

    def EFW_AC_BPD_Hadlock(self,AC,BPD):
        """
        EFW=10^(1.1134+0.05845*AC-0.000604*AC^2-0.007365*BPD^2+0.000595*AC*BPD+0.1694*BPD)
        Input		Output
        AC	BPD	EFW
        Unit	cm	cm	g
        :param AC:单位为cm
        :param BPD:单位为cm
        :return:胎重、误差（本公式无误差计算）
        """
        value = 10**(1.1134+0.05845*AC-0.000604*AC**2-0.007365*BPD**2+0.000595*AC*BPD+0.1694*BPD)
        return value, "/"

    def EFW_AC_BPD_Merz(self,AC,BPD):
        """
        EFW=-3200.40479+157.07186*AC+15.90391*BPD^2
        Input	Output
        AC	BPD	EFW
        Unit	cm	cm	g
        min	21.8	7
        max	36.5	10.5
        :param AC: 单位为cm
        :param BPD: 单位为cm
        :return:胎重、误差（本公式无误差计算）
        """
        if 21.8<=AC<=36.5 and 7<=BPD<=10.5:
            value = -3200.40479+157.07186*AC+15.90391*BPD**2
            return value, "/"
        else:
            return "/", r"21.8<=AC<=36.5 and 7<=BPD<=10.5"

    def EFW_AC_BPD_Shepard(self,AC,BPD):
        """
        EFW=10^(-1.7492+0.166*BPD+0.046*AC-0.002646*AC*BPD)*1000
        Input	Output
        AC	BPD	EFW
        cm	cm	g
        15.50	3.1	224
        40.00	10.0	4900
        :param AC:cm
        :param BPD:cm
        :return:
        """
        if 15.50<=AC<=40.00 and 3.1<=BPD<=10.0:
            value = 10**(-1.7492+0.166*BPD+0.046*AC-0.002646*AC*BPD)*1000
            return value, "/"
        else:
            return "/", r"15.50<=AC<=40.00 and 3.1<=BPD<=10.0"
        pass

    def EFW_AC_FL_Hadlock1(self,AC,FL):
        """
        EFW=10^(1.304+0.05281*AC+0.1938*FL-0.004*AC*FL)
        Input	Output
        AC	FL	EFW
        Unit	cm	cm	g
        min
        max
        SD=15.4%
        :param AC:cm
        :param FL:cm
        :return:
        """
        value = 10 ** (1.304+0.05281*AC+0.1938*FL-0.004*AC*FL)
        return value, value*0.154

    def EFW_AC_HC_INTERGROWTH(self,AC ,HC):
        """
        ln(EFW)=5.084820–54.06633×(AC/100)^3–95.80076×(AC/100)^3×ln(AC/100)+3.136370×(HC/100)
        Input	Output
        AC	HC	EFW
        Unit	cm	cm	g
        :param AC:
        :param HC:
        :return:
        """
        value = math.exp(5.084820-54.06633*(AC/100)**3-95.80076*(AC/100)**3*math.log1p(AC/100)+3.136370*(HC/100))
        return value, "/"

    def EFW_BPD_AC_FL_Hadlock2(self,BPD,AC,FL):
        """
        EFW=10^(1.335-0.0034*AC*FL+0.0316*BPD+0.0457*AC+0.1623*FL)
        Input	Output
        BPD	AC	FL	EFW
        Unit	cm	cm	cm	g
        2SD=14.6%
        :param BPD:
        :param AC:
        :param FL:
        :return:
        """
        value = 10**(1.335-0.0034*AC*FL+0.0316*BPD+0.0457*AC+0.1623*FL)
        return value, value*0.146


    def EFW_BPD_APTD_TTD_FL_Shinozuka1(self,BPD,APTD,TTD,FL):
        """
        EFW=1.07*BPD^3+3.42*APTD*TTD*FL
        Input	Output
        BPD	APTD	TTD	FL	EFW
        cm	cm	cm	cm	g
        :param BPD:
        :param APTD:
        :param TTD:
        :param FL:
        :return:
        """
        value = 1.07*BPD**3+3.42*APTD*TTD*FL
        return value, "/"

    def EFW_BPD_APTD_TTD_FL_Tokyo(self,BPD,APTD,TTD,FL):
        """
        EFW=1.07*BPD^3+3.42*APTD*TTD*FL
        Input	Output
        BPD	APTD	TTD	FL	EFW
        Unit	cm	cm	cm	cm	g
        :param BPD:
        :param APTD:
        :param TTD:
        :param FL:
        :return:
        """
        value = 1.07*BPD**3+3.42*APTD*TTD*FL
        return value, "/"

    def EFW_BPD_APTD_TTD_LV_Shinozuka3(self,BPD,APTD,TTD,LV):
        """
        EFW=1.07*BPD^3+2.91*APTD*TTD*FL
        Input	Output
        BPD	APTD	TTD	LV	EFW
        cm	cm	cm	cm	g
        :param BPD:
        :param APTD:
        :param TTD:
        :param LV:
        :return:
        """
        value = 1.07*BPD**3+2.91*APTD*TTD*LV
        return value, "/"


    def EFW_BPD_FL_AC_JSUM(self,BPD,FL,AC):
        """
        EFW=1.07*BPD^3+0.30*AC^2*FL
        Input	output
        BPD	FL	AC	EFW
        cm	cm	cm	g
        :param BPD:
        :param FL:
        :param AC:
        :return:
        """
        value = 1.07*BPD**3+0.30*AC**2*FL
        return value, "/"

    def EFW_BPD_FL_AC_Shinozuka2(self,BPD,FL,AC):
        """
        EFW=1.07*BPD^3+0.30*AC^2*FL
        Input	output
        BPD	FL	AC	EFW
        Unit	cm	cm	cm	g
        :param BPD:
        :param FL:
        :param AC:
        :return:
        """
        value = 1.07*BPD**3+0.30*AC**2*FL
        return value, "/"


    def EFW_BPD_FTA_FL_Osaka(self, BPD, FTA, FL):
        """
        EFW=6.3+1.25647*BPD^3+3.50665*FTA*FL
        Input	Output
        BPD	FTA	FL	EFW
        cm	cm2	cm	g
        :param BPD:
        :param FTA:
        :param FL:
        :return:
        """
        value = 6.3+1.25647*BPD**3+3.50665*FTA*FL
        return value, "/"


    def EFW_BPD_HC_AC_FL_Hadlock4(self,BPD,HC,AC,FL):
        """
        EFW=10^(1.3596-0.00386*AC*FL+0.0064*HC+0.00061*BPD*AC+0.0424*AC+0.174*FL)
        Input	Output
        BPD	HC	AC	FL	EFW
        Unit	cm	cm	cm	cm	g
        SD=14.6%
        :param BPD:
        :param HC:
        :param AC:
        :param FL:
        :return:
        """
        value = 10**(1.3596-0.00386*AC*FL+0.0064*HC+0.00061*BPD*AC+0.0424*AC+0.174*FL)
        return value, value*0.146

    def EFW_BPD_MAD_Persson2(self,BPD,MAD):
        """
        EFW=(BPD*10)^1.321*(MAD*10)^1.833*10^(-2.830)
        Input	output
        BPD	MAD	EFW
        Unit	cm	cm	g
        :param BPD:
        :param MAD:
        :return:
        """
        value = (BPD*10)**1.321*(MAD*10)**1.833*10**(-2.830)
        return value, "/"


    def EFW_BPD_MAD_FL_Persson1(self, BPD, MAD, FL):
        """
        Equation	EFW=(BPD*10)^0.972*(MAD*10)^1.743*(FL*10)^0.367*10^(-2.646)
        Input	output
        BPD	MAD	FL	EFW
        Unit	cm	cm	cm	g
        :param BPD:
        :param MAD:
        :param FL:
        :return:
        """
        value = (BPD*10)**0.972*(MAD*10)**1.743*(FL*10)**0.367*10**(-2.646)
        return value, "/"


    def EFW_BPD_TTD_Hansmann(self, BPD, TTD):
        """
        EFW=(-1.05775*BPD+0.649145*TTD+0.0930707*BPD^2-0.020562*TTD^2+0.515263)*1000
        Deviation	14.6%
        :param BPD:
        :param TTD:
        :return:
        """
        value = (-1.05775*BPD+0.649145*TTD+0.0930707*BPD**2-0.020562*TTD**2+0.515263) *1000
        return value, value*0.146


    def EFW_HC_AC_FL_Hadlock3(self,HC,AC,FL):
        """
        EFW=10^(1.326-0.00326*AC*FL+0.0107*HC+0.0438*AC+0.158*FL)
        Input
        HC	AC	FL
        cm	cm	cm
        SD=14.8%
        :param HC:
        :param AC:
        :param FL:
        :return:
        """
        value = 10**(1.326-0.00326*AC*FL+0.0107*HC+0.0438*AC+0.158*FL)
        return value, value*0.148

    def EFW_HC_AC_FL_Schild(self,HC,AC,FL):
        """
        EFW=5381.193+150.324*HC+2.069*FL^3+0.0232*AC^3-6235.478*log(HC)
        Input	output
        HC	AC	FL	EFW
        Unit	cm	cm	cm	g
        :param HC:cm
        :param AC:cm
        :param FL:cm
        :return:
        """
        value = 5381.193+150.324*HC+2.069*FL**3+0.0232*AC**3-6235.478*math.log10(HC)
        return value, "/"


class TableMerge:
    def get_fml_name(self,path):
        str = '.*_'+item+'_(.*)_.*_.*_'
        #str = r'.*_(.*)_.*_X10'
        patterm = re.compile(str)
        fml = patterm.findall(path)[0]
        return fml

    def merge(self, dir, item):
        file_new = dir + r'.xlsx'
        writer = pd.ExcelWriter(file_new)
        file_type = dir + r'\*.xlsx'
        file_list = glob.glob(file_type)
        print("***",file_new, file_type)
        #file_new = f"{dir}\{item}.xlsx"
        #file_list = glob.glob(r"F:\12-开立\计算公式\孕龄表格\AC\*.xlsx")
        for file in file_list:
            df = pd.read_excel(file)
            # 提取文件名
            fname = self.get_fml_name(file)
            print(file, fname)
            df.to_excel(writer, sheet_name=fname, index=False)
        writer.save()


if __name__ == '__main__':
    dir = r'F:\12-开立\计算公式\孕龄表格\AC'
    item = 'AC'
    TableMerge().merge(dir, item)