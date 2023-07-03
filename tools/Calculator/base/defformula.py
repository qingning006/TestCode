# -*- coding: utf-8 -*-
"""
author  : YangNana
filename: calformula.py
date    : 2023/2/23
desc    : 
"""
import math

# 体积公式
def vol_1d(d1, radio=1):
	return vol_3d(d1, d1, d1, radio)

def vol_2d(d1, d2, radio=1):
	return vol_3d(d1, d2, d2, radio)

def vol_3d(d1, d2, d3, radio=1):
	return '{:.3f}'.format(d1*d2*d3*radio)

#class FormulaOB:

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
            return None,r"21<=AC<=40"

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
            return None, r"21.8<=AC<=36.5 and 7<=BPD<=10.5"

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
            return None, r"15.50<=AC<=40.00 and 3.1<=BPD<=10.0"
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
        return value

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