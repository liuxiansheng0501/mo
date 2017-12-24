#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 13:37
# @Author  : liulijun
# @Site    : 
# @File    : stas.py
# @Software: PyCharm

import pandas as pd
import sys
import os

def fun1():
    #import
    Lxf_1D0=pd.read_csv("../Lxf_1D0_SNV.overlap2_hcSNVs.csv")
    Lxf_1D8=pd.read_csv("../Lxf_1D8_SNV.overlap2_hcSNVs.csv")
    Lxf_1D26=pd.read_csv("../Lxf_1D26_SNV.overlap2_hcSNVs.csv")
    Lxf_3D26=pd.read_csv("../Lxf_3D26_SNV.overlap2_hcSNVs.csv")

    #stas
    stasValueLxf_1D0=[]
    stasValueLxf_1D8=[]
    stasValueLxf_1D26=[]
    stasValueLxf_3D26=[]
    all=[]

    for type in [['C>G','G>C'],['C>A','G>T'],['C>T','G>A'],['A>G','T>C'],['A>C','T>G'],['A>T','T>A']]:
        stasValueLxf_1D0.append(len(Lxf_1D0[(Lxf_1D0['Basechange']==type[0])|(Lxf_1D0['Basechange']==type[1])])/len(Lxf_1D0))
        stasValueLxf_1D8.append(len(Lxf_1D8[(Lxf_1D8['Basechange']==type[0])|(Lxf_1D8['Basechange']==type[1])])/len(Lxf_1D8))
        stasValueLxf_1D26.append(len(Lxf_1D26[(Lxf_1D26['Basechange']==type[0])|(Lxf_1D26['Basechange']==type[1])])/len(Lxf_1D26))
        stasValueLxf_3D26.append(len(Lxf_3D26[(Lxf_3D26['Basechange']==type[0])|(Lxf_3D26['Basechange']==type[1])])/len(Lxf_3D26))

    all.append(stasValueLxf_1D0)
    all.append(stasValueLxf_1D8)
    all.append(stasValueLxf_1D26)
    all.append(stasValueLxf_3D26)
    all=pd.DataFrame(all,columns=['C>G','C>A','C>T','A>G','A>C','A>T'],index=['Lxf_1D0','Lxf_1D8','Lxf_1D26','Lxf_3D26'])

    #export
    all.to_csv('../Basechange_stas.csv')

    #extract
    Lxf_1D0=Lxf_1D0[(Lxf_1D0['ExonicFunc.refGene']=='synonymous SNV')|(Lxf_1D0['ExonicFunc.refGene']=='stopgain')|(Lxf_1D0['ExonicFunc.refGene']=='nonsynonymous SNV')]
    Lxf_1D8=Lxf_1D8[(Lxf_1D8['ExonicFunc.refGene']=='synonymous SNV')|(Lxf_1D8['ExonicFunc.refGene']=='stopgain')|(Lxf_1D8['ExonicFunc.refGene']=='nonsynonymous SNV')]
    Lxf_1D26=Lxf_1D26[(Lxf_1D26['ExonicFunc.refGene']=='synonymous SNV')|(Lxf_1D26['ExonicFunc.refGene']=='stopgain')|(Lxf_1D26['ExonicFunc.refGene']=='nonsynonymous SNV')]
    Lxf_3D26=Lxf_3D26[(Lxf_3D26['ExonicFunc.refGene']=='synonymous SNV')|(Lxf_3D26['ExonicFunc.refGene']=='stopgain')|(Lxf_3D26['ExonicFunc.refGene']=='nonsynonymous SNV')]

    #stas
    stasValueLxf_1D0=[]
    stasValueLxf_1D8=[]
    stasValueLxf_1D26=[]
    stasValueLxf_3D26=[]
    all=[]

    for type in [['C>G','G>C'],['C>A','G>T'],['C>T','G>A'],['A>G','T>C'],['A>C','T>G'],['A>T','T>A']]:
        stasValueLxf_1D0.append(len(Lxf_1D0[(Lxf_1D0['Basechange']==type[0])|(Lxf_1D0['Basechange']==type[1])])/len(Lxf_1D0))
        stasValueLxf_1D8.append(len(Lxf_1D8[(Lxf_1D8['Basechange']==type[0])|(Lxf_1D8['Basechange']==type[1])])/len(Lxf_1D8))
        stasValueLxf_1D26.append(len(Lxf_1D26[(Lxf_1D26['Basechange']==type[0])|(Lxf_1D26['Basechange']==type[1])])/len(Lxf_1D26))
        stasValueLxf_3D26.append(len(Lxf_3D26[(Lxf_3D26['Basechange']==type[0])|(Lxf_3D26['Basechange']==type[1])])/len(Lxf_3D26))

    all.append(stasValueLxf_1D0)
    all.append(stasValueLxf_1D8)
    all.append(stasValueLxf_1D26)
    all.append(stasValueLxf_3D26)
    all=pd.DataFrame(all,columns=['C>G','C>A','C>T','A>G','A>C','A>T'],index=['Lxf_1D0','Lxf_1D8','Lxf_1D26','Lxf_3D26'])

    #export
    all.to_csv('../ExonicFunc.refGene_stas.csv')

    #stas
    stasValueLxf_1D0=[]
    stasValueLxf_1D8=[]
    stasValueLxf_1D26=[]
    stasValueLxf_3D26=[]
    all=[]

    for type in [['C>G','G>C'],['C>A','G>T'],['C>T','G>A'],['A>G','T>C'],['A>C','T>G'],['A>T','T>A']]:
        stasValueLxf_1D0.append(len(Lxf_1D0[(Lxf_1D0['Basechange']==type[0])|(Lxf_1D0['Basechange']==type[1])]))
        stasValueLxf_1D8.append(len(Lxf_1D8[(Lxf_1D8['Basechange']==type[0])|(Lxf_1D8['Basechange']==type[1])]))
        stasValueLxf_1D26.append(len(Lxf_1D26[(Lxf_1D26['Basechange']==type[0])|(Lxf_1D26['Basechange']==type[1])]))
        stasValueLxf_3D26.append(len(Lxf_3D26[(Lxf_3D26['Basechange']==type[0])|(Lxf_3D26['Basechange']==type[1])]))

    all.append(stasValueLxf_1D0)
    all.append(stasValueLxf_1D8)
    all.append(stasValueLxf_1D26)
    all.append(stasValueLxf_3D26)
    all=pd.DataFrame(all,columns=['C>G','C>A','C>T','A>G','A>C','A>T'],index=['Lxf_1D0','Lxf_1D8','Lxf_1D26','Lxf_3D26'])

    #export
    all.to_csv('../ExonicFunc.refGene_stas_num.csv')

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files # 当前路径下所有非目录子文件

