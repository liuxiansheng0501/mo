#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 20:30
# @Author  : liulijun
# @Site    : 
# @File    : location.py
# @Software: PyCharm

import pandas as pd
import sys
import datetime

if len(sys.argv)!=5:
    print('please input argv like: chunkSize file1 file2 output')
else:
    sourceData=[]
    targetData=[]
    print('reading...')
    reader = pd.read_table(str(sys.argv[2:3][0])+".txt", iterator=True,header=None)
    loop = True
    chunkSize = int(sys.argv[1:2][0])
    chunks = []
    print('large file...')
    print('row size','\t','read time','\t','append time')
    while loop:
        try:
            st=datetime.datetime.now()
            chunk = reader.get_chunk(chunkSize)
            et=datetime.datetime.now()
            delta=(et-st).seconds/60
            chunks.append(chunk)
            at=datetime.datetime.now()
            delta_a=(at-et).seconds/60
            print(len(chunk),'\t',delta,'\t',delta_a)
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    sourceData = pd.concat(chunks, ignore_index=True)
    sourceData.columns=['chr','pos','c3','c4','c5','c6']

    #small file
    reader = pd.read_table(str(sys.argv[3:4][0]) + ".txt", iterator=True, header=None)
    loop = True
    chunkSize = int(sys.argv[1:2][0])
    chunks = []
    print('small file...')
    print('row size', '\t', 'read time', '\t', 'append time')
    while loop:
        try:
            st = datetime.datetime.now()
            chunk = reader.get_chunk(chunkSize)
            et = datetime.datetime.now()
            delta = (et - st).seconds / 60
            chunks.append(chunk)
            at = datetime.datetime.now()
            delta_a = (at - et).seconds / 60
            print(len(chunk), '\t', delta, '\t', delta_a)
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    targetData = pd.concat(chunks, ignore_index=True)
    targetData.columns = targetData[0:1].T[0].tolist()
    targetData=targetData.drop(0)
    targetData['large_c4']=''

    # find position
    for row in range(len(targetData)):
        chr=str(targetData['Chr'].iloc[row])
        pos =int(targetData['Pos'].iloc[row])
        if len(sourceData[(sourceData['chr']==chr)&(sourceData['pos']==pos)])>0:
            large_c4_value=sourceData[(sourceData['chr']==chr)&(sourceData['pos']==pos)]['c4'].iloc[0]
            targetData['large_c4'].iloc[row]=large_c4_value
    # export
    print('Results have exported to '+str(sys.argv[-1])+'.csv')
    targetData[['Chr','Pos','large_c4']].to_csv(str(sys.argv[-1])+'.csv')


