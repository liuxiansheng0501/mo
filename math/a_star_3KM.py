#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/17 0:36
# @Author  : liulijun
# @Site    : 
# @File    : a_star.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import math
from datetime import datetime
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt


#########################################################
class Node_Elem:
    """
    开放列表和关闭列表的元素类型，parent用来在成功的时候回溯路径
    """

    def __init__(self, parent, x, y, dist):
        self.parent = parent
        self.x = x
        self.y = y
        self.dist = dist


class A_Star:
    """
    A星算法实现类
    """

    # 注意w,h两个参数，如果你修改了地图，需要传入一个正确值或者修改这里的默认参数
    def __init__(self, s_x, s_y, e_x, e_y,map, w=60, h=30 ):
        self.s_x = s_x
        self.s_y = s_y
        self.e_x = e_x
        self.e_y = e_y

        self.width = w
        self.height = h

        self.open = []
        self.close = []
        self.path = []

        self.map=map

    # 查找路径的入口函数
    def find_path(self):
        # 构建开始节点
        p = Node_Elem(None, self.s_x, self.s_y, 0.0)
        while True:
            # 扩展F值最小的节点
            self.extend_round(p)
            # 如果开放列表为空，则不存在路径，返回
            if not self.open:
                return
            # 获取F值最小的节点
            idx, p = self.get_best()
            # 找到路径，生成路径，返回
            if self.is_target(p):
                self.make_path(p)
                return
            # 把此节点压入关闭列表，并从开放列表里删除
            self.close.append(p)
            print(len(self.close))
            del self.open[idx]

    def make_path(self, p):
        # 从结束点回溯到开始点，开始点的parent == None
        while p:
            self.path.append((p.x, p.y))
            p = p.parent

    def is_target(self, i):
        return i.x == self.e_x and i.y == self.e_y

    def get_best(self):
        best = None
        bv = 1000000  # 如果你修改的地图很大，可能需要修改这个值
        bi = -1
        for idx, i in enumerate(self.open):
            value = self.get_dist(i)  # 获取F值
            if value < bv:  # 比以前的更好，即F值更小
                best = i
                bv = value
                bi = idx
        return bi, best

    def get_dist(self, i):
        # F = G + H
        # G 为已经走过的路径长度， H为估计还要走多远
        # 这个公式就是A*算法的精华了。
        return i.dist + math.sqrt(
            (self.e_x - i.x) * (self.e_x - i.x)
            + (self.e_y - i.y) * (self.e_y - i.y)) * 1.2

    def extend_round(self, p):
        # 可以从8个方向走
        xs = (-1, 0, 1, -1, 1, -1, 0, 1)
        ys = (-1, -1, -1, 0, 0, 1, 1, 1)
        # 只能走上下左右四个方向
        #        xs = (0, -1, 1, 0)
        #        ys = (-1, 0, 0, 1)
        # print(p.x,p.y)
        for x, y in zip(xs, ys):
            new_x, new_y = x + p.x, y + p.y
            # 无效或者不可行走区域，则勿略
            if not self.is_valid_coord(new_x, new_y):
                continue
            # 构造新的节点
            node = Node_Elem(p, new_x, new_y, p.dist + self.get_cost(
                p.x, p.y, new_x, new_y))
            # 新节点在关闭列表，则忽略
            if self.node_in_close(node):
                continue
            i = self.node_in_open(node)
            if i != -1:
                # 新节点在开放列表
                if self.open[i].dist > node.dist:
                    # 现在的路径到比以前到这个节点的路径更好~
                    # 则使用现在的路径
                    self.open[i].parent = p
                    self.open[i].dist = node.dist
                continue
            self.open.append(node)

    def get_cost(self, x1, y1, x2, y2):
        """
        上下左右直走，代价为1.0，斜走，代价为1.4
        """
        if x1 == x2 or y1 == y2:
            return 1
        return 1.4

    def node_in_close(self, node):
        for i in self.close:
            if node.x == i.x and node.y == i.y:
                return True
        return False

    def node_in_open(self, node):
        for i, n in enumerate(self.open):
            if node.x == n.x and node.y == n.y:
                return i
        return -1

    def is_valid_coord(self, x, y):

        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        else:
            # print('eomi',x,y,self.width,x >= self.width)
            return self.map[y][x] != 1

    def get_searched(self):
        l = []
        for i in self.open:
            l.append((i.x, i.y))
        for i in self.close:
            l.append((i.x, i.y))
        return l


