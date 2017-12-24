#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/17 18:29
# @Author  : liulijun
# @Site    : 
# @File    : dist.py
# @Software: PyCharm

import pandas as pd
import os
import math

if __name__=='__main__':

    trainFile = 'D:/mo/数学建模/G-H.csv'
    pwd = os.getcwd()
    os.chdir(os.path.dirname(trainFile))
    data = pd.read_csv(os.path.basename(trainFile))
    data['dist']=''
    # print(data[['x','y','h','dist']])
    os.chdir(pwd)

    for id in range(len(data)):

        if id:
            if math.fabs(data['x'].iloc[id]-data['x'].iloc[id-1])==1 and math.fabs(data['y'].iloc[id]-data['y'].iloc[id-1])==1:
                data['dist'].iloc[id]=data['dist'].iloc[id-1]+1.414*38.2*3/1000
            else:
                data['dist'].iloc[id] = data['dist'].iloc[id - 1] +  38.2 * 3 / 1000
        else:
            data['dist'].iloc[id] = 0
    data[['x', 'y', 'h', 'dist']].to_csv(trainFile)