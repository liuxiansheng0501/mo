#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 13:56
# @Author  : liulijun
# @Site    : 
# @File    : matrix.py
# @Software: PyCharm
import copy
import pandas as pd

def matrix():
    matrix=[]
    data=[]
    for line in open("./10.20/All107PanelMutDis.PASS_Fc_Damages_SNVs.overlap2_hcSNVs.union(1).txt",'r'):
        data.append(line.split('	'))
    data = pd.DataFrame(data[1:], columns=data[0:1][0])

    patients=data.columns.tolist()[2:]
    geneset=list(set(data['Gene'].tolist()))

    for igene in geneset:
        imatrix=[]
        for patient in patients:
            num=0
            for value in data[data['Gene']==igene][patient].tolist():
                if ',' not in value:
                    if float(value)>0 and float(value) <=1:
                        num+=1
            imatrix.append(num)
        imatrix.append(sum(imatrix))
        matrix.append(imatrix)
    matrix_copy = copy.deepcopy(matrix)
    patients.append('ALL')
    matrix = pd.DataFrame(matrix,columns=patients)
    imatrix=[]
    for ipatient in patients:
        imatrix.append(sum(matrix[ipatient].tolist()))
    geneset.append('ALL')
    matrix_copy.append(imatrix)
    matrix_copy=pd.DataFrame(matrix_copy,columns=patients,index=geneset)
    matrix_copy.to_excel("./10.20/matrix.xlsx")

if __name__=="__main__":
    matrix()