def read(file_name,name):
    data=[]
    for line in open("../"+name+"/"+file_name,'r'):
        data.append(line.split('	'))
    data = pd.DataFrame(data[1:], columns=data[0:1][0])
    return data

def ExonicFunc_prop(sourceData):
    # extract
    sourceData = sourceData[(sourceData['ExonicFunc.refGene'] == 'synonymous SNV') | (sourceData['ExonicFunc.refGene'] == 'stopgain') | (sourceData['ExonicFunc.refGene'] == 'nonsynonymous SNV')]
    # stas
    stasValue = []
    for type in [['A>C', 'T>G'],['A>G', 'T>C'], ['A>T', 'T>A'], ['C>A', 'G>T'], ['C>G', 'G>C'], ['C>T', 'G>A']]:
        stasValue.append(len(sourceData[(sourceData['Basechange'] == type[0]) | (sourceData['Basechange'] == type[1])]) / len(sourceData))
    return stasValue

def ExonicFunc_num(sourceData):
    # extract
    sourceData = sourceData[(sourceData['ExonicFunc.refGene'] == 'synonymous SNV') | (sourceData['ExonicFunc.refGene'] == 'stopgain') | (sourceData['ExonicFunc.refGene'] == 'nonsynonymous SNV')]
    # stas
    stasValue = []
    for type in [['A>C', 'T>G'],['A>G', 'T>C'], ['A>T', 'T>A'], ['C>A', 'G>T'], ['C>G', 'G>C'], ['C>T', 'G>A']]:
        stasValue.append(len(sourceData[(sourceData['Basechange'] == type[0]) | (sourceData['Basechange'] == type[1])]))
    return stasValue

def fun2(dir):
    name=dir.split('/')[-1]
    pro_list=[]
    num_list=[]
    filelist=file_name(dir)
    for ifile in filelist:
        data=read(ifile,name)
        pro_v=ExonicFunc_prop(data)
        num_v=ExonicFunc_num(data)
        pro_list.append(pro_v)
        num_list.append(num_v)
    pro_list = pd.DataFrame(pro_list, columns=['A>C','A>G',   'A>T', 'C>A','C>G', 'C>T'],index=[item[0:item.index('_SNV')] for item in filelist])
    num_list = pd.DataFrame(num_list, columns=['A>C', 'A>G', 'A>T', 'C>A', 'C>G', 'C>T'], index=[item[0:item.index('_SNV')] for item in filelist])
    pro_list.to_csv('../'+name+'_ExonicFunc.refGene_stas_pro.csv')
    num_list.to_csv('../'+name+'_ExonicFunc.refGene_stas_num.csv')



if __name__=="__main__":
    fun2("D:/mo/10.17/LXF_WES")