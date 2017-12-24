#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/19 21:51
# @Author  : liulijun
# @Site    : 
# @File    : avg_height.py
# @Software: PyCharm

import os
import pandas as pd

def map_from_csv():

    map = []
    trainFile = 'D:/mo/数学建模/min0.csv'
    pwd = os.getcwd()
    os.chdir(os.path.dirname(trainFile))
    data = pd.read_csv(os.path.basename(trainFile))
    os.chdir(pwd)

    map_row = 925
    map_col = 971

    for icol in range(map_col):
        iz = []
        for irow in range(map_row):
            iz.append(int(data.iat[irow, icol]))
        map.append(iz)

def map_from_excel():


    trainFile = 'D:/mo/数学建模/区域高程数据.xlsx'
    data = pd.read_excel(trainFile,sheetsname='Sheet1')
    # trainFile = 'D:/mo/数学建模/min0.csv'
    # pwd = os.getcwd()
    # os.chdir(os.path.dirname(trainFile))
    # data = pd.read_csv(os.path.basename(trainFile))
    # os.chdir(pwd)

    map_max = []
    map_min = []
    map_mean = []
    id_map=[]
    cover_map=[]

    row=data.shape[0]
    col=data.shape[1]

    size=31

    for xid in range(0,int(row/size)+1):

        map_min_line = []
        map_max_line = []
        map_mean_line = []
        id_map_line=[]
        cover_map_line=[]
        for yid in range(0, int(col / size) + 1):

            xfrom=size*yid
            xto=size*(yid+1)-1
            xrange=[num for num in range(xfrom,xto+1)]
            # print('xrange',xrange[-1])

            yfrom = row - 1 - size * (xid + 1) + 1
            yto = row - 1 - size * (xid)
            yrange = [num for num in range(yfrom, yto + 1)]
            # print('yrange',yrange)
            if str(xrange[-1]) not in list(data.columns):
                xrange=xrange[0:col-int(xrange[0])]
                # print('xrange',xrange[-1])
            avg_data = data.iloc[yrange, xrange]
            # print('data',avg_data)
            print(xid,yid,'da', '最小值',avg_data.min().min(),'最大值',avg_data.max().max(),'平均值',avg_data.mean().mean())
            map_min_line.append(avg_data.min().min())
            map_max_line.append(avg_data.max().max())
            map_mean_line.append(avg_data.mean().mean())
            id_map_line.append((int((yfrom+yto)/2),int((xfrom+xto)/2)))
            cover_map_line.append(sum(avg_data[avg_data<=3000].count().tolist())/size/size)

        map_min.append(map_min_line)
        map_max.append(map_max_line)
        map_mean.append(map_mean_line)
        id_map.append(id_map_line)
        cover_map.append(cover_map_line)

    map_min = pd.DataFrame (map_min,columns=None,index=None)
    map_max = pd.DataFrame (map_max, columns=None, index=None)
    map_mean = pd.DataFrame (map_mean, columns=None, index=None)
    id_map = pd.DataFrame (id_map, columns=None, index=None)
    cover_map = pd.DataFrame(cover_map, columns=None, index=None)
    map_min.to_csv('D:/mo/数学建模/组合网格/map_min.csv')
    map_max.to_csv('D:/mo/数学建模/组合网格/map_max.csv')
    map_mean.to_csv('D:/mo/数学建模/组合网格/map_mean.csv')
    id_map.to_csv('D:/mo/数学建模/组合网格/id_map.csv')
    cover_map.to_csv('D:/mo/数学建模/组合网格/cover_map.csv')



if __name__=="__main__":
    map_from_excel()