#########################################################
class main:

    def __init__(self,start_position,end_position,sl,el):

        print(datetime.now())
        self.sp=start_position
        self.ep=end_position
        self.sl=sl
        self.el=el
        self.map()
        # self.print_map()
        print(datetime.now())
        self.find_path()
        print(datetime.now())
        self.print_map()
        print(datetime.now())

    def map(self):

        self.map=[]
        self.map_copy=[]
        # trainFile='D:/mo/数学建模/min0.csv'
        # pwd = os.getcwd()
        # os.chdir(os.path.dirname(trainFile))
        # data = pd.read_csv(os.path.basename(trainFile))
        # os.chdir(pwd)

        trainFile = 'D:/mo/数学建模/区域高程数据.xlsx'
        data = pd.read_excel(trainFile, sheetsname='Sheet1')
        # print(data)

        self.map_row=925
        self.map_col=971

        for icol in range(self.map_col):
            iz = []
            iz_copy=[]
            for irow in range(self.map_row):
                # print(irow,icol,data.iat[irow,icol],data.iat[icol,irow])
                iz_copy.append(int(data.iat[irow,icol]))
                if data.iat[irow, icol] > 3000:
                    iz.append(1)
                else:
                    iz.append(0)
                # break
            # break
            self.map.append(iz)
            self.map_copy.append(iz_copy)

    def print_map(self):

        path_x=[]
        path_y=[]

        for node in self.path:
            path_x.append(node[0])
            path_y.append(node[1])

        x, y = np.meshgrid(range(self.map_row), range(self.map_col))

        plt.contourf(x, y, self.map, 10, alpha=0.6, cmap=plt.cm.hot)

        C = plt.contour(x, y, self.map, 5, colors='black', linewidth=0.5)

        plt.plot(path_x,path_y,'--r')

        plt.clabel(C, inline=True, fontsize=10)

        plt.grid

        plt.show()

        # plt.savefig('')


    def get_start_XY(self):

        return self.sp[0],self.sp[1]


    def get_end_XY(self):
        return self.ep[0],self.ep[1]


    def get_symbol_XY(self,s):
        for y, line in enumerate(self.map):
            try:
                x = line.index(s)
            except:
                continue
            else:
                break
        return x, y


    #########################################################
    def mark_path(self,l):
        self.mark_symbol(l, 0)


    def mark_searched(self,l):
        pass
        # self.mark_symbol(l, 3)


    def mark_symbol(self,l, s):
        for x, y in l:
            self.map[y][x] = s


    def mark_start_end(self,s_x, s_y, e_x, e_y):

        self.map[s_y][s_x] = 0
        self.map[e_y][e_x] = 0


    def tm_to_test_map(self):
        for line in tm:
            self.map.append(list(line))


    def find_path(self):
        s_x, s_y = self.get_start_XY()
        e_x, e_y = self.get_end_XY()
        a_star = A_Star(s_x, s_y, e_x, e_y, self.map, self.map_row, self.map_col)
        a_star.find_path()
        searched = a_star.get_searched()
        self.path = a_star.path
        # 标记已搜索区域
        self.mark_searched(searched)
        # 标记路径
        self.mark_path(self.path)
        pathchain=[]
        for id in range(len(self.path)):
            node=self.path[id]
            if id:
                if math.fabs(self.path[id][0]-self.path[id-1][0])==1 and math.fabs(self.path[id][1]-self.path[id-1][1])==1:
                    pathchain.append([node[0],node[1],self.map_copy[node[1]][node[0]],pathchain[-1][3]+1.414*38.2*3/1000])
                else:
                    pathchain.append([node[0], node[1], self.map_copy[node[1]][node[0]], pathchain[-1][3]+38.2 * 3 / 1000])
            else:
                pathchain.append([node[0], node[1], self.map_copy[node[1]][node[0]],0])
        pathchain=pd.DataFrame(pathchain,columns=['x','y','h','dist'])
        pathchain.to_csv('D:/mo/数学建模/'+self.sl+'-'+self.el+'.csv')
        print("path length is %d" % (len(self.path)))
        print("searched squares count is %d" % (len(searched)))
        # 标记开始、结束点
        self.mark_start_end(s_x, s_y, e_x, e_y)


if __name__ == "__main__":

    position = {'A': [264, 784],
                'B': [576, 739],
                'C': [859, 669],
                'D': [643, 532],
                'E': [505, 415],
                'F': [757, 192],
                'G': [817, 426],
                'H': [924, 0]}
    target=list(position.keys())
    for start_id in range(len(target)):
        if start_id<len(target)-1:
            for end_id in range(start_id+1,len(target)):
                start_position=position[target[start_id]]
                end_position = position[target[end_id]]
                print(target[start_id],'-',target[end_id],start_position,'-',end_position)
                main(start_position,end_position,target[start_id],target[end_id])
