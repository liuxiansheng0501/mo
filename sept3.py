#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/3 16:42
# @Author  : liulijun
# @Site    : 
# @File    : sept3.py
# @Software: PyCharm

import pandas as pd
from openpyxl.workbook import Workbook

def adj_matrix():

    adj_matrix= [ [0 for i in range(24)] for i in range(24)]
    dframe = pd.read_excel("D:/mo/9.3/AllPanelMutDis.PASS_Fc_MAF_SNVs.overlap2_hcSNVs.MutNumberunion.xlsx", sheetname="AllPanelMutDis.PASS_Fc_MAF_SNVs")
    gene_list=list(dframe.index)
    adj_matrix = pd.DataFrame(adj_matrix, columns=gene_list,index=gene_list)
    for patients in dframe.columns:
        for i in range(len(gene_list)):
            for j in range(i+1,len(gene_list)):
                if dframe[patients].iloc[i]>0 and dframe[patients].iloc[j]>0:
                    adj_matrix[gene_list[i]].loc[gene_list[j]] += 1
                    adj_matrix[gene_list[j]].loc[gene_list[i]] += 1

    adj_matrix.to_csv('D:/mo/9.3/adj_mat.csv')

    wb = Workbook()
    ws0 = wb.active
    for i in range(len(gene_list)):
        for j in range(i + 1, len(gene_list)):
            ws0.append([gene_list[i],gene_list[j],adj_matrix[gene_list[i]].loc[gene_list[j]]])
    file_path = "D:/mo/9.3/gene_mut_value.csv"
    wb.save(file_path)



if __name__=="__main__":
    adj_matrix()
