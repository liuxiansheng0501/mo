#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/19 15:26
# @Author  : liulijun
# @Site    : 
# @File    : shortest_path.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt


class main:

    def __init__(self,position_list):

        self.ps=position_list
        self.map()
        self.print_map()

    def map(self):

        self.map=[]
        self.map_copy=[]
        trainFile='D:/mo/数学建模/min.csv'
        pwd = os.getcwd()
        os.chdir(os.path.dirname(trainFile))
        data = pd.read_csv(os.path.basename(trainFile))
        os.chdir(pwd)

        self.map_row=925
        self.map_col=971

        for icol in range(self.map_col):
            iz = []
            iz_copy=[]
            for irow in range(self.map_row):
                iz_copy.append(int(data.iat[irow,icol]))
                if data.iat[irow, icol] <=4150:
                    iz.append(0)
                else:
                    iz.append(1)
            self.map.append(iz)
            self.map_copy.append(iz_copy)

    def print_map(self):

        path_x=[]
        path_y=[]

        for node in self.path:
            path_x.append(node[0])
            path_y.append(node[1])

        x, y = np.meshgrid(range(self.map_row), range(self.map_col))

        plt.contourf(x, y, self.map, 20, alpha=0.8, cmap=plt.cm.cool)

        C = plt.contour(x, y, self.map, 5, colors='black', linewidth=0.2)

        plt.plot(path_x,path_y,'--r')

        plt.clabel(C, inline=True, fontsize=5)

        plt.xlabel('x')

        plt.ylabel('y')

        plt.grid

        plt.show()

def read_path_data(name,type):

    trainFile = 'D:/mo/数学建模/最短路径/'+name+'.csv'
    pwd = os.getcwd()
    os.chdir(os.path.dirname(trainFile))
    data = pd.read_csv(os.path.basename(trainFile))
    os.chdir(pwd)
    return_data=[]
    if type:
        for i in range(len(data['x'].tolist())):
            pass



if __name__ == "__main__":

    position = {'A': [264, 784],
                'B': [576, 739],
                'C': [859, 669],
                'D': [643, 532],
                'E': [505, 415],
                'F': [757, 192],
                'G': [817, 426],
                'H': [924, 0]}
