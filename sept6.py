#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/6 22:23
# @Author  : liulijun
# @Site    : 
# @File    : sept6.py
# @Software: PyCharm

import pandas as pd
import numpy as np
from scipy import stats
from openpyxl.workbook import Workbook

def main():

    conv_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-南京.xlsx", sheetname="常规")
    CAG_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-南京.xlsx", sheetname="CAG")
    DCAG_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-南京.xlsx", sheetname="DCAG")

    # male and female
    sex=[ [0 for i in range(4)] for i in range(3)]
    sex = pd.DataFrame(sex, columns=['男','女','男（比例）','女（比例）'], index=['常规','CAG','DCAG'])
    sex['type'] = ['常规', 'CAG', 'DCAG']

    sex['男'].loc['常规']=len(conv_patient_info[conv_patient_info['性别（男=1，女=2）']  ==1.0])
    sex['女'].loc['常规']= len(conv_patient_info[conv_patient_info['性别（男=1，女=2）'] == 2.0])
    sex['男（比例）'].loc['常规'] =sex['男'].loc['常规']/(sex['男'].loc['常规']+sex['女'].loc['常规'])
    sex['女（比例）'].loc['常规'] = sex['女'].loc['常规']/(sex['男'].loc['常规']+sex['女'].loc['常规'])

    sex['男'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['性别'] == 1.0])
    sex['女'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['性别'] == 2.0])
    sex['男（比例）'].loc['CAG'] = sex['男'].loc['CAG'] / (sex['男'].loc['CAG'] + sex['女'].loc['CAG'])
    sex['女（比例）'].loc['CAG'] = sex['女'].loc['CAG'] / (sex['男'].loc['CAG'] + sex['女'].loc['CAG'])

    sex['男'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['性别'] == 1.0])
    sex['女'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['性别'] == 2.0])
    sex['男（比例）'].loc['DCAG'] = sex['男'].loc['DCAG'] / (sex['男'].loc['DCAG'] + sex['女'].loc['DCAG'])
    sex['女（比例）'].loc['DCAG'] = sex['女'].loc['DCAG'] / (sex['男'].loc['DCAG'] + sex['女'].loc['DCAG'])

    # age
    age = [[0 for i in range(3)] for i in range(3)]
    age = pd.DataFrame(age, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    age['type'] = ['常规', 'CAG', 'DCAG']

    age['max'].loc['常规']= np.max(conv_patient_info['年龄'].tolist())
    age['min'].loc['常规']= np.min(conv_patient_info['年龄'].tolist())
    age['median'].loc['常规'] = np.median(conv_patient_info['年龄'].tolist())

    age['max'].loc['CAG'] = np.max(CAG_patient_info['年龄'].tolist())
    age['min'].loc['CAG'] = np.min(CAG_patient_info['年龄'].tolist())
    age['median'].loc['CAG'] = np.median(CAG_patient_info['年龄'].tolist())

    age['max'].loc['DCAG'] = np.max(DCAG_patient_info['年龄'].tolist())
    age['min'].loc['DCAG'] = np.min(DCAG_patient_info['年龄'].tolist())
    age['median'].loc['DCAG'] = np.median(DCAG_patient_info['年龄'].tolist())

    # disease type

    idisease_type = set(conv_patient_info['诊断'].tolist()+CAG_patient_info['诊断'].tolist()+DCAG_patient_info['诊断'].tolist())
    idisease_type.remove('-')
    disease_type = [[0 for i in range(len(idisease_type))] for i in range(3)]
    disease_type = pd.DataFrame(disease_type, columns=idisease_type, index=['常规', 'CAG', 'DCAG'])
    disease_type['type'] = ['常规', 'CAG', 'DCAG']
    for item in idisease_type:
        disease_type[item].loc['常规'] = len(conv_patient_info[conv_patient_info['诊断'] == str(item)])
    for item in idisease_type:
        disease_type[item].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['诊断'] == str(item)])
    for item in idisease_type:
        disease_type[item].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['诊断'] == str(item)])

    # WBC

    WBC = [[0 for i in range(3)] for i in range(3)]
    WBC = pd.DataFrame(WBC, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    WBC['type'] = ['常规', 'CAG', 'DCAG']

    datalist = conv_patient_info[conv_patient_info['WBC']!='-']
    datalist=datalist[datalist['WBC']!=float('nan')]['WBC'].tolist()
    for item in datalist:
        if not item>0:
            datalist.remove(item)
    WBC['max'].loc['常规'] = np.max(datalist)
    WBC['min'].loc['常规'] = np.min(datalist)
    WBC['median'].loc['常规'] = np.median(datalist)

    datalist = CAG_patient_info[CAG_patient_info['WBC'] != '-']
    datalist = datalist[datalist['WBC'] != float('NaN')]['WBC'].tolist()
    WBC['max'].loc['CAG'] = np.max(datalist)
    WBC['min'].loc['CAG'] = np.min(datalist)
    WBC['median'].loc['CAG'] = np.median(datalist)

    datalist = DCAG_patient_info['WBC'].tolist()
    WBC['max'].loc['DCAG'] = np.max(datalist)
    WBC['min'].loc['DCAG'] = np.min(datalist)
    WBC['median'].loc['DCAG'] = np.median(datalist)

    # Hb
    Hb = [[0 for i in range(3)] for i in range(3)]
    Hb = pd.DataFrame(Hb, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    Hb['type'] = ['常规', 'CAG', 'DCAG']

    datalist = conv_patient_info[conv_patient_info['Hb'] != '-']
    datalist = datalist[datalist['Hb'] != float('nan')]['Hb'].tolist()
    for item in datalist:
        if not item > 0:
            datalist.remove(item)
    Hb['max'].loc['常规'] = np.max(datalist)
    Hb['min'].loc['常规'] = np.min(datalist)
    Hb['median'].loc['常规'] = np.median(datalist)

    datalist = CAG_patient_info[CAG_patient_info['Hb'] != '-']
    datalist = datalist[datalist['Hb'] != float('NaN')]['Hb'].tolist()
    Hb['max'].loc['CAG'] = np.max(datalist)
    Hb['min'].loc['CAG'] = np.min(datalist)
    Hb['median'].loc['CAG'] = np.median(datalist)

    datalist = DCAG_patient_info['Hb'].tolist()
    Hb['max'].loc['DCAG'] = np.max(datalist)
    Hb['min'].loc['DCAG'] = np.min(datalist)
    Hb['median'].loc['DCAG'] = np.median(datalist)

    # PLT
    PLT = [[0 for i in range(3)] for i in range(3)]
    PLT = pd.DataFrame(PLT, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    PLT['type'] = ['常规', 'CAG', 'DCAG']

    datalist = conv_patient_info[conv_patient_info['PLT'] != '-']
    datalist = datalist[datalist['PLT'] != float('nan')]['PLT'].tolist()
    for item in datalist:
        if not item > 0:
            datalist.remove(item)
    PLT['max'].loc['常规'] = np.max(datalist)
    PLT['min'].loc['常规'] = np.min(datalist)
    PLT['median'].loc['常规'] = np.median(datalist)

    datalist = CAG_patient_info[CAG_patient_info['PLT'] != '-']
    datalist = datalist[datalist['PLT'] != float('NaN')]['PLT'].tolist()
    PLT['max'].loc['CAG'] = np.max(datalist)
    PLT['min'].loc['CAG'] = np.min(datalist)
    PLT['median'].loc['CAG'] = np.median(datalist)

    datalist = DCAG_patient_info['PLT'].tolist()
    PLT['max'].loc['DCAG'] = np.max(datalist)
    PLT['min'].loc['DCAG'] = np.min(datalist)
    PLT['median'].loc['DCAG'] = np.median(datalist)

    # NE
    NE = [[0 for i in range(3)] for i in range(3)]
    NE = pd.DataFrame(NE, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    NE['type'] = ['常规', 'CAG', 'DCAG']

    datalist = conv_patient_info[conv_patient_info['NE'] != '-']
    adatalist = datalist[datalist['NE'] != float('nan')]['NE'].tolist()
    datalist=[]
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    NE['max'].loc['常规'] = np.max(datalist)
    NE['min'].loc['常规'] = np.min(datalist)
    NE['median'].loc['常规'] = np.median(datalist)

    if '-' in CAG_patient_info['NE'].tolist():
        datalist = CAG_patient_info[CAG_patient_info['NE'] != '-']
    adatalist = datalist['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    NE['max'].loc['CAG'] = np.max(datalist)
    NE['min'].loc['CAG'] = np.min(datalist)
    NE['median'].loc['CAG'] = np.median(datalist)

    adatalist = DCAG_patient_info['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    NE['max'].loc['DCAG'] = np.max(datalist)
    NE['min'].loc['DCAG'] = np.min(datalist)
    NE['median'].loc['DCAG'] = np.median(datalist)

    # 初诊BM
    PRI_BM = [[0 for i in range(3)] for i in range(3)]
    PRI_BM = pd.DataFrame(PRI_BM, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    PRI_BM['type'] = ['常规', 'CAG', 'DCAG']

    if '-' in conv_patient_info['初诊BM(%)'].tolist():
        datalist = conv_patient_info[conv_patient_info['初诊BM(%)'] != '-']
    adatalist = datalist[datalist['初诊BM(%)'] != float('nan')]['初诊BM(%)'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    PRI_BM['max'].loc['常规'] = np.max(datalist)
    PRI_BM['min'].loc['常规'] = np.min(datalist)
    PRI_BM['median'].loc['常规'] = np.median(datalist)

    if '-' in CAG_patient_info['初诊BM(%)'].tolist():
        datalist = CAG_patient_info[CAG_patient_info['初诊BM(%)'] != '-']
    adatalist = datalist['初诊BM(%)'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    PRI_BM['max'].loc['CAG'] = np.max(datalist)
    PRI_BM['min'].loc['CAG'] = np.min(datalist)
    PRI_BM['median'].loc['CAG'] = np.median(datalist)

    if '-' in DCAG_patient_info['初诊BM(%)'].tolist():
        datalist = DCAG_patient_info[DCAG_patient_info['初诊BM(%)'] != '-']
    adatalist = datalist['初诊BM(%)'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    PRI_BM['max'].loc['DCAG'] = np.max(datalist)
    PRI_BM['min'].loc['DCAG'] = np.min(datalist)
    PRI_BM['median'].loc['DCAG'] = np.median(datalist)

    # 评价1疗效
    eva1_effect = [[0 for i in range(3)] for i in range(3)]
    eva1_effect = pd.DataFrame(eva1_effect, columns=['NR', 'CR', 'PR'], index=['常规', 'CAG', 'DCAG'])
    eva1_effect['type']=['常规', 'CAG', 'DCAG']

    eva1_effect['NR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='NR'])
    eva1_effect['CR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='CR'])
    eva1_effect['PR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='PR'])

    eva1_effect['NR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效'] == 'NR'])
    eva1_effect['CR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效'] == 'CR'])
    eva1_effect['PR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效'] == 'PR'])

    eva1_effect['NR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效'] == 'NR'])
    eva1_effect['CR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效'] == 'CR'])
    eva1_effect['PR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效'] == 'PR'])

    # 老年病人年龄分布
    dist_eldly=[[0 for i in range(3)] for i in range(3)]
    dist_eldly = pd.DataFrame(dist_eldly, columns=['<50', '50-59', '>=60'], index=['常规', 'CAG', 'DCAG'])
    dist_eldly['<50'].loc['常规']=len(conv_patient_info[conv_patient_info['年龄']<50])
    newconv_patient_info=conv_patient_info[conv_patient_info['年龄'] <= 59]
    dist_eldly['50-59'].loc['常规'] = len(newconv_patient_info[newconv_patient_info['年龄'] >= 50])
    dist_eldly['>=60'].loc['常规'] = len(conv_patient_info[conv_patient_info['年龄'] >= 60])

    dist_eldly['<50'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['年龄'] < 50])
    newconv_patient_info = CAG_patient_info[CAG_patient_info['年龄'] <= 59]
    dist_eldly['50-59'].loc['CAG'] = len(newconv_patient_info[newconv_patient_info['年龄'] >= 50])
    dist_eldly['>=60'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['年龄'] >= 60])

    dist_eldly['<50'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['年龄'] < 50])
    newconv_patient_info = DCAG_patient_info[DCAG_patient_info['年龄'] <= 59]
    dist_eldly['50-59'].loc['DCAG'] = len(newconv_patient_info[newconv_patient_info['年龄'] >= 50])
    dist_eldly['>=60'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['年龄'] >= 60])

    # 'NR', 'CR', 'PR'分布
    dist_eldly_NR = [[0 for i in range(3)] for i in range(3)]
    dist_eldly_NR = pd.DataFrame(dist_eldly_NR, columns=['<50', '50-59', '>=60'], index=['常规', 'CAG', 'DCAG'])
    dist_eldly_CR = [[0 for i in range(3)] for i in range(3)]
    dist_eldly_CR = pd.DataFrame(dist_eldly_CR, columns=['<50', '50-59', '>=60'], index=['常规', 'CAG', 'DCAG'])
    dist_eldly_PR = [[0 for i in range(3)] for i in range(3)]
    dist_eldly_PR = pd.DataFrame(dist_eldly_PR, columns=['<50', '50-59', '>=60'], index=['常规', 'CAG', 'DCAG'])

    selected_patient=conv_patient_info[conv_patient_info['年龄'] < 50]
    dist_eldly_NR['<50'].loc['常规']=len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['<50'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['<50'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = conv_patient_info[conv_patient_info['年龄'] >= 50]
    selected_patient = selected_patient[selected_patient['年龄'] <= 59]
    dist_eldly_NR['50-59'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['50-59'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['50-59'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = conv_patient_info[conv_patient_info['年龄'] >= 60]
    dist_eldly_NR['>=60'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['>=60'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['>=60'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = CAG_patient_info[CAG_patient_info['年龄'] < 50]
    dist_eldly_NR['<50'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['<50'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['<50'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = CAG_patient_info[CAG_patient_info['年龄'] >= 50]
    selected_patient = selected_patient[selected_patient['年龄'] <= 59]
    dist_eldly_NR['50-59'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['50-59'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['50-59'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = CAG_patient_info[CAG_patient_info['年龄'] >= 60]
    dist_eldly_NR['>=60'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['>=60'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['>=60'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = DCAG_patient_info[DCAG_patient_info['年龄'] < 50]
    dist_eldly_NR['<50'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['<50'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['<50'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = DCAG_patient_info[DCAG_patient_info['年龄'] >= 50]
    selected_patient = selected_patient[selected_patient['年龄'] <= 59]
    dist_eldly_NR['50-59'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['50-59'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['50-59'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = DCAG_patient_info[DCAG_patient_info['年龄'] >= 60]
    dist_eldly_NR['>=60'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['>=60'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['>=60'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    writer = pd.ExcelWriter('D:/mo/9.10/base_info_nanjing.xlsx')
    sex.to_excel(writer, '性别', index=False)
    age.to_excel(writer, '年龄', index=False)
    dist_eldly.to_excel(writer, '年龄分布', index=False)
    disease_type.to_excel(writer, '诊断', index=False)
    WBC.to_excel(writer, 'WBC', index=False)
    Hb.to_excel(writer, 'Hb', index=False)
    PLT.to_excel(writer, 'PLT', index=False)
    NE.to_excel(writer, 'NE', index=False)
    PRI_BM.to_excel(writer, '初诊BM(%)', index=False)
    eva1_effect.to_excel(writer, '评价1 疗效', index=False)
    dist_eldly_NR.to_excel(writer, 'NR', index=False)
    dist_eldly_CR.to_excel(writer, 'CR', index=False)
    dist_eldly_PR.to_excel(writer, 'PR', index=False)

def p_value():

    conv_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-合并.xlsx", sheetname="常规")
    CAG_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-合并.xlsx", sheetname="CAG")
    DCAG_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-合并.xlsx", sheetname="DCAG")

    # AGE
    age = [[0 for i in range(3)] for i in range(3)]
    age = pd.DataFrame(age, columns=['常规', 'CAG', 'DCAG'], index=['常规', 'CAG', 'DCAG'])
    agedata={}
    agedata['常规']=conv_patient_info['年龄'].tolist()
    agedata['CAG']=CAG_patient_info['年龄'].tolist()
    agedata['DCAG']=DCAG_patient_info['年龄'].tolist()

    # wilcox秩序和检验
    (s,p)=stats.ranksums(agedata['常规'], agedata['CAG'])
    age['常规'].loc['CAG']=p
    age['CAG'].loc['常规'] = p

    (s,p)=stats.ranksums(agedata['常规'], agedata['DCAG'])
    age['常规'].loc['DCAG']=p
    age['DCAG'].loc['常规'] = p

    # 诊断
    dignose = [[0 for i in range(3)] for i in range(3)]
    dignose = pd.DataFrame(dignose, columns=['常规', 'CAG', 'DCAG'], index=['常规', 'CAG', 'DCAG'])
    dignosedata = {}
    dignosedata['常规'] = conv_patient_info['诊断'].tolist()
    dignosedata['CAG'] = CAG_patient_info['诊断'].tolist()
    dignosedata['DCAG'] = DCAG_patient_info['诊断'].tolist()

    # wilcox秩序和检验
    (s, p) = stats.ranksums(dignosedata['常规'], dignosedata['CAG'])
    dignose['常规'].loc['CAG'] = p
    dignose['CAG'].loc['常规'] = p

    (s, p) = stats.ranksums(dignosedata['常规'], dignosedata['DCAG'])
    dignose['常规'].loc['DCAG'] = p
    dignose['DCAG'].loc['常规'] = p

    # WBC
    WBC = [[0 for i in range(3)] for i in range(3)]
    WBC = pd.DataFrame(WBC, columns=['常规', 'CAG', 'DCAG'], index=['常规', 'CAG', 'DCAG'])
    WBCdata = {}

    datalist = conv_patient_info[conv_patient_info['WBC'] != '-']
    datalist = datalist[datalist['WBC'] != float('nan')]['WBC'].tolist()
    for item in datalist:
        if not item > 0:
            datalist.remove(item)
    WBCdata['常规'] = datalist

    datalist = CAG_patient_info[CAG_patient_info['WBC'] != '-']
    datalist = datalist[datalist['WBC'] != float('NaN')]['WBC'].tolist()
    WBCdata['CAG'] = datalist

    WBCdata['DCAG'] = DCAG_patient_info['WBC'].tolist()

    # wilcox秩序和检验
    (s, p) = stats.ranksums(WBCdata['常规'], WBCdata['CAG'])
    WBC['常规'].loc['CAG'] = p
    WBC['CAG'].loc['常规'] = p

    (s, p) = stats.ranksums(WBCdata['常规'], WBCdata['DCAG'])
    WBC['常规'].loc['DCAG'] = p
    WBC['DCAG'].loc['常规'] = p

    # Hb
    Hb = [[0 for i in range(3)] for i in range(3)]
    Hb = pd.DataFrame(Hb, columns=['常规', 'CAG', 'DCAG'], index=['常规', 'CAG', 'DCAG'])
    Hbdata = {}

    datalist = conv_patient_info[conv_patient_info['Hb'] != '-']
    datalist = datalist[datalist['Hb'] != float('nan')]['Hb'].tolist()
    for item in datalist:
        if not item > 0:
            datalist.remove(item)
    Hbdata['常规'] = datalist

    datalist = CAG_patient_info[CAG_patient_info['Hb'] != '-']
    datalist = datalist[datalist['Hb'] != float('NaN')]['Hb'].tolist()
    Hbdata['CAG'] = datalist

    Hbdata['DCAG'] = DCAG_patient_info['Hb'].tolist()

    # wilcox秩序和检验
    (s, p) = stats.ranksums(Hbdata['常规'], Hbdata['CAG'])
    Hb['常规'].loc['CAG'] = p
    Hb['CAG'].loc['常规'] = p

    (s, p) = stats.ranksums(Hbdata['常规'], Hbdata['DCAG'])
    Hb['常规'].loc['DCAG'] = p
    Hb['DCAG'].loc['常规'] = p

    # PLT
    PLT = [[0 for i in range(3)] for i in range(3)]
    PLT = pd.DataFrame(PLT, columns=['常规', 'CAG', 'DCAG'], index=['常规', 'CAG', 'DCAG'])
    PLTdata = {}

    datalist = conv_patient_info[conv_patient_info['PLT'] != '-']
    datalist = datalist[datalist['PLT'] != float('nan')]['PLT'].tolist()
    for item in datalist:
        if not item > 0:
            datalist.remove(item)
    PLTdata['常规'] = datalist

    datalist = CAG_patient_info[CAG_patient_info['PLT'] != '-']
    datalist = datalist[datalist['PLT'] != float('NaN')]['PLT'].tolist()
    PLTdata['CAG'] = datalist

    PLTdata['DCAG'] = DCAG_patient_info['PLT'].tolist()

    # wilcox秩序和检验
    (s, p) = stats.ranksums(PLTdata['常规'], PLTdata['CAG'])
    PLT['常规'].loc['CAG'] = p
    PLT['CAG'].loc['常规'] = p

    (s, p) = stats.ranksums(PLTdata['常规'], PLTdata['DCAG'])
    PLT['常规'].loc['DCAG'] = p
    PLT['DCAG'].loc['常规'] = p

    # NE
    NE = [[0 for i in range(3)] for i in range(3)]
    NE = pd.DataFrame(NE, columns=['常规', 'CAG', 'DCAG'], index=['常规', 'CAG', 'DCAG'])
    NEdata = {}

    datalist = conv_patient_info[conv_patient_info['NE'] != '-']
    adatalist = datalist[datalist['NE'] != float('nan')]['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    NEdata['常规'] = datalist

    if '-' in CAG_patient_info['NE'].tolist():
        datalist = CAG_patient_info[CAG_patient_info['NE'] != '-']
    adatalist = datalist['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    NEdata['CAG'] = datalist

    adatalist = DCAG_patient_info['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    NEdata['DCAG'] = datalist

    # wilcox秩序和检验
    (s, p) = stats.ranksums(NEdata['常规'], NEdata['CAG'])
    NE['常规'].loc['CAG'] = p
    NE['CAG'].loc['常规'] = p

    (s, p) = stats.ranksums(NEdata['常规'], NEdata['DCAG'])
    NE['常规'].loc['DCAG'] = p
    NE['DCAG'].loc['常规'] = p

    # 初诊BM
    PRI_BM = [[0 for i in range(3)] for i in range(3)]
    PRI_BM = pd.DataFrame(PRI_BM, columns=['常规', 'CAG', 'DCAG'], index=['常规', 'CAG', 'DCAG'])
    PRI_BMdata = {}

    datalist = conv_patient_info[conv_patient_info['NE'] != '-']
    adatalist = datalist[datalist['NE'] != float('nan')]['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    PRI_BMdata['常规'] = datalist

    if '-' in CAG_patient_info['NE'].tolist():
        datalist = CAG_patient_info[CAG_patient_info['NE'] != '-']
    adatalist = datalist['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    PRI_BMdata['CAG'] = datalist

    adatalist = DCAG_patient_info['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    PRI_BMdata['DCAG'] = datalist

    # wilcox秩序和检验
    (s, p) = stats.ranksums(PRI_BMdata['常规'], PRI_BMdata['CAG'])
    PRI_BM['常规'].loc['CAG'] = p
    PRI_BM['CAG'].loc['常规'] = p

    (s, p) = stats.ranksums(PRI_BMdata['常规'], PRI_BMdata['DCAG'])
    PRI_BM['常规'].loc['DCAG'] = p
    PRI_BM['DCAG'].loc['常规'] = p

    # 评价1疗效
    eva1_effectall = [[0 for i in range(3)] for i in range(3)]
    eva1_effectall = pd.DataFrame(eva1_effectall, columns=['常规', 'CAG', 'DCAG'], index=['常规', 'CAG', 'DCAG'])

    eva1_effect = [[0 for i in range(3)] for i in range(3)]
    eva1_effect = pd.DataFrame(eva1_effect, columns=['NR', 'CR', 'PR'], index=['常规', 'CAG', 'DCAG'])

    eva1_effect['NR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='NR'])
    eva1_effect['CR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='CR'])
    eva1_effect['PR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='PR'])

    eva1_effect['NR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效']=='NR'])
    eva1_effect['CR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效']=='CR'])
    eva1_effect['PR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效']=='PR'])

    eva1_effect['NR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效']=='NR'])
    eva1_effect['CR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效']=='CR'])
    eva1_effect['PR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效']=='PR'])

    # 卡方检验
    print('chisquare',eva1_effect.loc['常规'].tolist(), eva1_effect.loc['CAG'].tolist())
    (s, p)=stats.chisquare(eva1_effect.loc['常规'].tolist(), eva1_effect.loc['CAG'].tolist())
    eva1_effectall['常规'].loc['CAG'] = p
    eva1_effectall['CAG'].loc['常规'] = p
    print('chisquare',eva1_effect.loc['常规'].tolist(), eva1_effect.loc['DCAG'].tolist())
    (s, p) = stats.chisquare(eva1_effect.loc['常规'].tolist(), eva1_effect.loc['DCAG'].tolist())
    eva1_effectall['常规'].loc['CAG'] = p
    eva1_effectall['CAG'].loc['常规'] = p


    writer = pd.ExcelWriter('D:/mo/9.10/relation.xlsx')
    age.to_excel(writer, '年龄', index=False)
    dignose.to_excel(writer, '诊断', index=False)
    WBC.to_excel(writer, 'WBC', index=False)
    Hb.to_excel(writer, 'Hb', index=False)
    PLT.to_excel(writer, 'PLT', index=False)
    NE.to_excel(writer, 'NE', index=False)
    PRI_BM.to_excel(writer, '初诊BM(%)', index=False)
    eva1_effectall.to_excel(writer, '评价1 疗效', index=False)


def main2():

    conv_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-南京.xlsx", sheetname="常规")
    # CAG_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-南京.xlsx", sheetname="CAG")
    DCAG_patient_info = pd.read_excel("D:/mo/9.10/老年AML临床资料 - 病例-南京.xlsx", sheetname="DCAG")

    # male and female
    sex=[ [0 for i in range(4)] for i in range(3)]
    sex = pd.DataFrame(sex, columns=['男','女','男（比例）','女（比例）'], index=['常规','CAG','DCAG'])
    sex['type'] = ['常规', 'CAG', 'DCAG']

    sex['男'].loc['常规']=len(conv_patient_info[conv_patient_info['性别（男=1，女=2）']  ==1.0])
    sex['女'].loc['常规']= len(conv_patient_info[conv_patient_info['性别（男=1，女=2）'] == 2.0])
    sex['男（比例）'].loc['常规'] =sex['男'].loc['常规']/(sex['男'].loc['常规']+sex['女'].loc['常规'])
    sex['女（比例）'].loc['常规'] = sex['女'].loc['常规']/(sex['男'].loc['常规']+sex['女'].loc['常规'])

    # sex['男'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['性别'] == 1.0])
    # sex['女'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['性别'] == 2.0])
    # sex['男（比例）'].loc['CAG'] = sex['男'].loc['CAG'] / (sex['男'].loc['CAG'] + sex['女'].loc['CAG'])
    # sex['女（比例）'].loc['CAG'] = sex['女'].loc['CAG'] / (sex['男'].loc['CAG'] + sex['女'].loc['CAG'])

    sex['男'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['性别（男=1，女=2）'] == 1.0])
    sex['女'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['性别（男=1，女=2）'] == 2.0])
    sex['男（比例）'].loc['DCAG'] = sex['男'].loc['DCAG'] / (sex['男'].loc['DCAG'] + sex['女'].loc['DCAG'])
    sex['女（比例）'].loc['DCAG'] = sex['女'].loc['DCAG'] / (sex['男'].loc['DCAG'] + sex['女'].loc['DCAG'])

    # age
    age = [[0 for i in range(3)] for i in range(3)]
    age = pd.DataFrame(age, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    age['type'] = ['常规', 'CAG', 'DCAG']

    age['max'].loc['常规']= np.max(conv_patient_info['年龄'].tolist())
    age['min'].loc['常规']= np.min(conv_patient_info['年龄'].tolist())
    age['median'].loc['常规'] = np.median(conv_patient_info['年龄'].tolist())

    # age['max'].loc['CAG'] = np.max(CAG_patient_info['年龄'].tolist())
    # age['min'].loc['CAG'] = np.min(CAG_patient_info['年龄'].tolist())
    # age['median'].loc['CAG'] = np.median(CAG_patient_info['年龄'].tolist())

    age['max'].loc['DCAG'] = np.max(DCAG_patient_info['年龄'].tolist())
    age['min'].loc['DCAG'] = np.min(DCAG_patient_info['年龄'].tolist())
    age['median'].loc['DCAG'] = np.median(DCAG_patient_info['年龄'].tolist())

    # disease type

    idisease_type = set(conv_patient_info['诊断'].tolist()+DCAG_patient_info['诊断'].tolist())
    disease_type = [[0 for i in range(len(idisease_type))] for i in range(3)]
    disease_type = pd.DataFrame(disease_type, columns=idisease_type, index=['常规', 'CAG', 'DCAG'])
    disease_type['type'] = ['常规', 'CAG', 'DCAG']
    for item in idisease_type:
        disease_type[item].loc['常规'] = len(conv_patient_info[conv_patient_info['诊断'] == str(item)])
    # for item in idisease_type:
    #     disease_type[item].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['诊断'] == str(item)])
    for item in idisease_type:
        disease_type[item].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['诊断'] == str(item)])

    # WBC

    WBC = [[0 for i in range(3)] for i in range(3)]
    WBC = pd.DataFrame(WBC, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    WBC['type'] = ['常规', 'CAG', 'DCAG']

    datalist = conv_patient_info[conv_patient_info['WBC']!='-']
    datalist=datalist[datalist['WBC']!=float('nan')]['WBC'].tolist()
    for item in datalist:
        if not item>0:
            datalist.remove(item)
    WBC['max'].loc['常规'] = np.max(datalist)
    WBC['min'].loc['常规'] = np.min(datalist)
    WBC['median'].loc['常规'] = np.median(datalist)

    # datalist = CAG_patient_info[CAG_patient_info['WBC'] != '-']
    # datalist = datalist[datalist['WBC'] != float('NaN')]['WBC'].tolist()
    # WBC['max'].loc['CAG'] = np.max(datalist)
    # WBC['min'].loc['CAG'] = np.min(datalist)
    # WBC['median'].loc['CAG'] = np.median(datalist)

    datalist = DCAG_patient_info['WBC'].tolist()
    WBC['max'].loc['DCAG'] = np.max(datalist)
    WBC['min'].loc['DCAG'] = np.min(datalist)
    WBC['median'].loc['DCAG'] = np.median(datalist)

    # Hb
    Hb = [[0 for i in range(3)] for i in range(3)]
    Hb = pd.DataFrame(Hb, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    Hb['type'] = ['常规', 'CAG', 'DCAG']

    datalist = conv_patient_info[conv_patient_info['Hb'] != '-']
    datalist = datalist[datalist['Hb'] != float('nan')]['Hb'].tolist()
    for item in datalist:
        if not item > 0:
            datalist.remove(item)
    Hb['max'].loc['常规'] = np.max(datalist)
    Hb['min'].loc['常规'] = np.min(datalist)
    Hb['median'].loc['常规'] = np.median(datalist)

    # datalist = CAG_patient_info[CAG_patient_info['Hb'] != '-']
    # datalist = datalist[datalist['Hb'] != float('NaN')]['Hb'].tolist()
    # Hb['max'].loc['CAG'] = np.max(datalist)
    # Hb['min'].loc['CAG'] = np.min(datalist)
    # Hb['median'].loc['CAG'] = np.median(datalist)

    datalist = DCAG_patient_info['Hb'].tolist()
    Hb['max'].loc['DCAG'] = np.max(datalist)
    Hb['min'].loc['DCAG'] = np.min(datalist)
    Hb['median'].loc['DCAG'] = np.median(datalist)

    # PLT
    PLT = [[0 for i in range(3)] for i in range(3)]
    PLT = pd.DataFrame(PLT, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    PLT['type'] = ['常规', 'CAG', 'DCAG']

    # A=conv_patient_info['PLT'].tolist()
    # for item in A:
    #     print(type(item),item)
    # datalist = conv_patient_info[conv_patient_info['PLT'] != '-']
    datalist = conv_patient_info['PLT'].tolist()
    for item in datalist:
        if not item > 0 and item!=float('nan'):
            datalist.remove(item)
    PLT['max'].loc['常规'] = np.max(datalist)
    PLT['min'].loc['常规'] = np.min(datalist)
    PLT['median'].loc['常规'] = np.median(datalist)

    # datalist = CAG_patient_info[CAG_patient_info['PLT'] != '-']
    # datalist = datalist[datalist['PLT'] != float('NaN')]['PLT'].tolist()
    # PLT['max'].loc['CAG'] = np.max(datalist)
    # PLT['min'].loc['CAG'] = np.min(datalist)
    # PLT['median'].loc['CAG'] = np.median(datalist)

    datalist = DCAG_patient_info['PLT'].tolist()
    PLT['max'].loc['DCAG'] = np.max(datalist)
    PLT['min'].loc['DCAG'] = np.min(datalist)
    PLT['median'].loc['DCAG'] = np.median(datalist)

    # NE
    NE = [[0 for i in range(3)] for i in range(3)]
    NE = pd.DataFrame(NE, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    NE['type'] = ['常规', 'CAG', 'DCAG']

    # datalist = conv_patient_info[conv_patient_info['NE'] != '-']
    # adatalist = datalist[datalist['NE'] != float('nan')]['NE'].tolist()
    # datalist=[]
    # for item in adatalist:
    #     if item > 0:
    #         datalist.append(item)
    # NE['max'].loc['常规'] = np.max(datalist)
    # NE['min'].loc['常规'] = np.min(datalist)
    # NE['median'].loc['常规'] = np.median(datalist)

    # if '-' in CAG_patient_info['NE'].tolist():
    #     datalist = CAG_patient_info[CAG_patient_info['NE'] != '-']
    # adatalist = datalist['NE'].tolist()
    # datalist = []
    # for item in adatalist:
    #     if item > 0:
    #         datalist.append(item)
    # NE['max'].loc['CAG'] = np.max(datalist)
    # NE['min'].loc['CAG'] = np.min(datalist)
    # NE['median'].loc['CAG'] = np.median(datalist)

    adatalist = DCAG_patient_info['NE'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    NE['max'].loc['DCAG'] = np.max(datalist)
    NE['min'].loc['DCAG'] = np.min(datalist)
    NE['median'].loc['DCAG'] = np.median(datalist)

    # 初诊BM
    PRI_BM = [[0 for i in range(3)] for i in range(3)]
    PRI_BM = pd.DataFrame(PRI_BM, columns=['max', 'min', 'median'], index=['常规', 'CAG', 'DCAG'])
    PRI_BM['type'] = ['常规', 'CAG', 'DCAG']

    if '-' in conv_patient_info['初诊BM(%)'].tolist():
        datalist = conv_patient_info[conv_patient_info['初诊BM(%)'] != '-']
    adatalist = datalist[datalist['初诊BM(%)'] != float('nan')]['初诊BM(%)'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    PRI_BM['max'].loc['常规'] = np.max(datalist)
    PRI_BM['min'].loc['常规'] = np.min(datalist)
    PRI_BM['median'].loc['常规'] = np.median(datalist)

    # if '-' in CAG_patient_info['初诊BM(%)'].tolist():
    #     datalist = CAG_patient_info[CAG_patient_info['初诊BM(%)'] != '-']
    # adatalist = datalist['初诊BM(%)'].tolist()
    # datalist = []
    # for item in adatalist:
    #     if item > 0:
    #         datalist.append(item)
    # PRI_BM['max'].loc['CAG'] = np.max(datalist)
    # PRI_BM['min'].loc['CAG'] = np.min(datalist)
    # PRI_BM['median'].loc['CAG'] = np.median(datalist)

    if '-' in DCAG_patient_info['初诊BM(%)'].tolist():
        datalist = DCAG_patient_info[DCAG_patient_info['初诊BM(%)'] != '-']
    else:
        datalist = DCAG_patient_info
    adatalist = datalist['初诊BM(%)'].tolist()
    datalist = []
    for item in adatalist:
        if item > 0:
            datalist.append(item)
    PRI_BM['max'].loc['DCAG'] = np.max(datalist)
    PRI_BM['min'].loc['DCAG'] = np.min(datalist)
    PRI_BM['median'].loc['DCAG'] = np.median(datalist)

    # 评价1疗效
    eva1_effect = [[0 for i in range(3)] for i in range(3)]
    eva1_effect = pd.DataFrame(eva1_effect, columns=['NR', 'CR', 'PR'], index=['常规', 'CAG', 'DCAG'])
    eva1_effect['type']=['常规', 'CAG', 'DCAG']

    eva1_effect['NR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='NR'])
    eva1_effect['CR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='CR'])
    eva1_effect['PR'].loc['常规'] = len(conv_patient_info[conv_patient_info['评价1 疗效']=='PR'])

    # eva1_effect['NR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效'] == 'NR'])
    # eva1_effect['CR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效'] == 'CR'])
    # eva1_effect['PR'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['评价1 疗效'] == 'PR'])

    eva1_effect['NR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效'] == 'NR'])
    eva1_effect['CR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效'] == 'CR'])
    eva1_effect['PR'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['评价1 疗效'] == 'PR'])

    # 老年病人年龄分布
    dist_eldly=[[0 for i in range(3)] for i in range(3)]
    dist_eldly = pd.DataFrame(dist_eldly, columns=['<50', '50-59', '>=60'], index=['常规', 'CAG', 'DCAG'])
    dist_eldly['<50'].loc['常规']=len(conv_patient_info[conv_patient_info['年龄']<50])
    newconv_patient_info=conv_patient_info[conv_patient_info['年龄'] <= 59]
    dist_eldly['50-59'].loc['常规'] = len(newconv_patient_info[newconv_patient_info['年龄'] >= 50])
    dist_eldly['>=60'].loc['常规'] = len(conv_patient_info[conv_patient_info['年龄'] >= 60])

    # dist_eldly['<50'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['年龄'] < 50])
    # newconv_patient_info = CAG_patient_info[CAG_patient_info['年龄'] <= 59]
    # dist_eldly['50-59'].loc['CAG'] = len(newconv_patient_info[newconv_patient_info['年龄'] >= 50])
    # dist_eldly['>=60'].loc['CAG'] = len(CAG_patient_info[CAG_patient_info['年龄'] >= 60])

    dist_eldly['<50'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['年龄'] < 50])
    newconv_patient_info = DCAG_patient_info[DCAG_patient_info['年龄'] <= 59]
    dist_eldly['50-59'].loc['DCAG'] = len(newconv_patient_info[newconv_patient_info['年龄'] >= 50])
    dist_eldly['>=60'].loc['DCAG'] = len(DCAG_patient_info[DCAG_patient_info['年龄'] >= 60])

    # 'NR', 'CR', 'PR'分布
    dist_eldly_NR = [[0 for i in range(3)] for i in range(3)]
    dist_eldly_NR = pd.DataFrame(dist_eldly_NR, columns=['<50', '50-59', '>=60'], index=['常规', 'CAG', 'DCAG'])
    dist_eldly_CR = [[0 for i in range(3)] for i in range(3)]
    dist_eldly_CR = pd.DataFrame(dist_eldly_CR, columns=['<50', '50-59', '>=60'], index=['常规', 'CAG', 'DCAG'])
    dist_eldly_PR = [[0 for i in range(3)] for i in range(3)]
    dist_eldly_PR = pd.DataFrame(dist_eldly_PR, columns=['<50', '50-59', '>=60'], index=['常规', 'CAG', 'DCAG'])

    selected_patient=conv_patient_info[conv_patient_info['年龄'] < 50]
    dist_eldly_NR['<50'].loc['常规']=len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['<50'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['<50'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = conv_patient_info[conv_patient_info['年龄'] >= 50]
    selected_patient = selected_patient[selected_patient['年龄'] <= 59]
    dist_eldly_NR['50-59'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['50-59'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['50-59'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = conv_patient_info[conv_patient_info['年龄'] >= 60]
    dist_eldly_NR['>=60'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['>=60'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['>=60'].loc['常规'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    # selected_patient = CAG_patient_info[CAG_patient_info['年龄'] < 50]
    # dist_eldly_NR['<50'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    # dist_eldly_CR['<50'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    # dist_eldly_PR['<50'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])
    #
    # selected_patient = CAG_patient_info[CAG_patient_info['年龄'] >= 50]
    # selected_patient = selected_patient[selected_patient['年龄'] <= 59]
    # dist_eldly_NR['50-59'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    # dist_eldly_CR['50-59'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    # dist_eldly_PR['50-59'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])
    #
    # selected_patient = CAG_patient_info[CAG_patient_info['年龄'] >= 60]
    # dist_eldly_NR['>=60'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    # dist_eldly_CR['>=60'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    # dist_eldly_PR['>=60'].loc['CAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = DCAG_patient_info[DCAG_patient_info['年龄'] < 50]
    dist_eldly_NR['<50'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['<50'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['<50'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = DCAG_patient_info[DCAG_patient_info['年龄'] >= 50]
    selected_patient = selected_patient[selected_patient['年龄'] <= 59]
    dist_eldly_NR['50-59'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['50-59'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['50-59'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    selected_patient = DCAG_patient_info[DCAG_patient_info['年龄'] >= 60]
    dist_eldly_NR['>=60'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'NR'])
    dist_eldly_CR['>=60'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'CR'])
    dist_eldly_PR['>=60'].loc['DCAG'] = len(selected_patient[selected_patient['评价1 疗效'] == 'PR'])

    writer = pd.ExcelWriter('D:/mo/9.10/base_info_nanjing.xlsx')
    sex.to_excel(writer, '性别', index=False)
    age.to_excel(writer, '年龄', index=False)
    dist_eldly.to_excel(writer, '年龄分布', index=False)
    disease_type.to_excel(writer, '诊断', index=False)
    WBC.to_excel(writer, 'WBC', index=False)
    Hb.to_excel(writer, 'Hb', index=False)
    PLT.to_excel(writer, 'PLT', index=False)
    NE.to_excel(writer, 'NE', index=False)
    PRI_BM.to_excel(writer, '初诊BM(%)', index=False)
    eva1_effect.to_excel(writer, '评价1 疗效', index=False)
    dist_eldly_NR.to_excel(writer, 'NR', index=False)
    dist_eldly_CR.to_excel(writer, 'CR', index=False)
    dist_eldly_PR.to_excel(writer, 'PR', index=False)


if __name__=="__main__":
    main2()