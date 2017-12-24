#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/11 11:59
# @Author  : liulijun
# @Site    : 
# @File    : Nov11.py
# @Software: PyCharm

import pandas as pd

class main:

    def __init__(self,path):
        self.path=path
        self.raw_data=self.read()
        self.preprocess()
        self.num_of_patients()
        self.num_of_patients_gene()
        self.mutation_age()
        self.RefCHIP21genes()
        self.CHIP_age()
        self.CHIP_age2()
        self.RefCHIPfrel()
        writer = pd.ExcelWriter('D:/mo/11.11/result.xlsx')
        self.patientsinfo.to_excel(writer, '病人-年龄-突变数', index=True)
        self.mutation_matrix.to_excel(writer, '突变数矩阵', index=True)
        self.mutation_distribution.to_excel(writer, '突变数分布', index=True)
        self.summut.to_excel(writer, '突变数总和', index=True)
        self.isCHIP.to_excel(writer, 'isCHIP', index=True)
        self.CHIPfrel.to_excel(writer, 'CHIPfrel', index=True)
        self.CHIPmutationnum.to_excel(writer, '年龄段-CHIP突变数', index=True)
        self.Top5CHIP.to_excel(writer, '年龄段-TOP5CHIP突变数', index=True)
        writer.save


    def preprocess(self):
        data=pd.DataFrame()
        for row in range(len(self.raw_data)):
            if type(self.raw_data['freq'].iloc[row]) == int or type(self.raw_data['freq'].iloc[row]) == float:
                if self.raw_data['freq'].iloc[row] <=40:
                    data=pd.concat([data,self.raw_data[row:row+1]])
        self.raw_data=data
        # self.raw_data.to_excel('D:/mo/11.11/50.xlsx')

    def read(self):
        self.CHIP = pd.read_excel('D:/mo/11.11/RefCHIP21genes.xlsx')
        return pd.read_excel(self.path)

    def num_of_patients(self):
        self.patientsinfo=[]
        self.patientlist=list(set(self.raw_data['姓名'].tolist()))
        for pat in self.patientlist:
            age=self.raw_data[self.raw_data['姓名']==pat]['年龄'].iloc[0]
            mut_num=len(set(self.raw_data[self.raw_data['姓名']==pat]['pro1'].tolist()))
            range=str(age//10*10)+'-'+str(age//10*10+10)
            self.patientsinfo.append([pat,age,range,mut_num])
        self.patientsinfo=pd.DataFrame(self.patientsinfo,columns=['姓名','年龄','年龄段','突变数'])
        # self.patientsinfo.to_excel('D:/mo/11.11/病人-年龄-突变数.xlsx')

    def num_of_patients_gene(self):
        self.genelist = list(set(self.raw_data['基因'].tolist()))
        data = pd.DataFrame(columns=self.genelist+['age'], index=self.patientlist)
        data = data.fillna(0)
        for pat in self.patientlist:
            data['age'].loc[pat] = self.raw_data[self.raw_data['姓名'] == pat]['年龄'].iloc[0]
            for igene in self.genelist:
                chipdata = self.raw_data[(self.raw_data['基因'] == igene) & (self.raw_data['姓名'] == pat)]
                data[igene].loc[pat]=len(set(chipdata['pro1'].tolist()))
        data.loc['col_sum'] = data.apply(lambda x: x.sum())
        self.mutation_matrix=data
        # data.to_excel('D:/mo/11.11/病人-基因-突变数矩阵.xlsx')

    def mutation_age(self):
        rangelist=sorted(self.patientsinfo['年龄段'].tolist())
        data={}
        summut={}
        max=0
        for range in rangelist:
            data[range]=self.patientsinfo[self.patientsinfo['年龄段']==range]['突变数'].tolist()
            summut[range]=sum(self.patientsinfo[self.patientsinfo['年龄段']==range]['突变数'].tolist())
            if len(data[range])>max:
                max=len(data[range])
        for key in data.keys():
            data[key]=data[key]+(['']*(max-len(data[key])))
        data=pd.DataFrame.from_dict(data)
        summut=pd.DataFrame.from_dict(summut,orient='index')
        summut.columns=['突变数总和']
        self.mutation_distribution=data
        self.summut=summut
        # data.to_excel('D:/mo/11.11/年龄段-突变数分布.xlsx')
        # summut.to_excel('D:/mo/11.11/年龄段-突变数总和.xlsx')

    def RefCHIP21genes(self):
        data=[]
        CHIPlist=self.CHIP['GeneName'].tolist()
        for pat in self.patientlist:
            if len(list(set(self.raw_data[self.raw_data['姓名']==pat]['基因'].tolist()).intersection(set(CHIPlist))))>0:
                data.append([pat,self.raw_data[self.raw_data['姓名']==pat]['年龄'].iloc[0],1])
            else:
                data.append([pat, self.raw_data[self.raw_data['姓名'] == pat]['年龄'].iloc[0], 0])
        data = pd.DataFrame(data, columns=['姓名', '年龄', 'CHIP突变？'])
        self.isCHIP=data
        # data.to_excel('D:/mo/11.11/姓名-年龄-？CHIP.xlsx')

    def RefCHIPfrel(self):
        data={}
        CHIPlist=self.CHIP['GeneName'].tolist()
        max = 0
        for gene in CHIPlist:
            data[gene] = self.raw_data[self.raw_data['基因'] == gene]['freq'].tolist()
            if len(data[gene]) > max:
                max = len(data[gene])
        for key in data.keys():
            data[key]=data[key]+(['']*(max-len(data[key])))
        data = pd.DataFrame.from_dict(data)
        self.CHIPfrel=data
        # data.to_excel('D:/mo/11.11/CHIPfrel.xlsx')

    def CHIP_age(self):
        rangelist=[]
        for i in range(9):
            rangelist.append(str(i*10)+'-'+str(i*10+10))
        CHIPlist = self.CHIP['GeneName'].tolist()
        data = pd.DataFrame(columns=CHIPlist,index=rangelist)
        data=data.fillna(0)
        for chipgene in CHIPlist:
            for pat in self.patientlist:
                chipdata=self.raw_data[(self.raw_data['基因']==chipgene)&(self.raw_data['姓名']==pat)]
                if len(chipdata)>0:
                    agerange = str(chipdata['年龄'].iloc[0] // 10 * 10) + '-' + str(chipdata['年龄'].iloc[0] // 10 * 10 + 10)
                    data[chipgene].loc[agerange] += len(set(chipdata['pro1'].tolist()))
        data.loc['Row_sum'] = data.apply(lambda x: x.sum())
        data['Col_sum'] = data.apply(lambda x: x.sum(), axis=1)
        data=data.T.sort_values(by='Row_sum',ascending=False)
        self.top5CHIP=data.index.tolist()[1:6]
        self.otherCHIP=data.index.tolist()[6:]
        self.notinCHIP=list(set(self.raw_data['基因'].tolist()).difference(set(CHIPlist)))
        self.CHIPmutationnum=data
        # data.to_excel('D:/mo/11.11/年龄段-CHIP突变数.xlsx')

    def CHIP_age2(self):
        rangelist=[]
        for i in range(9):
            rangelist.append(str(i*10)+'-'+str(i*10+10))

        data = pd.DataFrame(columns=self.top5CHIP+['OTHER IN CHIP','NOT IN CHIP'],index=rangelist)
        data=data.fillna(0)
        for chipgene in self.top5CHIP:
            for pat in self.patientlist:
                chipdata=self.raw_data[(self.raw_data['基因']==chipgene)&(self.raw_data['姓名']==pat)]
                if len(chipdata)>0:
                    agerange=str(chipdata['年龄'].iloc[0]//10*10)+'-'+str(chipdata['年龄'].iloc[0]//10*10+10)
                    data[chipgene].loc[agerange]+=len(set(chipdata['pro1'].tolist()))
        for chipgene in self.otherCHIP:
            for pat in self.patientlist:
                chipdata=self.raw_data[(self.raw_data['基因']==chipgene)&(self.raw_data['姓名']==pat)]
                if len(chipdata)>0:
                    agerange = str(chipdata['年龄'].iloc[0] // 10 * 10) + '-' + str(chipdata['年龄'].iloc[0] // 10 * 10 + 10)
                    data['OTHER IN CHIP'].loc[agerange] += len(set(chipdata['pro1'].tolist()))
        for chipgene in self.notinCHIP:
            for pat in self.patientlist:
                chipdata=self.raw_data[(self.raw_data['基因']==chipgene)&(self.raw_data['姓名']==pat)]
                if len(chipdata)>0:
                    agerange = str(chipdata['年龄'].iloc[0] // 10 * 10) + '-' + str(chipdata['年龄'].iloc[0]// 10 * 10 + 10)
                    data['NOT IN CHIP'].loc[agerange] += len(set(chipdata['pro1'].tolist()))

        data.loc['Row_sum'] = data.apply(lambda x: x.sum())
        data['Col_sum'] = data.apply(lambda x: x.sum(), axis=1)
        data=data.T.sort_values(by='Row_sum',ascending=False)
        self.Top5CHIP=data
        # data.to_excel('D:/mo/11.11/年龄段-TOP5CHIP突变数.xlsx')


if __name__=="__main__":
    main('D:/mo/11.11/2016-2017.11.11-Only AML-paneldata -excludeNagetive.xlsx')





